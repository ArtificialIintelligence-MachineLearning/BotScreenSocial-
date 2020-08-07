import time
import pyautogui
start_time = time.time()
seconds = 30
while True:
    current_time = time.time()
    elapsed_time = current_time - start_time
    if elapsed_time > seconds:
        screenWidth, screenHeight = pyautogui.size()
        currentMouseX, currentMouseY = pyautogui.position()
        pyautogui.moveTo(100, 50)
        pyautogui.click()
        pyautogui.moveTo(1070, 100)
        pyautogui.doubleClick()
        pyautogui.doubleClick()
        pyautogui.doubleClick()
        pyautogui.doubleClick()
        pyautogui.doubleClick()
        pyautogui.doubleClick()
        pyautogui.doubleClick()
        pyautogui.moveTo(550, 550)
        pyautogui.click()
        pyautogui.write('Olá! Em ' + str(int(elapsed_time)) + " seconds", interval=0.25)
        pyautogui.moveTo(1070, 740)
        pyautogui.doubleClick()
        pyautogui.doubleClick()
        pyautogui.moveTo(500, 670)
        pyautogui.click()
