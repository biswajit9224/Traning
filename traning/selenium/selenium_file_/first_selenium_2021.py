from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import visibility_of_element_located
chrome_driver = webdriver.Chrome(r"C:\Users\91824\Downloads\Compressed\chromedriver_win32\chromedriver")
chrome_driver.get(r'file:///D:/python_practice/traning/selenium/html_files/loading.html')

# chrome_driver.get(r'file:///D:/python_practice/traning/selenium/html_files/prograssbar.html')
# chrome_driver.get("https://www.naukri.com/")
# sleep(5)
# chrome_driver.maximize_window()
# sleep(3)
# handels = chrome_driver.window_handles
# sleep(5)
# for handel in handels[1:]:
#     chrome_driver.switch_to.window(handel)
#     chrome_driver.close()
#     sleep(2)
#
# chrome_driver.switch_to.window(handels[0])
# sleep(3)
# chrome_driver.find_element_by_xpath("(//input[@class='sugInp'])[1]").send_keys('python')
# sleep(2)
# chrome_driver.find_element_by_xpath("//button[.='Search']").click()
# sleep(2)
# lists = chrome_driver.find_elements_by_xpath("//article[@class='jobTuple bgWhite br4 mb-8']//div[@class='jobTupleHeader']//a")
# sleep(8)
# for index,each in enumerate(lists):
#     print(index,each.text)





























# handels = chrome_driver.window_handles
# sleep(1)
# for i in handels[1:]:
#     chrome_driver.switch_to.window(i)
#     chrome_driver.close()
#     sleep(1)
# chrome_driver.switch_to.window(handels[0])
# sleep(2)
# chrome_driver.find_element_by_xpath("(//input[@class='sugInp'])[1]").send_keys("python")
#
# sleep(1)
#
# chrome_driver.find_element_by_xpath("//button[@class='btn']").click()
#
# sleep(10)
#
# links = chrome_driver.find_elements_by_xpath("//a[@class='title fw500 ellipsis']")
#
# sleep(2)

# print(len(links))
# for i in links:
#     print(i.text)
#     sleep(1)
# links[0].click()
# sleep(6)
# chrome_driver.find_element_by_xpath("(//button[.='Apply'])[1]")
# sleep(1)


# chrome_driver.get("http://demowebshop.tricentis.com/")
# chrome_driver.maximize_window()
# sleep(2)
# chrome_driver.find_element_by_xpath("//input[@value='Search']").click()
# sleep(3)
# opts = webdriver.ChromeOptions()

# print(chrome_driver.switch_to.alert.text)
# chrome_driver.switch_to.alert.accept()


#
# sleep(3)
# chrome_driver.find_element_by_xpath("//a[.='Twitter']").click()
# sleep(5)
# handels = chrome_driver.window_handles
# chrome_driver.switch_to.window(handels[1])
# sleep(1)
# chrome_driver.find_element_by_xpath("//input[@data-testid='SearchBox_Search_Input']").send_keys('hello')
# handels = chrome_driver.window_handles
# for handel in handels:
#     print(hand
# for handel in handels[1:]:
#     chrome_driver.switch_to.window(handel)
#     # print(chrome_driver.title)
#     # sleep(1)
#     if chrome_driver.title=='ICICI':
#         chrome_driver.close()

# w = WebDriverWait(chrome_driver,15)
# v = visibility_of_element_located(("name","fname"))
# w.until(v)
# chrome_driver.find_element_by_name('fname').send_keys("hello")
# chrome_driver.find_element_by_xpath("//button[.='Click Me']").click()
# w = WebDriverWait(chrome_driver,10)
# warp = visibility_of_element_located(("xpath","//div[.='100%']"))
# w.until(warp)
# print('done')
