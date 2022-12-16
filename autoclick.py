# get screen info and click the exit button
import pyautogui
import time
import cv2

# find the exit button
while True:
    exitButton = pyautogui.locateOnScreen('./exit.png')
    print(exitButton)
    # click the exit button
    if exitButton:
        pyautogui.click(exitButton)
        pyautogui.click(exitButton)
        break
