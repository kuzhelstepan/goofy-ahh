import pyautogui
import time
time.sleep(4)
count=0
while count<=100:
    pyautogui.typewrite('Long Live The Ottoman Empire')
    pyautogui.press("enter")
    count=count+1
