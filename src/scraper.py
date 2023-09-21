from platform import python_branch
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from time import sleep

# def read_and_write():

# driver = webdriver.Chrome(ChromeDriverManager().install())
options = Options()
options.binary_location = '/Applications/Brave Browser.app/Contents/MacOS/Brave Browser'
driver = webdriver.Chrome(options=options)

driver.get("https://signon.jgi.doe.gov/")
sleep(3)

# login
driver.find_element("xpath", "//*[@id='login']").send_keys("asandhu@olin.edu")
driver.find_element("xpath", "//*[@id='password']").send_keys("repSak-hajha1-zirvyx")
driver.find_element("xpath", "//*[@id='password']").send_keys(Keys.RETURN)
sleep(3)

# scaffold search
driver.get("https://img.jgi.doe.gov/cgi-bin/mer/main.cgi?section=ScaffSearch&page=searchForm")
sleep(2)

# for scaffold in scaffolds:

# search scaffold
driver.find_element("xpath", "//*[@id='myAutoInput']").send_keys("Ga0508132_00002")
driver.find_element("xpath", "//*[@id='myAutoInput']").send_keys(Keys.RETURN)
sleep(2)

# click on result
driver.find_element("xpath", "//*[@id='yui-rec0']/td[2]/div/a").click()
sleep(2)

# click on Gene count link which leads to gene table
driver.find_element("xpath", "//*[@id='content_other']/form/table/tbody/tr[5]/td/a").click()
sleep(2)

# click on select all button
driver.find_element("xpath", "//*[@id='genelist1']").click()
sleep(1)

# click on export button
driver.find_element("xpath", "//*[@id='genelist-navA-Export-button']").click()
sleep(1)
# press enter with pynput
sleep(1)


sleep(10)
