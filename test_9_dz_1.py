import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

"""АВТОРИЗАЦИЯ"""

# Заходим на тестовый сайт
service_obj = Service("D:\\Projects\\PythonSelenium\\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
base_url = "https://www.saucedemo.com/"
driver.get(base_url)
driver.maximize_window()

# Авторизовываемся на сайте
standart_user = "standard_user"
standart_password = "secret_sauce"

user = driver.find_element(By.XPATH, "//input[@id='user-name']")
user.send_keys(standart_user)
print("Input Login")

password = driver.find_element(By.XPATH, "//input[@id='password']")
password.send_keys(standart_password)
print("Input Password")

login_button = driver.find_element(By.XPATH, "//input[@id='login-button']")
login_button.click()
print("Click Login button")

"""ИНФОРМАЦИЯ О ПЕРВОМ ТОВАРЕ"""

# Считываем название продукта 1
bike_light = driver.find_element(By.XPATH, "//a[@id='item_0_title_link']")
name_bike_light = bike_light.text
print(name_bike_light)

# Считываем цену продукта 1
price_bike_light = driver.find_element(By.XPATH, "//*[@id='inventory_container']/div/div[2]/div[2]/div[2]/div")
v_price_bike_light = price_bike_light.text
print(v_price_bike_light)

"""ИНФОРМАЦИЯ О ВТОРОМ ТОВАРЕ"""
# Считываем название продукта 2
jacket = driver.find_element(By.XPATH, "//a[@id='item_5_title_link']")
name_jacket = jacket.text
print(name_jacket)

# Считываем цену продукта 2
price_jacket = driver.find_element(By.XPATH, "//*[@id='inventory_container']/div/div[4]/div[2]/div[2]/div")
v_price_jacket = price_jacket.text
print(v_price_jacket)

"""ДОБАВЛЯЕМ ДВА ТОВАРА В КОРЗИНУ"""
# Добавляем первый товар
add_bike_light = driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-bike-light']")
add_bike_light.click()
print("Add Bike Light to CART")

# Добавляем второй товар
add_jacket = driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-fleece-jacket']")
add_jacket.click()
print("Add Jacket to CART")

"""ПЕРЕХОДИМ В КОРЗИНУ"""
cart = driver.find_element(By.XPATH, "//a[@class='shopping_cart_link']")
cart.click()
print("Click move to CART")

"""НАЖИМАЕМ КНОПКУ CHECKOUT"""
checkout = driver.find_element(By.XPATH, "//button[@id='checkout']")
checkout.click()
print("Click Checkout")

"""ЗАПОЛНЯЕМ ИНФОРМАЦИЮ ДЛЯ ОПЛАТЫ И ПЕРЕХОДИМ ДАЛЬШЕ"""
first_name = driver.find_element(By.XPATH, "//input[@id='first-name']")
first_name.send_keys("Abra")

last_name = driver.find_element(By.XPATH, "//input[@id='last-name']")
last_name.send_keys("Kadabra")

zip = driver.find_element(By.XPATH, "//input[@id='postal-code']")
zip.send_keys("12345")

continue_button = driver.find_element(By.XPATH, "//input[@id='continue']")
continue_button.click()
print("Information for buy")

"""ПРОВЕРЯЕМ ЧТО НАЗВАНИЕ ТОВАРОВ И ЦЕНЫ СОВПАДАЮТ С ГЛАВНОЙ СТРАНИЦЕЙ"""
# Проверяем для товара 1
cart_bike_light = driver.find_element(By.XPATH, "//a[@id='item_0_title_link']")
v_cart_bike_light = cart_bike_light.text
assert name_bike_light == v_cart_bike_light
print("Assert name Bike Light")

cart_price_bike_light = driver.find_element(By.XPATH, "//*[@id='checkout_summary_container']/div/div[1]/div[3]/div[2]/div[2]/div")
v_cart_price_bike_light = cart_price_bike_light.text
assert v_price_bike_light == v_cart_price_bike_light
print("Assert price Bike Light")

# Проверяем для товара 2
cart_jacket = driver.find_element(By.XPATH, "//a[@id='item_5_title_link']")
v_cart_jacket = cart_jacket.text
assert name_jacket == v_cart_jacket
print("Assert name Jacket")

cart_price_jacket = driver.find_element(By.XPATH, "//*[@id='checkout_summary_container']/div/div[1]/div[4]/div[2]/div[2]/div")
v_cart_price_jacket = cart_price_jacket.text
assert v_price_jacket == v_cart_price_jacket
print("Assert price Jacket")

"""ПРОВЕРЯЕМ ИТОГОВУЮ ЦЕНУ ТОВАРОВ"""
# Преобразовываем цену товара 1 в число с плавающей точкой
price_1 = float(v_price_bike_light.lstrip("$"))
print(price_1)

# Преобразовываем цену товара 2 в чсило с плавающей точкой
price_2 = float(v_price_jacket.lstrip("$"))
print(price_2)

# Считываем итоговую сумму с страницы и преобразовываем в float с округлением
total = driver.find_element(By.XPATH, "//*[@id='checkout_summary_container']/div/div[2]/div[5]")
total_price = total.text
main_price = round(float(total_price.lstrip("Item total: $")), 2)
print(main_price)

# Складываем товар 1 с товаром 2 и сравниваем с итоговой суммой
initial_price = round((price_1 + price_2), 2)
print(initial_price)

assert initial_price == main_price
print("Assert TOTAL")




