#WORKS 0912/2021 1233
# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support import expected_conditions as expected
from selenium.webdriver.support.wait import WebDriverWait
import unittest, time, re, os
import timeit
import shutil
import json
import smtplib, ssl #needed for sending email
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from datetime import date
##############CHROME OPTIONS#########################################
option = webdriver.ChromeOptions()
extset = ['enable-automation', 'ignore-certificate-errors']
ignimg = "profile.managed_default_content_settings.images"
#mobile = {'deviceName':'Galaxy S5'}
mobile = {'deviceName':'iPhone 6'}
#mobile = {'deviceName':'iPad Mini'}
option.add_argument("--disable-infobars") #Prevents msg Chrome is being controlled by automated software
option.add_experimental_option("excludeSwitches", extset)
option.add_experimental_option('mobileEmulation', mobile)
#option.add_argument('--start-maximized')
#option.add_argument('--headless') 
option.add_argument('--window-size=360,768')
#option.add_argument('--window-size=1920,1080') #Galaxy S5 
#option.add_argument('--window-size=750 , 1334') #iPhone 6
#options.add_argument("--window-size=800,600")
option.add_argument('--disable-gpu') 
#option.add_argument('-disable-popup-blocking')
#option.add_argument('--disable-multi-display-layout')
#option.add_argument('--3d-display-mode')
#option.add_argument("--auto-open-devtools-for-tabs") #OPENS CHROME DEV TOOLS
######################################################################################################################
#driver.find_element_by_xpath("").click()
#driver.find_element_by_css_selector("").click() 
#driver.find_element_by_css_selector("#header > div > div > div.header__logo > a > img:nth-child(3)").click()  #CM HOME
######################################################################################################################
#driver = webdriver.Chrome(chrome_options=option) #DEPRECATED
driver = webdriver.Chrome(options=option)
driver.implicitly_wait(20)
driver.get('https://www.cryptomaniaks.com')
#===============================================================================================================
