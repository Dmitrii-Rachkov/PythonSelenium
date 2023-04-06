import datetime
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys, ActionChains

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

password = driver.find_element(By.XPATH, "//input[@id='password']")
password.send_keys(password_all)
print("Input Password")

password.send_keys(Keys.RETURN)
print("Click login button")

# Есть у нас в кнопке меню скрытые элементы которые в DevTools видны только после нажатия кнопки меню
menu_button = driver.find_element(By.XPATH, "//button[@id='react-burger-menu-btn']")
menu_button.click()
print("Menu click")
time.sleep(3)
about_button = driver.find_element(By.XPATH, "//a[@id='about_sidebar_link']")
about_button.click()
print("About click")

url_about = "https://saucelabs.com/"
get_url = driver.current_url
assert get_url == url_about
print(" YES")

now_date = datetime.datetime.utcnow().strftime("%Y.%m.%d.%H.%M.%S")
test_screen = driver.save_screenshot(".\\screen\\" + "test_7" + now_date + ".png")
time.sleep(3)

# Команда для перемещения назад и вперёд в браузере (стрелки в левом углу)
driver.back() # Назад
print("Back page")
time.sleep(3)
driver.forward() # Вперёд
print("Forward")








