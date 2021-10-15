from selenium import webdriver
import time
import math

try:

    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/find_link_text")

    str(math.ceil(math.pow(math.pi, math.e)*10000))

    input1 = browser.find_element_by_tag_name("input").send_keys("Ivan")
    input2 = browser.find_element_by_name("last_name").send_keys("Petrov")
    input3 = browser.find_element_by_class_name("city").send_keys("Smolensk")
    input4 = browser.find_element_by_id("country").send_keys("Russia")
    button = browser.find_element_by_css_selector("button.btn").click()

finally:
    time.sleep(30)
    browser.quit()
