from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests
import json

driver = webdriver.Chrome(executable_path='/Users/maruiling/Downloads/chromedriver')
driver.get("https://waterlooworks.uwaterloo.ca/myAccount/co-op/coop-postings.htm")

driver.find_element_by_xpath("//a[@class='button']").click()

driver.find_element_by_xpath("//a[@href='https://waterlooworks.uwaterloo.ca/waterloo.htm?action=login']").click()

user = "r66ma@edu.uwaterloo.ca"
driver.find_element_by_xpath("//input[@id='userNameInput']").send_keys(user)

driver.find_element_by_xpath("//span[@id='nextButton']").click()

pwd = "nope"
driver.find_element_by_xpath("//input[@id='passwordInput']").send_keys(pwd)

driver.find_element_by_xpath("//span[@id='submitButton']").click()

driver.find_element_by_xpath("//a[@class='clickGuard'][@href='/myAccount/co-op.htm']").click()

#elemet = driver.find_element_by_xpath("//td[@class='full'][contains(text(), 'For My Program')]")
driver.find_element_by_xpath("//input[@type='submit'][@value='Search']").click()


html = driver.page_source
soup = BeautifulSoup(html, 'lxml')

divTages = soup.find_all('div', attrs={'class': 'btn-group'})
job = {}
for div in divTages:
    try:
        job['title'] = div.find('a', attrs={'href': 'javascript:void(0);'}).text.strip()
    except:
        print("问题")
print(job)