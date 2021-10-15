import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
browser = webdriver.Chrome()

link = "http://suninjuly.github.io/selects1.html"
link2 = "http://suninjuly.github.io/selects2.html"
try:
    browser.get(link)
    val = спойлер спрятан
    browser.find_element_by_tag_name("select").click()
    browser.find_element_by_*спойлер спрятан*.click()
    browser.find_element_by_tag_name("button").click()
    time.sleep(3)

    browser.get(link2)
    val = *спойлер спрятан*
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_visible_text(*спойлер спрятан*)
    browser.find_element_by_tag_name("button").click()
finally:
    time.sleep(10)
    browser.quit()