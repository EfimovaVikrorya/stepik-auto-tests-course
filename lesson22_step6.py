from selenium import webdriver
import time
import math


try: 
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

# функция для вычисления математического выражения
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

# подставляем его в х

    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)
    y_element = browser.find_element_by_id("answer")
    y_element.send_keys(y)

    button = browser.find_element_by_tag_name("button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

# Отметить checkbox "I'm the robot"
    option1 = browser.find_element_by_id("robotCheckbox")
    option1.click()

# Выбрать radiobutton "Robots rule!"
    option2 = browser.find_element_by_id("robotsRule")
    option2.click()

# Отправляем заполненную форму
    button = browser.find_element_by_class_name("btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)



finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()