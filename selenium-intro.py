from selenium import webdriver

'''
1. create a selenium instance using 1 function
2. call a url using 2nd function
3. get the properties of the url 3rd function
'''

def Selenium_instance():
    #  1st
    print(" i am in selenium instance")
    path = "C://Users//vamsi//python-selenium//chromedriver.exe"
    driver = webdriver.Chrome(path)
    url= "http://stackoverflow.com"
    obj1 = getUrl(url,driver)

def getUrl(URL,driver):
    # 2nd
    print("i am in get url")
    webpage= driver.get(URL)
    # print(dir(driver))
    obj2 = prop_url(driver)
    

def prop_url(driver):
    print("i am in prop url")
    print("page title: ",driver.title)


obj = Selenium_instance()
