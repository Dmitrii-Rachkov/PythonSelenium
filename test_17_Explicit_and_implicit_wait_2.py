"""Пример Явного Ожидания"""

# Явное ожидание - это ожидание когда мы явно прописываем не для всего нашего теста, а для
# каждого нашего локатора, для каждого элемента индивидуальное время ожидания

# Также мы можем устанавливать ожидание от какого-либо типа действия, например кликабл -
# это когда наш элемент доступен для нажатия

# Также мы можем искать по visible - это когда элемент присутствует не только в DOMe, но и
# виден на странице. Например когда баннер есть в DOMe, но ему нужно время на загрузку и отображение

# Нельзя одновременно использовать Неявное и Явное ожидание, потому что они могут противоречить
# друг другу и тесты будут падать

# Минус Явного ожидание в том, что это удленяет наш код, необходимо для каждого элемента писать
# строку с явным ожиданием

# Плюс то, что тесты более надёжны и стабильны, ведь здесь индивидуальный подход к каждому элементу

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service_obj = Service('D:\\Projects\\PythonSelenium\\chromedriver.exe')
driver = webdriver.Chrome(service=service_obj)
base_url = 'https://demoqa.com/dynamic-properties'
driver.get(base_url)
driver.maximize_window()

print("Start Test")

# Задаём нашей системе время в течении которого мы будем пытаться найти элемент,
# который будет кликабелен
visible_button = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//button[@id='visibleAfter']")))

visible_button.click()
print("Finish Test")


