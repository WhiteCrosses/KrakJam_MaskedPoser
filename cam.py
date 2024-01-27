# import the opencv library 
import cv2 
import numpy as np
import pygame
import sys

class CamManager:
    def __init__(self):
        # define a video capture object 
        self.vid = cv2.VideoCapture(0, cv2.CAP_DSHOW) 
        self.bg_vid = cv2.VideoCapture(0, cv2.CAP_DSHOW) 

        self.vid.set(cv2.CAP_PROP_AUTO_EXPOSURE, 1)
        self.vid.set(cv2.CAP_PROP_EXPOSURE, -5)

        self.bg_vid.set(cv2.CAP_PROP_AUTO_EXPOSURE, 1)
        self.bg_vid.set(cv2.CAP_PROP_EXPOSURE, -5)

        self.mymask = cv2.imread("./Mockup/mockpose.png") # mask shape must = template
        self.isBg = False
        self.ret, self.bg = self.bg_vid.read()
        self.backup_bg = self.bg

        self.mymask = cv2.resize(self.mymask, (self.bg.shape[1], self.bg.shape[0]))
        self.screen_image = self.bg

        self.mymask = 255 - self.mymask
        mymask_gray = cv2.cvtColor(self.mymask, cv2.COLOR_BGR2GRAY)
        mymask_blur = cv2.GaussianBlur(mymask_gray, (7, 7), 0)
        (T, self.mymask) = cv2.threshold(mymask_blur, 200, 255, cv2.THRESH_BINARY_INV)

    def remove_noise(self, img):
        img_no_noise = np.zeros_like(img)

        labels,stats= cv2.connectedComponentsWithStats(img.astype(np.uint8),connectivity=4)[1:3]

        largest_area_label = np.argmax(stats[1:, cv2.CC_STAT_AREA]) +1

        img_no_noise[labels==largest_area_label] = 1
        return img_no_noise

    def process_image(self, frame, bg):

        difference = 255 - cv2.absdiff(frame, bg)
        gray = cv2.cvtColor(difference, cv2.COLOR_BGR2GRAY)
        blur = cv2.GaussianBlur(gray, (7, 7), 0)
        (T, difference) = cv2.threshold(blur, 220, 255,
        cv2.THRESH_BINARY_INV)
        return difference

    def process_mask(self, mask, frame):
        mask_diff = 255 - cv2.absdiff(frame, mask)
        return mask_diff

    def get_percentage(self, image):
        res = image.astype(np.uint8)
        percentage = percentage = (res.size - np.count_nonzero(res) * 100)/ res.size
        return percentage

    def normalize(image):
        pass

    def check_if_captured(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
                if event.key == pygame.K_ESCAPE:
                    print("CLOSING")
                    pygame.quit()
                    sys.exit()
                if event.key == pygame.K_c:
                    return True

        return False



        if cv2.waitKey(1) & 0xFF == ord('c'): 
            return True
        else:
            return False

    def get_background(self):
        if(not self.isBg):
            ret, self.bg = self.bg_vid.read()
            #bg = cv2.normalize(bg, None, 0, 1.0, cv2.NORM_MINMAX, dtype=cv2.CV_32F)
            #cv2.imshow('bg', self.bg)
            self.backup_bg = self.bg
            if self.check_if_captured():
                print("captured")
                self.isBg = True
                
                #Capture frame from the camera
                ret, frame = self.vid.read()
                
                #Create image from difference of camera image and saved background
                difference = self.process_image(frame, self.bg)

                #Calculate difference between frame and applied mask
                mask_diff = self.process_mask(self.mymask, difference)
                
                #Calculate percentage from created difference of mask and image
                base_percentage = self.get_percentage(mask_diff)

                #break
        return self.bg

    def check_for_closing(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
                if event.key == pygame.K_ESCAPE:
                    print("CLOSING")
                    pygame.quit()
                    sys.exit()

    def cam_loop(self):
            self.get_background()
            self.check_for_closing()
            #Load bg image from saved one
            self.bg = self.backup_bg
            
            #Capture frame from the camera
            ret, frame = self.vid.read()
            
            #Create image from difference of camera image and saved background
            difference = self.process_image(frame, self.bg)

            #Calculate difference between frame and applied mask
            mask_diff = self.process_mask(self.mymask, difference)
            
            #Calculate percentage from created difference of mask and image
            percentage = self.get_percentage(mask_diff)



            #if((100 + percentage) < 80):
            #    print(1)
            #elif((100 + percentage) < 90):
            #    print(2)
            #else:
            #    print(3)

            self.screen_image = mask_diff

            return self.screen_image

            # the 'q' button is set as the 
            # quitting button you may use any 
            # desired button of your choice 

        # After the loop release the cap object 
        #vid.release() 
        # Destroy all the windows 
        #cv2.destroyAllWindows() 
