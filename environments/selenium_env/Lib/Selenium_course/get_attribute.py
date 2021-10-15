from selenium import webdriver
import time
import math
link = "http://suninjuly.github.io/get_attribute.html"


def calc():

    x_element = browser.find_element_by_id("treasure")
    x = x_element.get_attribute('valuex')
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)
    y = calc()
    element = browser.find_element_by_css_selector('input[required]').send_keys(y)
    option1 = browser.find_element_by_css_selector("[type='checkbox']").click()
    option2 = browser.find_element_by_css_selector("[value='robots']").click()
    submit = browser.find_element_by_css_selector("button").click()

finally:
    # успеваем скопировать код за 20 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()