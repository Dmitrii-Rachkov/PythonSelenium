"""ЗАПОЛНЯЕМ ПОЛЯ ФОРМЫ С ПОМОЩЬЮ КОДА"""

# Каждый элемент (текст, поле, кнопка, картинка) на веб-странице имеет локатор,
# т.е. то имя, тот адрес по которому мы можем к нему обратиться
# Чтобы узнать это имя нужно открыть DevTools на веб-сайте
# Мы можем нажать на стрелочку тем самым начать поиск элементов.
# Т.е. мы водим указателем по экрану и ищем элементы.
# На вкладке 'elements' мы можем увидеть тег 'input' у нашего поля 'Username', этот тег говорит о том
# что мы можем сюда вводить данные
# Разработчики должны позаботиться о том, чтобы в разметке html были нормальные локаторы


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
service_obj = Service('D:\\Projects\\PythonSelenium\\chromedriver.exe')
driver = webdriver.Chrome(service=service_obj)
driver.get('https://www.saucedemo.com/')
driver.maximize_window()
# Создадим переменную для нашего поля ввода 'Username'
# user_name = driver.find_element_by_id("user-name")
# Данный метод 'find_element_by_id()' - устарел, но на проектах старых он может попасться вам
# user_name = driver.find_element_by_id("user-name")
# чтобы код ниже заработал нужно ещё импортировать пакет
from selenium.webdriver.common.by import By
user_name = driver.find_element(By.ID, "user-name")
user_name.send_keys("standard_user")



# time.sleep(15)
# driver.close()

