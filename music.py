from pygame import mixer

def load_music():
    #init the mixer
    mixer.init()
    mixer.music.load("audio/mus_poza_easy_v1.wav")
    mixer.music.set_volume(1.0)
    mixer.music.play(-1)

def load_button_sound():
    mixer.init()
    mixer.music.load("audio/sfx_gui_2.wav")
    mixer.music.set_volume(1.0)
    mixer.music.play()