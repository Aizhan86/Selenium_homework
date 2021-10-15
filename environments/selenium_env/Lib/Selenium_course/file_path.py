from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_css_selector("[name='firstname']").send_keys("Ivan")
    input2 = browser.find_element_by_css_selector("[name='lastname']").send_keys("Ivanov")
    input3 = browser.find_element_by_css_selector("[name='email']").send_keys("Ivanov@mail.ru")
    current_dir = os.path.abspath(os.path.dirname('__/C:/Users/Aizhan.Orynbayeva/PycharmProjects/pythonProject3/environments/selenium_env/Lib/Selenium_course/__'))
    file_path = os.path.join(current_dir, "file_example.txt")
    element = browser.find_element(By.CSS_SELECTOR, "[type='file']").send_keys(file_path)
    submit = browser.find_element_by_css_selector('button').click()

finally:
    # успеваем скопировать код за 20 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
