import time
from selenium import webdriver
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://practice.automationtesting.in/")
driver.execute_script("window.scrollBy(0, 600);")
Selenium_Ruby = driver.find_element_by_css_selector(".post-160 > a > img")
Selenium_Ruby.click()
time.sleep(5)
driver.execute_script("window.scrollBy(0, 700);")
reviews = driver.find_element_by_class_name("reviews_tab")
reviews.click()
star_5 = driver.find_element_by_class_name("star-5")
star_5.click()
driver.execute_script("window.scrollBy(0, 200);")
comment = driver.find_element_by_id("comment")
comment.send_keys("Nice book!")
name = driver.find_element_by_id("author")
name.send_keys("Maria")
email = driver.find_element_by_id("email")
email.send_keys("test@mail.com")
submit_btn = driver.find_element_by_class_name("submit")
submit_btn.click()
driver.quit()