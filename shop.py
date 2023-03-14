import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("https://practice.automationtesting.in/")
my_account = driver.find_element_by_id("menu-item-50")
my_account.click()
email = driver.find_element_by_name("username")
email.send_keys("ilka.ilkoy@gmail.com")
password = driver.find_element_by_id("password")
password.send_keys("fG|pGFj$#9")
login_btn = driver.find_element_by_name("login")
login_btn.click()
shop = driver.find_element_by_id("menu-item-40")
shop.click()
book = driver.find_element_by_css_selector(".post-181 > a")
book.click()
book_name = WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.TAG_NAME, "h1"), "HTML5 Forms"))
driver.quit()
#
#
# import time
# from selenium import webdriver
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
# shop = driver.find_element_by_id("menu-item-40")
# shop.click()
# HTML = driver.find_element_by_css_selector(".cat-item-19 > a")
# HTML.click()
# items_count = driver.find_elements_by_css_selector("a.woocommerce-LoopProduct-link")
# if len(items_count) == 3:
#     print("Отображается 3 товара")
# else:
#     print("Ошибка. Количество товаров: " + str(len(items_count)))
# driver.quit()
#
#
# import time
# from selenium import webdriver
# from selenium.webdriver.support.select import Select
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
# shop = driver.find_element_by_id("menu-item-40")
# shop.click()
# default = driver.find_element_by_css_selector(".orderby > option:nth-child(1)")
# default_select = default.get_attribute("selected")
# print("selected: ", default_select)
# sorting = driver.find_element_by_class_name("orderby")
# select = Select(sorting)
# select.select_by_value("price-desc")
# default_new = driver.find_element_by_css_selector(".orderby > option:nth-child(6)")
# default_new_select = default_new.get_attribute("selected")
# print("selected: ", default_select)
# driver.quit()
#
#
# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.implicitly_wait(5)
# wait = WebDriverWait(driver, 5)
# driver.get("https://practice.automationtesting.in/")
# my_account = driver.find_element_by_id("menu-item-50")
# my_account.click()
# email = driver.find_element_by_name("username")
# email.send_keys("ilka.ilkoy@gmail.com")
# password = driver.find_element_by_id("password")
# password.send_keys("fG|pGFj$#9")
# login_btn = driver.find_element_by_name("login")
# login_btn.click()
# shop = driver.find_element_by_id("menu-item-40")
# shop.click()
# book = driver.find_element_by_css_selector(".post-169 > a")
# book.click()
# book_old_price = driver.find_element_by_css_selector(".price > del > span")
# book_old_price_text = book_old_price.text
# assert book_old_price_text == "₹600.00"
# book_new_price = driver.find_element_by_css_selector(".price > ins > span")
# book_new_price_text = book_new_price.text
# assert book_new_price_text == "₹450.00"
# image = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "images")) )
# image.click()
# close = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "pp_close")) )
# close.click()
# driver.quit()
#
#
# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.implicitly_wait(5)
# wait = WebDriverWait(driver, 5)
# driver.get("https://practice.automationtesting.in/")
# my_account = driver.find_element_by_id("menu-item-50")
# my_account.click()
# email = driver.find_element_by_name("username")
# email.send_keys("ilka.ilkoy@gmail.com")
# password = driver.find_element_by_id("password")
# password.send_keys("fG|pGFj$#9")
# login_btn = driver.find_element_by_name("login")
# login_btn.click()
# shop = driver.find_element_by_id("menu-item-40")
# shop.click()
# driver.execute_script("window.scrollBy(0, 1100);")
# book = driver.find_element_by_css_selector(".post-165 > a:nth-child(2)")
# book.click()
# time.sleep(5)
# basket = driver.find_element_by_class_name("cartcontents")
# basket_count = basket.text
# assert "1 Item" in basket_count
# amount = driver.find_element_by_css_selector("#wpmenucartli > a > .amount")
# amount_count = amount.text
# assert "350.00" in amount_count
# basket.click()
# subtotal = wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".cart-subtotal > td > span"), "350.00"))
# total = wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".order-total > td > strong > span"), "357.00"))
# driver.quit()
#
#
# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.implicitly_wait(5)
# wait = WebDriverWait(driver, 5)
# driver.get("https://practice.automationtesting.in/")
# shop = driver.find_element_by_id("menu-item-40")
# shop.click()
# time.sleep(5)
# driver.execute_script("window.scrollBy(0, 1100);")
# book = driver.find_element_by_css_selector(".post-165 > a:nth-child(2)")
# book.click()
# time.sleep(5)
# basket = driver.find_element_by_class_name("wpmenucart-contents")
# basket.click()
# driver.execute_script("window.scrollBy(0, 300);")
# checkout = wait.until(EC.element_to_be_clickable((By.CLASS_NAME,"wc-forward")))
# checkout.click()
# first_name = wait.until(EC.element_to_be_clickable((By.ID,"billing_first_name")))
# first_name.send_keys("Ella")
# last_name = driver.find_element_by_id("billing_last_name")
# last_name.send_keys("Joy")
# email = driver.find_element_by_id("billing_email")
# email.send_keys("ilka.ilkoy@gmail.com")
# phone = driver.find_element_by_id("billing_phone")
# phone.send_keys("+9937163813")
# address = driver.find_element_by_id("billing_address_1")
# address.send_keys("First Street")
# town = driver.find_element_by_id("billing_city")
# town.send_keys("Mumbai")
# postcode = driver.find_element_by_id("billing_postcode")
# postcode.send_keys("123456")
# driver.execute_script("window.scrollBy(0, 900);")
# time.sleep(5)
# payment = driver.find_element_by_css_selector("[value='cheque']")
# payment.click()
# order = driver.find_element_by_id("place_order")
# order.click()
# thank_you = wait.until(EC.text_to_be_present_in_element((By.CLASS_NAME, "woocommerce-thankyou-order-received"), "Thank you. Your order has been received."))
# check_payment = wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".shop_table.order_details > tfoot > tr:nth-child(3) > td"), "Check Payments"))
# driver.quit()
