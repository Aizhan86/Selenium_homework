from selenium import webdriver
import time
import math
link = "http://SunInJuly.github.io/execute_script.html"


def calc():

    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element_by_tag_name("button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()
    y = calc()

    input = browser.find_element_by_id("answer").send_keys(y)

    option1 = browser.find_element_by_id("robotCheckbox").click()
    option2 = browser.find_element_by_css_selector("[for='robotsRule']").click()
    submit = browser.find_element_by_css_selector('button').click()

finally:
    # успеваем скопировать код за 20 секунд
    time.sleep(100)
    # закрываем браузер после всех манипуляций
    browser.quit()