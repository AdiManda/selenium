# Alegeti-va unu sau mai multe din sugestiile de site-uri de mai jos
# https://www.phptravels.net/
# http://automationpractice.com/index.php
# https://formy-project.herokuapp.com/
# https://the-internet.herokuapp.com/
# https://www.techlistic.com/p/selenium-practice-form.html
# jules.app

# Alegeti cate 3 elemente din fiecare tip de selector din urmatoarele categorii:

# Id
# Link text
# Partial link text
# Name
# Tag*
# Class name*

# Probabil nu veti gasi un singur website care sa cuprinda toate variantele de mai sus, astfel ca va recomandam sa folositi mai multe site-uri
# Optional: La tag si class name veti folosi find elementS! - salvati in lista. Interactionati cu un element la alegere din lista

# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


s = Service(ChromeDriverManager().install())
chrome = webdriver.Chrome(service=s)

chrome.maximize_window()
chrome.get("https://formy-project.herokuapp.com/form")
first_name = chrome.find_element(By.ID, "first-name")
first_name.send_keys("Eido")
last_name = chrome.find_element(By.ID, "last-name")
last_name.send_keys("Crowley")
sleep(3)

chrome.maximize_window()
chrome.get("https://formy-project.herokuapp.com")
chrome.find_element(By.PARTIAL_LINK_TEXT, "File Upload").click()
sleep(3)

chrome.maximize_window()
chrome.get("https://formy-project.herokuapp.com")
chrome.find_element(By.PARTIAL_LINK_TEXT, "Buttons").click()
# sleep(3)

chrome.maximize_window()
chrome.get("http://www.seleniumframework.com/Practiceform/")
chrome.find_element(By.NAME, "name").send_keys("Eido")
sleep(3)

chrome.maximize_window()
chrome.get("http://www.seleniumframework.com/Practiceform/")
chrome.find_element(By.NAME, "telephone").send_keys("07xxxxxxx")
sleep(3)

chrome.maximize_window()
chrome.get("https://formy-project.herokuapp.com/autocomplete")
chrome.lista_input = chrome.find_elements(By.TAG_NAME, "input")
chrome.lista_input[0].send_keys('adresa')
chrome.lista_input[1].send_keys('strada')
sleep(1)

chrome.maximize_window()
chrome.get("https://formy-project.herokuapp.com/dropdown")
chrome.find_element(By.CLASS_NAME, "navbar-brand").click()
sleep(3)

chrome.maximize_window()
chrome.get("https://formy-project.herokuapp.com/dropdown")
chrome.find_element(By.CLASS_NAME, "dropdown").click()
sleep(3)
