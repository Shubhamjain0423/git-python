from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import json
import sys
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup
import os
from   selenium import webdriver
from   selenium.common.exceptions import TimeoutException
import smtplib
import mimetypes
import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email import encoders
from email.message import Message
from email.mime.base import MIMEBase
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

me = "sjain336@dxc.com"
you = "sjain336@dxc.com"
msg = MIMEMultipart()
msg['Subject'] = "Insurance Portal Check"
msg['From'] = me
msg['To'] = ", ".join(you)

capabilities = DesiredCapabilities().FIREFOX
capabilities["marionette"] = True
#browser = webdriver.Firefox(capabilities=cap, executable_path=r'C:\geckodriver-v0.24.0-win32\geckodriver.exe')

#browser = webdriver.Firefox(capabilities=cap, executable_path=r'C:\geckodriver-v0.24.0-win32\geckodriver.exe')
binary = FirefoxBinary('C:/Program Files/Mozilla Firefox/firefox.exe')
driver = webdriver.Firefox(firefox_binary=binary, capabilities=capabilities, executable_path=r"C:\geckodriver-v0.29.1-win64\geckodriver.exe")


#driver = webdriver.Firefox(r'C:\geckodriver-v0.24.0-win32\geckodriver.exe')
driver.implicitly_wait(60)

user = "sushant.kumar@xchanging.com"
pwd = "01aug2021"
try:
    driver.get("https://insuranceportal.xchanging.com/")
    
    window_before = driver.window_handles[0]
    
    driver.find_element_by_link_text("login").click()
    
    window_after = driver.window_handles[1]
    
    driver.switch_to.window(window_after)
    
    driver.find_element_by_name("userId").click()
    driver.find_element_by_name("userId").click()
    driver.find_element_by_name("userId").clear()
    driver.find_element_by_name("userId").send_keys("sushant.kumar@xchanging.com")
    
    driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Password'])[1]/input[1]").clear()
    driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Password'])[1]/input[1]").send_keys("01aug2021")
    driver.find_element_by_link_text("OK").click()
    
    driver.switch_to.window(window_before)
    
    driver.find_element_by_link_text("Premium Tracker").click()
    driver.find_element_by_link_text("Transaction Status Management").click()
    driver.find_element_by_name("barCode").click()
    driver.find_element_by_name("barCode").clear()
    driver.find_element_by_name("barCode").send_keys("REP00243382")
    driver.find_element_by_link_text("submit").click()
    driver.find_element_by_xpath("/html/body/div/table[2]/tbody/tr/td[2]/div/div[2]/form[2]/div[1]/span[3]/table/tbody/tr[2]/td[1]/input")
    driver.quit()
	##/html/body/div/table[2]/tbody/tr/td[2]/div/table/tbody/tr/td[1]/span/h1
    html = "No Errors to report"
    msg.attach(MIMEText(html,'html'))
    s = smtplib.SMTP('smtp.xchanginghosting.com')

    s.sendmail(me, you,  msg.as_string())
    s.quit()
except:
    driver.quit()
    print("Something went wrong")
    html = "Few Errors to report"
    msg.attach(MIMEText(html,'html'))
    s = smtplib.SMTP('smtp.xchanginghosting.com')

    s.sendmail(me, you,  msg.as_string())
    s.quit()
####"/html/body/div/table[2]/tbody/tr/td[2]/div/div[2]/form[2]/div[1]/span[3]/table/tbody/tr[2]/td[1]/input"
####/html/body/div/table[2]/tbody/tr/td[2]/div/div[2]/form[2]/div[1]/span[3]/table/tbody/tr[2]/td[1]/input


