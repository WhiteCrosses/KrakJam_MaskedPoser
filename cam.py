# import the opencv library 
import cv2 
import numpy as np


# define a video capture object 
vid = cv2.VideoCapture(0) 
vid2 = cv2.VideoCapture(0) 

vid.set(cv2.CAP_PROP_AUTO_EXPOSURE, 1)
vid.set(cv2.CAP_PROP_EXPOSURE, -5)

vid2.set(cv2.CAP_PROP_AUTO_EXPOSURE, 1)
vid2.set(cv2.CAP_PROP_EXPOSURE, -5)


mymask = cv2.imread("Test_mask.png") # mask shape must = template
isBg = False
ret, bg = vid2.read()
backup_bg = bg

mymask = cv2.resize(mymask, (bg.shape[1], bg.shape[0]))
#mymask = cv2.normalize(mymask, None, 0, 1.0, cv2.NORM_MINMAX, dtype=cv2.CV_32F)

mymask = 255 - mymask
mymask_gray = cv2.cvtColor(mymask, cv2.COLOR_BGR2GRAY)
mymask_blur = cv2.GaussianBlur(mymask_gray, (7, 7), 0)
(T, mymask) = cv2.threshold(mymask_blur, 200, 255, cv2.THRESH_BINARY_INV)
 
def remove_noise(img):
    img_no_noise = np.zeros_like(img)

    labels,stats= cv2.connectedComponentsWithStats(img.astype(np.uint8),connectivity=4)[1:3]

    largest_area_label = np.argmax(stats[1:, cv2.CC_STAT_AREA]) +1

    img_no_noise[labels==largest_area_label] = 1
    return img_no_noise

def process_image(frame, bg):
    #frame = cv2.normalize(frame, None, 0, 1.0, cv2.NORM_MINMAX, dtype=cv2.CV_32F)
    print("frame size : ", frame.shape)
    print("mask size : ", mymask.shape)
    print("person captured")
    
    difference = 255 - cv2.absdiff(frame, bg)
    gray = cv2.cvtColor(difference, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (7, 7), 0)
    (T, difference) = cv2.threshold(blur, 220, 255,
	cv2.THRESH_BINARY_INV)
    return difference

def normalize(image):
    pass


while(True): 
    ret, bg = vid2.read()
    while(not isBg):
        ret, bg = vid2.read()
        #bg = cv2.normalize(bg, None, 0, 1.0, cv2.NORM_MINMAX, dtype=cv2.CV_32F)
        backup_bg = bg
        cv2.imshow('bg', bg)
        if cv2.waitKey(1) & 0xFF == ord('c'): 
            isBg = True
            vid2.release()
            cv2.destroyAllWindows()
            break
    bg = backup_bg

	# Capture the video frame 
	# by frame 
    ret, frame = vid.read()
    
    difference = process_image(frame, bg)
    
    print("frame size : ", difference.shape)
    print("mask size : ", mymask.shape)

    mask_diff = 255 - cv2.absdiff(difference, mymask)
    res = mask_diff.astype(np.uint8)
    percentage = percentage = (np.count_nonzero(res) * 100)/ res.size
    print(percentage)

    cv2.imshow('frame', mask_diff)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    elif cv2.waitKey(1) & 0xFF == ord('w'):
        pass

	# the 'q' button is set as the 
	# quitting button you may use any 
	# desired button of your choice 

# After the loop release the cap object 
#vid.release() 
# Destroy all the windows 
#cv2.destroyAllWindows() 
