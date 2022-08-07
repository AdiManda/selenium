# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring

from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

# initializare browser
s = Service(ChromeDriverManager().install())
chrome = webdriver.Chrome(service=s)

chrome.maximize_window()  # deschide browser chrome

chrome.get("https://formy-project.herokuapp.com/form")  # deschide pagina din paranteza
# chrome.quit()
first_name = chrome.find_element(By.ID, "first-name")
first_name.send_keys("Eido")
last_name = chrome.find_element(By.ID, "last-name")
last_name.send_keys("crowley")
sleep(3)
chrome.quit()