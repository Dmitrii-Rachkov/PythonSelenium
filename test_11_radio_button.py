"""Radio Button"""

# В этом элементе мы можем выбрать только одно значение

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service('D:\\Projects\\PythonSelenium\\chromedriver.exe')
driver = webdriver.Chrome(service=service_obj)
base_url = 'https://demoqa.com/radio-button'
driver.get(base_url)
driver.maximize_window()

# Ищем наш radio button на сайте
radio_button = driver.find_element(By.XPATH, "//label[@for='yesRadio']")
radio_button.click()

expected_text = "You have selected Yes"
actual_text = driver.find_element(By.XPATH, "//p[@class='mt-3']").text
assert expected_text == actual_text
print("Radio Button is GOOD")
