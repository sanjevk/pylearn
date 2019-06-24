from time import sleep

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome()

driver.get("https://www.google.com")
driver.maximize_window()
page_title = driver.title
expected_title = "Google"
if (page_title == expected_title) is True:
    print("Title matches")


search_name = "q"
driver.find_element_by_name(search_name).send_keys("Sanjev", Keys.RETURN)
links = driver.find_elements_by_xpath("//h3[@class='LC20lb']/a[@href]")  # searches for all links insede h3 tags with class "r"
for link in links:
    d = {'url': link.get_attribute('href'),
         'title': link.text}
    print(d)
driver.close()




