'''
website url
get title

functions

'''
from selenium import webdriver
import time


def Selenium_Instance2():
    print('am instance')

    path_1 = "C://Users//vamsi//python-selenium//chromedriver.exe"
    driver = webdriver.Chrome(path_1)
    url = "http://blazedemo.com/"
    page = driver.get(url)
    # write find elements by ...
    header = driver.find_elements_by_css_selector('div[class="container"] h1')[0].text
    slect = driver.find_element_by_xpath("//select[@name='fromPort']/option[text()='Boston']").click() 
    #find_element_by_xpath("//select[@name='element_name']/option[text()='option_text']").click() toPort
    slect_destination = driver.find_element_by_xpath("//select[@name='toPort']/option[text()='Rome']").click() 
    driver.find_elements_by_css_selector('input[class="btn btn-primary"]')[0].click()
    time.sleep(20)


def launchApp(url,driver):
    print('am launching url')
    page = driver.get(url)
    # write find elements by ...
    header = driver.find_elements_by_css_selector('div[class="container"] h1')[0].text
    slect = driver.find_element_by_xpath("//select[@name='fromPort']/option[text()='Boston']").click() 
    #find_element_by_xpath("//select[@name='element_name']/option[text()='option_text']").click() toPort
    slect_destination = driver.find_element_by_xpath("//select[@name='toPort']/option[text()='Rome']").click() 
    #driver.find_elements_by_css_selector('input[class="btn btn-primary"]')[0].click()
    print(header)

#    Pwd = driver.find_element_by_class_name('inputtext.login_form_input_box')

obj = Selenium_Instance2()