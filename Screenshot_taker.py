import pyautogui
import schedule
import time


def screen():
    screen = pyautogui.screenshot()
    screen.save('F:\\Download\\shot_screen.png')


schedule.every(10).seconds.do(screen)
while True:
    schedule.run_pending()
    time.sleep(1)  # wait
