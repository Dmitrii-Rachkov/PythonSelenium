from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

"""Приветствуем пользователя, рассказываем о товарах и сохраняем выбранный товар в переменную"""
print("Приветствую тебя в нашем интернет магазине")
print("\nВыбери один из следующих товаров и укажи его номер:"
      "\n1 - Sauce Labs Bike Light"
      "\n2 - Sauce Labs Bolt T-Shirt"
      "\n3 - Sauce Labs Onesie"
      "\n4 - Test.allTheThings() T-Shirt (Red)"
      "\n5 - Sauce Labs Backpack"
      "\n6 - Sauce Labs Fleece Jacket")

# Вводим переменную чтобы сохранить в неё выбор пользователя и чтобы переменная была видна дальше в коде
goal_select = 0

# Проверяем, что вводятся целые числа от 1 до 6
try:
    select = int(input())
    if select < 1 or select > 6:
        print("Ошибка. Необходимо ввести целое число от 1 до 6. Перезапустите программу!")
    else:
        print(f'Вы выбрали продукт №{select}')
        goal_select = select
except ValueError:
    print("Ошибка. Необходимо ввести целое число от 1 до 6. Перезапустите программу!")
    quit()

"""Заходим на тестовый сайт и авторизовываемся"""
service_obj = Service('D:\\Projects\\PythonSelenium\\chromedriver.exe')
driver = webdriver.Chrome(service=service_obj)
base_url = "https://www.saucedemo.com/"
driver.get(base_url)
driver.maximize_window()
driver.implicitly_wait(10) # неявное ожидание на случай если сайт будет долго загружаться

# Авторизовываемся на сайте
standart_user = "standard_user"
standart_password = "secret_sauce"

user = driver.find_element(By.XPATH, "//input[@id='user-name']")
user.send_keys(standart_user)
print("Введён логин")

password = driver.find_element(By.XPATH, "//input[@id='password']")
password.send_keys(standart_password)
print("Введён пароль")

login_button = driver.find_element(By.XPATH, "//input[@id='login-button']")
login_button.click()
print("Нажимаем кнопку Login")

"""Считываем информацию о товаре"""
# Считываем название продукта
product = driver.find_element(By.XPATH, "//a[@id='item_" + str(goal_select - 1) + "_title_link']")
name_product = product.text
print(name_product)

# Считываем цену продукта выбирая нужный XPATH
match goal_select:
    case 1:
        price_xpath = "//*[@id='inventory_container']/div/div[2]/div[2]/div[2]/div"
    case 2:
        price_xpath = "//*[@id='inventory_container']/div/div[3]/div[2]/div[2]/div"
    case 3:
        price_xpath = "//*[@id='inventory_container']/div/div[5]/div[2]/div[2]/div"
    case 4:
        price_xpath = "//*[@id='inventory_container']/div/div[6]/div[2]/div[2]/div"
    case 5:
        price_xpath = "//*[@id='inventory_container']/div/div[1]/div[2]/div[2]/div"
    case 6:
        price_xpath = "//*[@id='inventory_container']/div/div[4]/div[2]/div[2]/div"

price = driver.find_element(By.XPATH, price_xpath)
value_price = price.text
print(f'Цена продукта = {value_price}')

"""Добавляем товар в корзину"""
match goal_select:
    case 1:
        id_cart = "//button[@id='add-to-cart-sauce-labs-bike-light']"
    case 2:
        id_cart = "//button[@id='add-to-cart-sauce-labs-bolt-t-shirt']"
    case 3:
        id_cart = "//button[@id='add-to-cart-sauce-labs-onesie']"
    case 4:
        id_cart = "//button[@id='add-to-cart-test.allthethings()-t-shirt-(red)']"
    case 5:
        id_cart = "//button[@id='add-to-cart-sauce-labs-backpack']"
    case 6:
        id_cart = "//button[@id='add-to-cart-sauce-labs-fleece-jacket']"

add_cart = driver.find_element(By.XPATH, id_cart)
add_cart.click()
print("Товар добавлен в корзину")

"""Переходим в корзину"""
cart = driver.find_element(By.XPATH, "//a[@class='shopping_cart_link']")
cart.click()
print("Переходим в корзину")

"""НАЖИМАЕМ КНОПКУ CHECKOUT"""
checkout = driver.find_element(By.XPATH, "//button[@id='checkout']")
checkout.click()
print("Нажимаем кнопку Checkout")

"""ЗАПОЛНЯЕМ ИНФОРМАЦИЮ ДЛЯ ОПЛАТЫ И ПЕРЕХОДИМ ДАЛЬШЕ"""
first_name = driver.find_element(By.XPATH, "//input[@id='first-name']")
first_name.send_keys("Abra")

last_name = driver.find_element(By.XPATH, "//input[@id='last-name']")
last_name.send_keys("Kadabra")

zip = driver.find_element(By.XPATH, "//input[@id='postal-code']")
zip.send_keys("12345")

continue_button = driver.find_element(By.XPATH, "//input[@id='continue']")
continue_button.click()
print("Информация о покупке")

"""Проверяем что название товара совпадает с изначальным выбором"""
cart_product = driver.find_element(By.XPATH, "//a[@id='item_" + str(goal_select - 1) + "_title_link']")
v_cart_product = cart_product.text
assert name_product == v_cart_product
print("Имя продукта верно")

"""Проверяем итоговую цену товара"""
# Преобразовываем цену товара в число с плавающей точкой
price_1 = float(value_price.lstrip("$"))
print(price_1)

# Считываем итоговую сумму с страницы и преобразовываем в float с округлением
total = driver.find_element(By.XPATH, "//*[@id='checkout_summary_container']/div/div[2]/div[5]")
total_price = total.text
main_price = round(float(total_price.lstrip("Item total: $")), 2)
print(main_price)

assert price_1 == main_price
print("Цена совпадает")

