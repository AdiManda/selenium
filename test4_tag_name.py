# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring

from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

s = Service(ChromeDriverManager().install())
chrome = webdriver.Chrome(service=s)

chrome.maximize_window()  # deschide browser chrome

chrome.get("https://formy-project.herokuapp.com/form")  # deschide pagina din paranteza

lista_elemente_input = chrome.find_elements(By.TAG_NAME, "input")
lista_elemente_input[2].send_keys("qa")
sleep(3)
chrome.quit()
