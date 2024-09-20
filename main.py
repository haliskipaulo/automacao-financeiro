from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
import pyautogui

driver = webdriver.Firefox()

driver.get('https://mauer.2cloud.com.br/ERP360/Login.aspx')
driver.maximize_window()

sleep(1)

login = driver.find_element(By.ID, "ContentPlaceHolder1_txtLogin")
senha = driver.find_element(By.ID, "ContentPlaceHolder1_txtSenha")
botao = driver.find_element(By.ID, "ContentPlaceHolder1_btnLogin")

login.send_keys("mauer.PauloAlexandre")
senha.send_keys("ElevorPaulo2024@")
sleep(0.1)
botao.click()

sleep(5)

pyautogui.moveTo(2, 500)

sleep(1)

'''

botao_fixar_location = pyautogui.locateCenterOnScreen('botao_fixar.png', confidence=0.8)
pyautogui.click(botao_fixar_location)

botao_financeiro_location = pyautogui.locateCenterOnScreen('botao_financeiro.png', confidence=0.8)
sleep(0.2)
pyautogui.click(botao_financeiro_location)

botao_bancosCaixa_location = pyautogui.locateCenterOnScreen('botao-bancoscaixa.png', confidence=0.8)
sleep(0.2)
pyautogui.click(botao_bancosCaixa_location)

PYAUTOGUI FUNCIONANDO

'''

barra_lateral = driver.find_element(By.ID, "ContentPlaceHolder1_asideMasterPage")
fixar_menu  = driver.find_element(By.XPATH, "//aside[@id='ContentPlaceHolder1_asideMasterPage']//nav[@id='ContentPlaceHolder1_menuSidebar']//div[@class='profile-picture']//a[@class='fixed-sidebar float-right d-none d-md-inline']")

fixar_menu.click()

sleep(1)

botao_financeiro = driver.find_element(By.CLASS_NAME, "far fa-money-bill-alt")


# botao_financeiro.click()

# driver.quit()