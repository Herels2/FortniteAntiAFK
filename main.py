import os
import time
import keyboard
import pyautogui
import random
import datetime
import ctypes

ctypes.windll.kernel32.SetConsoleTitleA(b"Fortnite AntiAFK by Sterrist (https://t.me/Sterrist)")
hour = datetime.datetime.now()

try:
    while True:
        tickkc = random.randint(1, 10)
        pyautogui.click(tickkc, interval=tickkc)
        print(f'{hour}: Click')
        time.sleep(random.randint(1,5))
        keyboard.press('w')
        time.sleep(random.randint(1, 5))
        keyboard.release('w')
        print(f'{hour}: Pressed W')
        time.sleep(random.randint(1,5))
        keyboard.press('s')
        time.sleep(random.randint(1, 5))
        keyboard.release('s')
        print(f'{hour}: Pressed S')
        pyautogui.click(tickkc, interval=tickkc)
        print(f'{hour}: Click')
        time.sleep(random.randint(1,5))
        keyboard.press('d')
        time.sleep(random.randint(1, 5))
        keyboard.release('d')
        print(f'{hour}: Pressed D')
        time.sleep(random.randint(1, 5))
        keyboard.press('a')
        time.sleep(random.randint(1, 5))
        keyboard.release('a')
        print(f'{hour}: Pressed A')
        pyautogui.click(tickkc, interval=tickkc)
        print(f'{hour}: Click')

except KeyboardInterrupt:
    print(f'{hour}: Stopped')
    os.system('pause')