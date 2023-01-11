import subprocess
import tkinter as tk
import time
import pyautogui
import string
import random

# Resources
lock = 0
screenWidth = pyautogui.size().width
screenHeight = pyautogui.size().height

def kill():
    # Terminate all Microsoft Edge processes
    subprocess.run(['taskkill', '/F', '/IM', 'msedge.exe'], shell=True)

def run(mode="desktop"):
    # Start MS Edge
    if mode == "desktop":
        subprocess.run(['start', 'msedge'], shell=True)
        print("desktop mode")

    elif mode == "mobile":
        subprocess.run(['start', 'msedge', '--auto-open-devtools-for-tabs'], shell=True)
        print("mobile mode")

def get_random_string(length):
    letters = string.ascii_lowercase + string.ascii_uppercase
    result_str = ''.join(random.choice(letters) for i in range(length))

    if random.randint(1, 10_000) == 666:
        result_str = "careless hangman"

    return result_str

if __name__ == "__main__":
    try:
        run("desktop")
        time.sleep(3)
        urlBarLocation = pyautogui.locateOnScreen('Screenshot_687.png')
        while urlBarLocation == None:
            if lock == 0:
                urlBarLocation = pyautogui.locateOnScreen('Screenshot_687.png')
                lock = 1
            elif lock == 1:
                urlBarLocation = pyautogui.locateOnScreen('Screenshot_686.png')
                lock = 2
            elif lock == 2:
                urlBarLocation = pyautogui.locateOnScreen('Screenshot_687.png')
                lock = 0
        print(urlBarLocation,"\nlock =",lock)
        x, y, w, h = urlBarLocation
        print((x + w)//2, (y + h//2))
        pyautogui.moveTo((x + w)//2 + 120, (y + h//2))
        for i in range(0, 30):
            pyautogui.click()
            pyautogui.hotkey('ctrl', 'a')
            pyautogui.press('delete')
            pyautogui.typewrite(get_random_string(16))
            pyautogui.press("enter")
    except:
        print("Task 'run' failed")
    finally:
        kill()
        print("finished")