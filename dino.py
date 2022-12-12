import pyautogui as ai
from PIL import Image, ImageGrab # PIL is pillow
# from numpy import asarray
import time

def hit(key):
    ai.keyDown(key)

def isCollide(data):
    for i in range(280,330):
        for j in range(600,700):
            if(data[i,j]<85):
                hit("up")
                return
    return 
    
# def takeSS():
#     img=ImageGrab.grab().convert('L')
#     img.show()

if __name__=="__main__":
    time.sleep(2)
    print("Starting in 2 sec...")
    # hit("up")
    while True:
        img=ImageGrab.grab().convert('L') #returns an associative array

        data=img.load() #data is storing the pixels, 0 means black and 255 means white. So, less than 100 tends to black ;)
        # break
        isCollide(data)
    
    # draw a rectangle
    for i in range(280,330):
        for j in range(600,700):
            data[i,j]=80
    img.show()
    # print(asarray(img))