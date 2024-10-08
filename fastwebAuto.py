import pyautogui
import time
from datetime import datetime

pyautogui.FAILSAFE = False

screenWidth, screenHeight = pyautogui.size()

while True:
    pyautogui.click(screenWidth - 2, screenHeight - 2)
    pyautogui.click(screenWidth - 2, 2)
    pyautogui.doubleClick(115, 238)

    time.sleep(10)
    pyautogui.click(1122, 116)
    
    agora = datetime.now()
    data_hora_formatada = agora.strftime("%H:%M:%S - %d/%m/%Y")
    print(f"Última execução: {data_hora_formatada}")
    
    time.sleep(280)
    pyautogui.click(screenWidth - 20, 3)
    
    time.sleep(10)
