"""Double click and Right click by mouse"""

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service('D:\\Projects\\PythonSelenium\\chromedriver.exe')
driver = webdriver.Chrome(service=service_obj)
base_url = 'https://demoqa.com/buttons'
driver.get(base_url)
driver.maximize_window()

# Найдём кнопку двойного клика
action = ActionChains(driver)
# Выделив ActionChains и зажав ctrl мы можем увидеть все функции этого класса
double_click = driver.find_element(By.XPATH, "//button[@id='doubleClickBtn']")
action.double_click(double_click).perform()
# Метод perform() необходим чтобы мы сохранили результат

# Проверим текст после двойного нажатия
expected_double = "You have done a double click"
actual_double_locator = driver.find_element(By.XPATH, "//p[@id='doubleClickMessage']")
actual_double_text = actual_double_locator.text
assert expected_double == actual_double_text
print("Double click is GOOD")

# Найдём и нажмём правой кнопкой мыши
right_mouse = driver.find_element(By.XPATH, "//button[@id='rightClickBtn']")
action.context_click(right_mouse).perform()

# Проверим текст после нажатия правой кнопкой мыши
expected_right = "You have done a right click"
right_locator = driver.find_element(By.XPATH, "//p[@id='rightClickMessage']")
actual_right = right_locator.text
assert expected_right == actual_right
print("Right mouse is WORK")



