from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By

service_obj = Service('D:\\Projects\\PythonSelenium\\chromedriver.exe')
driver = webdriver.Chrome(service=service_obj)
driver.get('https://www.saucedemo.com/')
driver.maximize_window()
# user_name = driver.find_element(By.ID, "user-name") # ID
# user_name = driver.find_element(By.NAME, "user-name") # NAME
# user_name = driver.find_element(By.XPATH, "//*[@id='user-name']") #  FULL XPATH
# user_name = driver.find_element(By.XPATH, "//input[@id='user-name']") #  надёжный вариант XPATH ID
user_name = driver.find_element(By.XPATH, "//input[@placeholder='Username']") #  надёжный вариант 2 XPATH placeholder
user_name.send_keys("standard_user")

# Помимо 'id' мы можем обращаться к элементам на веб странице и по-другому:
# id, name, class_name, xpath, link_text, tag_name, css_selector
# Прежде всего это зависит от того, какую страницу мы имеем в плане HTML кода,
# т.е. какая у нас разметка страницы

# Мы можем обратиться к любому атрибуту элемента на странице
# Если нам не хватает встроенных функции для поиска локаторов, то мы можем воспользоваться XPATH
# Для этого в DevTools нужно навести на локатор и нажать правой кнопкой мыши и скопировать (не full) XPATH
# Второй способ когда мы ищем элемент по первому тегу получается и вручную вводим путь до него
# этот способ более надёжный

# Введём пароль в форму с помощью 'css_selector'
password = driver.find_element(By.CSS_SELECTOR, "#password") # CSS_SELECTOR
# Чтобы узнать 'css_selector' элемента нужно нажать по нему правой кнопкой мыши и скопировать selector
password.send_keys("secret_sauce")

# Жмём на кнопку 'login'
button_login = driver.find_element(By.XPATH, "//input[@id='login-button']")
button_login.click()

