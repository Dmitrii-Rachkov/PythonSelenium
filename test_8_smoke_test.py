from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

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

button_login = driver.find_element(By.XPATH, "//input[@id='login-button']")
button_login.click()
print("Click login button")

"""Info product 1"""
# Считываем название нашего продукта
product_1 = driver.find_element(By.XPATH, "//a[@id='item_4_title_link']")
value_product_1 = product_1.text
print(value_product_1)

# Считываем цену нашего продукта
price_1 = driver.find_element(By.XPATH, "//div[@class='inventory_item_price']")
price_1_value = price_1.text
print(price_1_value)

# Добавляем наш продукт в корзину
buy_product_1 = driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-backpack']")
buy_product_1.click()
print("Add to CART product 1")

# Корзина с товаром, открываем её
cart_1 = driver.find_element(By.XPATH, "//span[@class='shopping_cart_badge']")
cart_1.click()
print("Open shopping CART")

"""INFO cart product 1"""
name_cart_1 = driver.find_element(By.XPATH, "//div[@class='inventory_item_name']")
value_name_cart_1 = name_cart_1.text
print("Name product 1 in CART")
assert value_product_1 == value_name_cart_1
print("Assert text")

price_cart_1 = driver.find_element(By.XPATH, "//div[@class='inventory_item_price']")
value_price_cart_1 = price_cart_1.text
print("Price product 1 in CART")
assert price_1_value == value_price_cart_1
print("Assert price")

# Жмём на кнопку Checkout
checkout = driver.find_element(By.XPATH, "//button[@class='btn btn_action btn_medium checkout_button']")
checkout.click()
print("Click checkout")

"""Заполняем поля"""
first_name = driver.find_element(By.XPATH, "//input[@id='first-name']")
first_name.send_keys("Abra")
print("Frist Name")

last_name = driver.find_element(By.XPATH, "//input[@id='last-name']")
last_name.send_keys("Kadabra")
print("Last Name")

postal = driver.find_element(By.XPATH, "//input[@id='postal-code']")
postal.send_keys("12345")
print("Postal")

# Нажимаем кнопку continue
button_continue = driver.find_element(By.XPATH, "//input[@id='continue']")
button_continue.click()
print("Continue click")

"""Страница с подтверждением оплаты"""
checkout_product_1 = driver.find_element(By.XPATH, "//div[@class='inventory_item_name']")
checkout_product_1_value = checkout_product_1.text
assert value_product_1 == checkout_product_1_value
print("Assert Overview Name")

checkout_price_1 = driver.find_element(By.XPATH, "//div[@class='inventory_item_price']")
checkout_price_1_value = checkout_price_1.text
assert price_1_value == checkout_price_1_value
print("Assert Overview Price")

# Total сумма сравниваем с суммой на главной странице
action = ActionChains(driver)
total = driver.find_element(By.XPATH, "//div[@class='summary_subtotal_label']")
action.move_to_element(total).perform()
total_value = total.text
item_total = "Item total: " + price_1_value
assert item_total == total_value
print("Total Assert")
