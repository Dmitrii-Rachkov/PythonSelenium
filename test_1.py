from selenium import webdriver
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

# Считываем слово 'PRODUCTS' на странице
text_products = driver.find_element(By.XPATH, "//span[@class='title']")

# Метод 'text' считывает значение нашего локатора и присваивает его нашей переменной
value_text_products = text_products.text
print(value_text_products)

# Сделаем проверку что на главной странице после регистрации есть слово 'PRODUCTS'
# Если значение не совпадает, то мы получим ошибку
assert value_text_products == "PRODUCTS"
print("GOOD")

# Проверка с помощью сравнения переходов по URL
# URL более стабильный и неизменчивый при разработке сайта
url_main_page = "https://www.saucedemo.com/inventory.html"
# сохраняем значение url на котором мы находимся
get_url = driver.current_url
print(get_url)
assert url_main_page == get_url
print("URL is good")
