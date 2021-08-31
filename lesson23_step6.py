from selenium import webdriver
import time
import math

try: 
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
# нажать на кнопку
    button = browser.find_element_by_class_name("btn-primary")
    button.click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

# На новой странице решить капчу для роботов, чтобы получить число с ответом
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
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()