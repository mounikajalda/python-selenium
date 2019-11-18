from selenium import webdriver

print("directory in selenium.")
print(dir(webdriver))

# chrome driver path
path = "C://Users//vamsi//python-selenium//chromedriver.exe"
driver = webdriver.Chrome(path)
# url path
driver.get("http://stackoverflow.com")
# 