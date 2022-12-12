import pyautogui as ai
import time
time.sleep(4)
i=1
while (i!=50):
    ai.keyDown('H')
    ai.keyDown('E')
    ai.keyDown('L')
    ai.keyDown('L')
    ai.keyDown('O')
    ai.write(str(i)+" ^_^")
    ai.keyDown('enter')
    i+=1
