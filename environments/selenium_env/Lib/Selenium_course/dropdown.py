from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

link = "http://suninjuly.github.io/selects1.html"


def calc():
    x_element = browser.find_element_by_id("num1")
    x = x_element.text
    y_element = browser.find_element_by_id("num2")
    y = y_element.text
    return (str(int(x) + int(y)))


try:
    browser = webdriver.Chrome()
    browser.get(link)
    s = calc()
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(s)
    submit = browser.find_element_by_css_selector('button').click()

finally:
    # успеваем скопировать код за 10 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
