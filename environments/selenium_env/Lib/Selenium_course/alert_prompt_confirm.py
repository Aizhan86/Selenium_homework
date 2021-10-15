from selenium import webdriver
import time
import math
link = "http://suninjuly.github.io/alert_accept.html"


def calc():

    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)
    submit1 = browser.find_element_by_css_selector('button').click()
    alert = browser.switch_to.alert
    alert.accept()
    y = calc()
    input = browser.find_element_by_id("answer").send_keys(y)
    submit2 = browser.find_element_by_css_selector('button').click()

finally:
    # успеваем скопировать код за 20 секунд
    time.sleep(20)
    # закрываем браузер после всех манипуляций
    browser.quit()