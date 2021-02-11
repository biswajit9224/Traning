from selenium import webdriver
import time
from selenium.webdriver.support.select import Select
chrome_driver= webdriver.Chrome(r"C:\Users\91824\Downloads\Compressed\chromedriver_win32\chromedriver")
# time.sleep(3)
# chrome_driver.get(r"file:///D:/python_practice/traning/selenium/html_files/abs_path.html")
# time.sleep(3)

# chrome_driver.find_element_by_name('text')
# time.sleep(3)
# chrome_driver.get('http://demowebshop.tricentis.com/')
# time.sleep(5)

# chrome_driver.find_element_by_xpath("//a[text()='Register']").click()
# time.sleep(2)

# chrome_driver.find_element_by_xpath("//input[@id='gender-male']").click()
# time.sleep(2)

# chrome_driver.find_element_by_xpath("//input[@id='FirstName']").send_keys('Biswajit')
# time.sleep(2)

# chrome_driver.find_element_by_xpath("//input[@id='LastName']").send_keys('Dash')
# time.sleep(2)

# chrome_driver.find_element_by_xpath("//input[@id='Email']").send_keys('hai_hallo@gmail.com')
# time.sleep(2)

# chrome_driver.find_element_by_xpath("//input[@id='Password']").send_keys('kanha_')
# time.sleep(2)

# chrome_driver.find_element_by_xpath("//input[@id='ConfirmPassword']").send_keys('kanha_')
# time.sleep(2)

# chrome_driver.find_element_by_xpath("//input[@name='register-button']").click()
# time.sleep(4)

# chrome_driver.find_element_by_name('q').send_keys('healthbook')
# time.sleep(5)
# data = chrome_driver.find_elements_by_css_selector('input[value="Search"]')
# print(type(data))
# for each in data:
#     print(each)
# chrome_driver.find_elements_by_link_text('Register').click()

# time.sleep(5)
# chrome_driver.implicitly_wait(20)
# time.sleep(10)
# data = chrome_driver.title
# print(data)
# driver.close()#only close the parent pop up
# driver.quit()#both child and parent pop up will close
# chrome_driver.maximize_window

chrome_driver.get(r'file:///D:/python_practice/traning/selenium/html_files/first.html')
element = chrome_driver.find_element_by_id('dd')
s = Select(element)
time.sleep(2)
s.select_by_visible_text('audi')
time.sleep(2)
s.select_by_visible_text('honda')
time.sleep(2)


optionss = s.options

for index in range(1,len(optionss)):
    s.select_by_index(index)
    time.sleep(1)

# items = []
# for i in optionss:          #or items = [i.text for i in optionss]
#     items.append(i.text)


for item in items:
    s.select_by_visible_text(item)
    time.sleep(1)







