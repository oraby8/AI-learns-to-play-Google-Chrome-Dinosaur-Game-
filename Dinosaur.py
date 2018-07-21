from PIL import ImageGrab,ImageOps
import pyautogui
import time
import numpy as np

class Cordinates():
    replay=(250,200)#GameOver cordinate
    dinosaur=(122,202)#dinosaur cordinate
    y=205
    x=158
    
def replaygame():
    #to repaly the Game
    pyautogui.click(Cordinates.replay)

    
def jumping():
    #to make jump
    pyautogui.keyDown('space')
    time.sleep(0.001)
    print("jump")
    pyautogui.keyUp('space')

def imagegrab():
    box=(Cordinates.dinosaur[0]+10,Cordinates.dinosaur[1],Cordinates.x+40,Cordinates.dinosaur[1]+20)

    image=ImageGrab.grab(box)
    grayimage=ImageOps.grayscale(image)
    a=np.array(grayimage.getcolors())
    b=a.sum()
    return(b)


replaygame()
while True:
    if imagegrab() != 1567:
        print(imagegrab())
        jumping()
    
