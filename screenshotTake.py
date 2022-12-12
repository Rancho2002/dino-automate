from PIL import Image, ImageGrab # PIL is pillow
import time

def takeSS():
    img=ImageGrab.grab()
    img.show()

if __name__=="__main__":
    time.sleep(2)
    takeSS()