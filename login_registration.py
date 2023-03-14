import time
from selenium import webdriver
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("https://practice.automationtesting.in/")
my_account = driver.find_element_by_id("menu-item-50")
my_account.click()
email = driver.find_element_by_name("email")
email.send_keys("ilka.ilkoy@gmail.com")
password = driver.find_element_by_id("reg_password")
password.send_keys("fG|pGFj$#9")
register_btn = driver.find_element_by_name("register")
register_btn.click()
driver.quit()

# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.implicitly_wait(5)
# driver.get("https://practice.automationtesting.in/")
# my_account = driver.find_element_by_id("menu-item-50")
# my_account.click()
# email = driver.find_element_by_name("username")
# email.send_keys("ilka.ilkoy@gmail.com")
# password = driver.find_element_by_id("password")
# password.send_keys("fG|pGFj$#9")
# login_btn = driver.find_element_by_name("login")
# login_btn.click()
# logout_btn = WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.LINK_TEXT, "Logout"), "Logout"))
# driver.quit()