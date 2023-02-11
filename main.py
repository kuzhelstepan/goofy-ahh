import pyautogui
import time
time.sleep(4)
count=0
while count<=40:
    pyautogui.typewrite('Goofy Ahh')
    pyautogui.press("enter")
    count=count+1