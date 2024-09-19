from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
import pyautogui

driver = webdriver.Firefox()

driver.get('https://mauer.2cloud.com.br/ERP360/Login.aspx')

sleep(10)

login = driver.find_element(By.ID, "ContentPlaceHolder1_txtLogin")
senha = driver.find_element(By.ID, "ContentPlaceHolder1_txtSenha")
botao = driver.find_element(By.ID, "ContentPlaceHolder1_btnLogin")

login.send_keys("mauer.PauloAlexandre")
senha.send_keys("ElevorPaulo2024@")
sleep(0.2)
botao.click()

sleep(5)

driver.maximize_window()

pyautogui.moveTo(2, 500)

sleep(1)

barra_lateral = driver.find_element(By.ID, "ContentPlaceHolder1_asideMasterPage")
# fixar_menu = driver.find_element(By.XPATH, "//*[contains(@class, 'fa') and contains(@class, 'fa-bars')]")

# fixar_menu.click()

botao_financeiro = driver.find_element(By.CSS_SELECTOR, "em.far.fa-money-bill-alt")
botao_financeiro.find_element(By.XPATH, "..").click()

# botao_financeiro.click()

# driver.quit()