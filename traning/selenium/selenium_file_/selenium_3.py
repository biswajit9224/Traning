from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
chrome_driver = webdriver.Chrome(r"C:\Users\91824\Downloads\Compressed\chromedriver_win32\chromedriver")
action = ActionChains(chrome_driver)
# chrome_driver.get("file:///D:/python_practice/traning/selenium/html_files/parent_child.html")
chrome_driver.get("https://www.monsterindia.com/")
sleep(5)

chrome_driver.find_element_by_xpath("//a[@target='_blank'][.='Fresher Jobs']").click()
# chrome_driver.find_element_by_xpath("//input[@title='Search']").click()