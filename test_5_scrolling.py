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

# Дальше мы скролим страницу вниз с помощью ползунка
# driver.execute_script("window.scrollTo(X, Y)") # X - по горизонтали, Y - по вертикали в пикселях
driver.execute_script("window.scrollTo(0, 0)") # Значит мы в левом верхнем углу

# Скролинг нам нужен например если наш элемент находится внизу, и даже если мы напишем локатор
# то браузер не сможет его найти так как он внизу и его не видно
# Также можно скролить если вам нужны скриншоты всей страницы, а не одной её части
time.sleep(3)
driver.save_screenshot('.\\screen\\' + "Screenshot" + datetime.datetime.utcnow().strftime("%Y.%m.%d.%H.%M.%S") + ".png")
driver.execute_script("window.scrollTo(0, 400)")
time.sleep(3)
driver.save_screenshot('.\\screen\\' + "Screenshot" + datetime.datetime.utcnow().strftime("%Y.%m.%d.%H.%M.%S") + ".png")

# Мы с вами не знаем разрешение экрана сервере и разрешения экрана пользователя и размер экрана
# Мы не знаем сколько нам скролить до нужного нам элемента
time.sleep(2)
driver.execute_script("window.scrollTo(0, 0)") # в исходное положение, только открыли страницу
time.sleep(2)
action = ActionChains(driver) # показываем системе что хотим управлять нашим драйвером
red_footbolka = driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-onesie']")
action.move_to_element(red_footbolka).perform() # перемещаемся к этому элементу
time.sleep(2)
driver.save_screenshot('.\\screen\\' + "Screenshot" + datetime.datetime.utcnow().strftime("%Y.%m.%d.%H.%M.%S") + ".png")








