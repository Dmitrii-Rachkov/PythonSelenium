import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys

service_obj = Service('D:\\Projects\\PythonSelenium\\chromedriver.exe')
driver = webdriver.Chrome(service=service_obj)
base_url = 'https://www.saucedemo.com/' # наш сайт поместим в переменную и будем использовать её дальше
driver.get(base_url)
driver.maximize_window()

# Создаём переменные для логина и пароля
login_standard_user = "standard_user"
password_all = "secret_sauce"

user_name = driver.find_element(By.XPATH, "//input[@id='user-name']")
user_name.send_keys(login_standard_user)
print("Input Login")

# Удалим одну букву с помощью кнопки 'backspace' на клавиатуре:
# Для этого нужно импортировать пакет Keys из селениума
time.sleep(5) # сделаем паузу для наглядности
user_name.send_keys(Keys.BACKSPACE)
time.sleep(3)
user_name.send_keys(Keys.BACKSPACE) # удалим ещё символ
time.sleep(3)
user_name.send_keys("er") # возвращаем обратно всё как было
time.sleep(3)
user_name.send_keys(Keys.BACKSPACE * 3) # имитирует 3 нажатия 'backspace'
time.sleep(3)
user_name.send_keys("ser")

password = driver.find_element(By.XPATH, "//input[@id='password']")
password.send_keys(password_all)
print("Input Password")

# Нажамаем на клавиатуре как будто 'Enter' с помощью команды 'Return' или 'Enter'
password.send_keys(Keys.RETURN)

# Тестируем дроп-даун с фильтром на странице
filter_main = driver.find_element(By.XPATH, "//select[@class='product_sort_container']")
filter_main.click()
print("Filter click")
time.sleep(5)
filter_main.send_keys(Keys.DOWN * 2) # спускаемся в дроп-даун на две позиции ниже как бы стрелками
time.sleep(3)
filter_main.send_keys(Keys.UP) # На одну позицию вверх
time.sleep(3)
filter_main.send_keys(Keys.RETURN)

# также можно выбрать конкретное значение в дроп-дауне
time.sleep(3)
filter_main = driver.find_element(By.XPATH, "//select[@class='product_sort_container']")
filter_main.click()
time.sleep(3)
price = driver.find_element(By.XPATH, "//option[@value='hilo']")
price.click()
print("Price")



