import time
import webbrowser
import random
import string
import os
import pyautogui

def get_random_string(length):
    letters = string.ascii_lowercase + string.ascii_uppercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str



for i in range(0, 35):
    pyautogui.click(240, 60)
    pyautogui.hotkey("ctrl", "a")
    pyautogui.press("delete")
    pyautogui.typewrite("https://www.bing.com/search?q="+get_random_string(32))
    pyautogui.press("enter")
    time.sleep(0.2)