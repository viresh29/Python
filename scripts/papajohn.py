from fake_useragent import UserAgent
from selenium import webdriver
from random import randrange
import time


ua = UserAgent(verify_ssl=False)
user_agent = ua.random

print("User Agent - " + user_agent)

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("user-agent=" + user_agent)
driver = webdriver.Chrome(chrome_options=chrome_options)

id = randrange(100000000000000)
url = "https://www.papajohnsfeedback.com/GBR?GUID=" + str(id)

print(url)

driver.get(url)
time.sleep(1)

driver.find_element_by_id('NextButton').click()
time.sleep(1)

driver.find_element_by_id('NextButton').click()
time.sleep(1)

driver.find_element_by_xpath("//div[contains(@class, 'Opt1')]/span").click()
time.sleep(1)


driver.find_element_by_id('NextButton').click()
time.sleep(1)

code = driver.find_element_by_class_name(
    'ValCode').get_attribute("innerHTML").split(' ')[2]
