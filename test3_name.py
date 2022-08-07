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

chrome.get("http://www.seleniumframework.com/Practiceform/")  # deschide pagina din paranteza

chrome.find_element(By.NAME, "country").send_keys("Romania")
chrome.find_element(By.NAME, "company").send_keys("ItFactory")
sleep(3)
chrome.quit()