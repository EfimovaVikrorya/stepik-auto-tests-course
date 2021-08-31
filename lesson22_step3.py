from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

try:
    link = "http://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome()
    browser.get(link)

# Посчитать сумму заданных чисел
    x_element = browser.find_element_by_id("num1")
    y_element = browser.find_element_by_id("num2")
    x = int(x_element.text)
    y = int(y_element.text) 
    z= str(x + y)


    select = Select(browser.find_element_by_id("dropdown"))
    select.select_by_value(z) # ищем элемент со значением z
 
    button = browser.find_element_by_class_name("btn")
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()