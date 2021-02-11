from selenium import webdriver
from time import sleep
chrome_driver = webdriver.Chrome(r"C:\Users\91824\Downloads\Compressed\chromedriver_win32\chromedriver")
chrome_driver.get("http://demowebshop.tricentis.com/")
chrome_driver.maximize_window()
sleep(3)
# _languages = ['Ruby', 'Python', 'JavaScript', 'Java', 'C#']
# for each in _languages:
#     chrome_driver.find_element_by_xpath(f"//td[.='{each}']/../td/input[@type='checkbox']").click()
#     sleep(1)
# _voates = ['Excellent', 'Poor', 'Good', 'Very bad']
# for each in _voates:
#     chrome_driver.find_element_by_xpath(f"//label[.='{each}']/../input[@type='radio']").click()
#     sleep(1)

# _actual = {
#     "$25 Virtual Gift Card":25.00,
#     "Build your own computer":1200.00,
#     "Build your own expensive computer":1800.00,
#     "Simple Computer":800.00,
#     "Build your own cheap computer":800.00,
#     "14.1-inch Laptop":159.00
# }
#
# for _item in _actual:
#     _xpath = chrome_driver.find_element_by_xpath(f"//h2[@class='product-title']//a[.='{_item}']/../..//span")
#     print(f"{_xpath.text} is sucessfully equal to {_actual[_item]}" if float(_xpath.text)==_actual[_item] else "its not matching")
# data = chrome_driver.find_element_by_xpath("//h2[@class='product-title']//a[.='$25 Virtual Gift Card']/../..//span")
# if float(data.text)==float(xpect):
#     print('True')
# else:
#     print('False')
# //div[@class='details']//a[.='Health Book']
# _books = ['Health Book', 'Science', 'Coumpting and Internet', 'Fiction']
# for book in _books:
# _xpath = \
# _books = ['Fiction', 'Computing and Internet', 'Health Book', 'Science']
# l=[2,3,4,5]
# chrome_driver.find_element_by_xpath("//ul[@class='top-menu']//a[contains(text(),'Books')]").click()
# for _book in _books:
#     _xpath = f"//div[@class='details']//a[.='{_book}']/../..//div[@class='buttons']"
#     chrome_driver.find_element_by_xpath(_xpath).click()
#     sleep(1)
# sleep(5)
# chrome_driver.find_element_by_xpath("//span[.='Shopping cart']").click()
# for j,k in zip(_books,l):
#     _xpath = f"(//a[.='{j}'])[2]/../..//input[@type='text']"
#     chrome_driver.find_element_by_xpath(_xpath).clear()
#     chrome_driver.find_element_by_xpath(_xpath).send_keys(k)
#     sleep(1)
    # chrome_driver.find_element_by_xpath("// tbody // input[ @ value = '1']").send_keys(3)