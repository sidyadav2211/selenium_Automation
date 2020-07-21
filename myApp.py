from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://web.whatsapp.com//")
print("Scan Code")
input()
print("loged In")
time.sleep(12)
Search_box = driver.find_element_by_xpath("//*[@id='side']/div[1]/div/label/div/div[2]")

Search_box.send_keys("Ram Yadav ")
Search_box.send_keys(Keys.ENTER)
time.sleep(10)
msg_send = driver.find_element_by_xpath(
    "//*[@id='main']/footer/div[1]/div[2]/div/div[2]"
)


msg_send.send_keys("Hi Ram")

msg_send.send_keys(Keys.ENTER)
msg_send.send_keys("Bye")
msg_send.send_keys(Keys.ENTER)
time.sleep(2)
Search_box = driver.find_element_by_xpath("//*[@id='side']/div[1]/div/label/div/div[2]")

Search_box.send_keys("Raja")
Search_box.send_keys(Keys.ENTER)
time.sleep(10)
msg_box = driver.find_element_by_xpath(
    "//*[@id='main']/footer/div[1]/div[2]/div/div[2]"
)
msg_box.send_keys("Hi")
msg_box.send_keys(Keys.ENTER)
time.sleep(4)

scroll = driver.execute_script("window.scrollBy(0,1000)")
driver.quit()

# search_bar = driver.find_element_by_id("twotabsearchtextbox")
# search_bar.send_keys("Shoe for Mens")
# search_bar.send_keys(Keys.RETURN)

# select_img=driver.find_element_by_xpath("//img[@class='s-image']")
# scroll=driver.execute_script("arguments[0].scrollIntoView();",select_img)
# select_img.click()

# select_ele = driver.find_elements_by_class_name("s-image")
# link = select_ele[34]
# link.click()

# drop_Down = Select(driver.find_element_by_css_selector("select"))
# show = drop_Down.select_by_index(2)
# print(show)


# time.sleep(7)

