import pyautogui
import time

txt = input('Enter text:')
while True:
    time.sleep(5)
    pyautogui.typewrite(txt)
    pyautogui.press('enter')
