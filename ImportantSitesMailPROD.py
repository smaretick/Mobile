#09/6/2021
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
from datetime import datetime
from datetime import date
#--------------------------------------------------------------------------------------------------
#FILE/APP INIT######################################################################################
#--------------------------------------------------------------------------------------------------#
path = os.getcwd()
print ("The current working directory is %s" % path)
dir_name = "SCREENSHOTSIMP"
completeName = os.path.join(path, dir_name)
print(completeName)
#----------------------------------------------------------------------------------------------------
#f = open('curl.txt', 'w')
f = open('SeleniumIMP.txt', 'w')
f.write('OPENING OUTPUT FILE SeleniumIMP.txt \n')
print ("OPENING OUTPUT FILE SeleniumIMP.txt")
#print ("The screenshots directory is %s" % completeName)
#f.write('The screenshots directory is %s" % completeName \n')
#------CHECK FOR EXISTING SCREENSHOTSIMP DIR------#
if os.path.isdir(dir_name):
   f.write('SCREENSHOTSIMP DIR EXISTS  \n')
   #os.rmdir(dir_name)
   #shutil. rmtree (completeName)
   #print ("CREATING SCREENSHOTSIMP")
   #os.mkdir(completeName)
else:
   print ("SCREENSHOTSIMP DIR CREATED")
   os.mkdir(completeName)
#----------------------------------------------------------------------------------------------------
#-----------------TIMING----------------------------------------------------------------------------- 
#DATE & TIME
now = datetime.now() # current date and time
time = now.strftime("%H:%M:%S") 
print("time:", time)
date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
print("date and time:",date_time)
now = datetime.now() # current date and time
#d2 = today.strftime("%B %d, %Y") #dd/mm/YY
dt_string = now.strftime("%m/%d/%Y %H:%M:%S")
#print ("The start time is %s" % d2)
#f.write('"The start time is %s" % d2) \n')
print("date and time =", dt_string)
f.write("The date & time is %s \n" % dt_string)
time = now.strftime("%H:%M:%S")
print("time:", time)
print ("The start time is %s" % time)
#print("--- %s seconds ---" % (time.time() - time))
#f.write('"--- %s seconds ---" % (time.time() - time) \n')
f.write('The start time is %s" % time \n')
#####################HEADLESS BROWSER##############################################################
options = FirefoxOptions()
options.add_argument("--headless")
print ("FirefoxOptions %s" % options)
browser = webdriver.Firefox(options=options)
browser.get("https://cryptomaniaks.com") #CRYPTOMANIAKS SITE
browser.implicitly_wait(20)
print ("Opening Headless Browser to https://cryptomaniaks.com")
f.write('Opening Headless Browser to https://cryptomaniaks.com \n')
browser.save_screenshot(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'SCREENSHOTSIMP', 'ScreenShot1.png'))
#####################ELEMENTS#####################################################################
#----------------------------------------------------------------------------------------------------
#FIREFOX##########################################################################################
#browser = webdriver.Firefox()
#browser.implicitly_wait(15)
#browser.maximize_window()
#browser.save_screenshot('/Users/scott/Desktop/SCREENSHOTSIMP/ScreenShot1.png')
#print ("Firefox Opening Browser")
#f.write('Opening Firefox Browser \n')
#CHROME###########################################################################################
#ChromeDriver
#DesiredCapabilities capabilities = DesiredCapabilities.chrome();
#desired_capabilities=DesiredCapabilities.CHROME
#capabilities.setCapability("chrome.verbose", false);
#options = webdriver.ChromeOptions();
#options.add_argument("--start-maximized");
#browser = webdriver.Chrome(options)
#browser = webdriver.Chrome(chrome_options=options)
#browser.save_screenshot('/Users/scott/Desktop/SCREENSHOTSIMP/ScreenShot1.png')
#browser = webdriver.Chrome()
#----------------------------------------------------------------------------------------------------
#SEND MAIL########################################################################################
def Send_Mail():
	fromaddr = "scottmaretick51@gmail.com"
	toaddr = "gayle@cryptomaniaks.com"
	#toaddr = "scottmaretick51@gmail.com"
	msg = MIMEMultipart()
	msg['From'] = fromaddr
	msg['To'] = toaddr
	msg['Subject'] = "Important Sites"
	body = "The Important Sites automated checker ran"
	msg.attach(MIMEText(body, 'plain'))
	filename = "SeleniumIMP.txt"
	os.chdir(path)
	#attachment = open("/Users/scott/Desktop/SeleniumIMP.txt", "rb")
	attachment = open("SeleniumIMP.txt", "rb")
	p = MIMEBase('application', 'octet-stream')
	p.set_payload((attachment).read())
	encoders.encode_base64(p)
	p.add_header('Content-Disposition', "attachment; filename= %s" % filename)
	msg.attach(p)
	s = smtplib.SMTP('smtp.gmail.com', 587)
	s.starttls()
	s.login(fromaddr, "Sm110751$")
	text = msg.as_string()
	s.sendmail(fromaddr, toaddr, text)
	s.quit()
#################################################################################################
os.path.abspath(os.getcwd())
#browser.save_screenshot(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'SCREENSHOTSIMP', 'ScreenShotXX.png'))
#################################################################################################
browser.implicitly_wait(15)
browser.get("https://cryptomaniaks.com") #CRYPTOMANIAKS SITE
print ("Opening Browser to https://cryptomaniaks.com")
f.write('Opening Browsr to https://cryptomaniaks.com \n')
#time.sleep(15)
#browser.save_screenshot('/Users/scott/Desktop/SCREENSHOTSIMP/ScreenShot2.png')
browser.save_screenshot(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'SCREENSHOTSIMP', 'ScreenShot2.png'))
print ("Capturing screenshot2 cryptomaniaks.com")
f.write('Capturing screenshot2 cryptomaniaks.com \n')
#----------------------------------------------------------------------------------------------------
print ("Return Code https://cryptomaniaks.com Browser")
os.system('curl -Is https://cryptomaniaks.com/| head -1 ')
#browser.title = https://cryptomaniaks.com
#print "browser.title is %s." % browser.title
#1---------------------------------------------------------------------------------------------------
browser.implicitly_wait(15)  
browser.get("https://cryptomaniaks.com/latest-cryptocurrency-news/best-crypto-sports-betting-sites")
print ("Navigating to #1 best-crypto-sports-betting-sites")
f.write('Navigating to #1 best-crypto-sports-betting-sites \n')
#browser.save_screenshot('/Users/scott/Desktop/SCREENSHOTSIMP/ScreenShot3.png')
browser.save_screenshot(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'SCREENSHOTSIMP', 'ScreenShot3.png'))
print ("Capturing screenshot #3")
f.write('Capturing screenshot #3 \n')
#----------------------------------------------------------------------------------------------------
#curl -Is https://cryptomaniaks.com/latest-cryptocurrency-news/best-crypto-sports-betting-sites | head -1 | awk '{print "best-crypto-sports-betting-sites " $2}' > curl.txt
print ("Return Code https://cryptomaniaks.com/latest-cryptocurrency-news/best-crypto-sports-betting-sites Browser")
os.system('curl -Is https://cryptomaniaks.com/latest-cryptocurrency-news/best-crypto-sports-betting-sites | head -1')
#2---------------------------------------------------------------------------------------------------
browser.implicitly_wait(15)
browser.get("https://cryptomaniaks.com/stake-review")
print ("Navigating to #2 stake-review site")
f.write('Navigating to #2 stake-review site \n')
#browser.save_screenshot('/Users/scott/Desktop/SCREENSHOTSIMP/ScreenShot4.png')
browser.save_screenshot(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'SCREENSHOTSIMP', 'ScreenShot4.png'))
print ("Capturing screenshot #4")
f.write('Capturing screenshot #4 \n')
#----------------------------------------------------------------------------------------------------
#os.system('curl -Is https://cryptomaniaks.com/stake-review | head -1 | awk '{print "stake-review " $2}'')
print ("Return Code https://cryptomaniaks.com/stake-review")
os.system('curl -Is https://cryptomaniaks.com/stake-review | head -1')
#3---------------------------------------------------------------------------------------------------
browser.implicitly_wait(15)
browser.get("https://cryptomaniaks.com/latest-cryptocurrency-news/best-crypto-sports-betting-sites")
print ("Navigating to CM Most Valuable & Important Pages #3 site")
f.write('Navigating to CM Most Valuable & Important Pages #3 site \n')
#browser.save_screenshot('/Users/scott/Desktop/SCREENSHOTSIMP/ScreenShot5.png')
browser.save_screenshot(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'SCREENSHOTSIMP', 'ScreenShot5.png'))
print ("Capturing screenshot #5")
f.write('Capturing screenshot #5 \n')
#----------------------------------------------------------------------------------------------------
#os.system('curl -Is https://cryptomaniaks.com/latest-cryptocurrency-news/best-crypto-sports-betting-sites | head -1 | awk '{print "best-crypto-sports-betting-sites " $2}'')
print ("Return Code https://cryptomaniaks.com/latest-cryptocurrency-news/best-crypto-sports-betting-sites")
os.system('curl -Is https://cryptomaniaks.com/latest-cryptocurrency-news/best-crypto-sports-betting-sites | head -1')
#4---------------------------------------------------------------------------------------------------
browser.implicitly_wait(15)
browser.get("https://cryptomaniaks.com/best-bitcoin-casinos")
print ("Navigating to #4 best-bitcoin-casinos site")
f.write('Navigating to #4 best-bitcoin-casinos site \n')
#browser.save_screenshot('/Users/scott/Desktop/SCREENSHOTSIMP/ScreenShot6.png')
browser.save_screenshot(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'SCREENSHOTSIMP', 'ScreenShot6.png')) 
print ("Capturing screenshot #6")
f.write('Capturing screenshot #6 \n')
#----------------------------------------------------------------------------------------------------
#os.system('curl -Is https://cryptomaniaks.com/best-bitcoin-casinos | head -1 | awk '{print "best-bitcoin-casinos " $2}'')
print ("Return Code https://cryptomaniaks.com/best-bitcoin-casinos")
os.system('curl -Is https://cryptomaniaks.com/best-bitcoin-casinos | head -1')
#5---------------------------------------------------------------------------------------------------
browser.implicitly_wait(15)
browser.get("https://cryptomaniaks.com/bitcoin-gambling-sites")
print ("Navigating to #5 bitcoin-gambling-sites")
f.write('Navigating to #5 bitcoin-gambling-sites \n')
#browser.save_screenshot('/Users/scott/Desktop/SCREENSHOTSIMP/ScreenShot7.png')
browser.save_screenshot(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'SCREENSHOTSIMP', 'ScreenShot7.png')) 
print ("Capturing screenshot #7")
f.write('Capturing screenshot #7 \n')
#----------------------------------------------------------------------------------------------------
#os.system('curl -Is https://cryptomaniaks.com/bitcoin-gambling-sites | head -1 | awk '{print "bitcoin-gambling-sites " $2}'')
print ("Return Code https://cryptomaniaks.com/bitcoin-gambling-sites")
os.system('curl -Is https://cryptomaniaks.com/bitcoin-gambling-sites | head -1')
#6---------------------------------------------------------------------------------------------------
browser.implicitly_wait(15)
browser.get("https://cryptomaniaks.com/ethereum-casinos")
print ("Navigating to #6 ethereum-casinos site")
f.write('Navigating to #6 ethereum-casinos site \n')
#browser.save_screenshot('/Users/scott/Desktop/SCREENSHOTSIMP/ScreenShot8.png')
browser.save_screenshot(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'SCREENSHOTSIMP', 'ScreenShot8.png'))
print ("Capturing screenshot #8")
f.write('Capturing screenshot #8 \n')
#----------------------------------------------------------------------------------------------------
#os.system('curl -Is https://cryptomaniaks.com/ethereum-casinos site | head -1 | awk '{print "ethereum-casinos site " $2}'')
print ("Return Code https://cryptomaniaks.com/ethereum-casinos site")
os.system('curl -Is https://cryptomaniaks.com/ethereum-casinos site | head -1')
#7---------------------------------------------------------------------------------------------------
browser.implicitly_wait(15)
browser.get("https://cryptomaniaks.com/ethereum-gambling-sites")
print ("Navigating to #7 ethereum-gambling-sites")
f.write('Navigating to #7 ethereum-gambling-sites \n')
#browser.save_screenshot('/Users/scott/Desktop/SCREENSHOTSIMP/ScreenShot9.png')
browser.save_screenshot(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'SCREENSHOTSIMP', 'ScreenShot9.png')) 
print ("Capturing screenshot #9")
f.write('Capturing screenshot #9 \n')
#----------------------------------------------------------------------------------------------------
#os.system('curl -Is https://cryptomaniaks.com/ethereum-gambling-sites | head -1 | awk '{print "ethereum-gambling-sites " $2}'')
print ("Return Code https://cryptomaniaks.com/ethereum-gambling-sites")
os.system('curl -Is https://cryptomaniaks.com/ethereum-gambling-sites | head -1')
#8---------------------------------------------------------------------------------------------------
browser.implicitly_wait(15)
browser.get("https://cryptomaniaks.com/best-bitcoin-roulette-sites") 
print ("Navigating to #8 best-bitcoin-roulette-sites")
f.write('Navigating to #8 best-bitcoin-roulette-sites \n')
#browser.save_screenshot('/Users/scott/Desktop/SCREENSHOTSIMP/ScreenShot10.png')
browser.save_screenshot(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'SCREENSHOTSIMP', 'ScreenShot10.png'))
print ("Capturing screenshot #10")
f.write('Capturing screenshot #10 \n')
#----------------------------------------------------------------------------------------------------
#os.system('curl -Is https://cryptomaniaks.com/best-bitcoin-roulette-sites | head -1 | awk '{print "best-bitcoin-roulette-sites " $2}'')
print ("Return Code https://cryptomaniaks.com/best-bitcoin-roulette-sites")
os.system('curl -Is https://cryptomaniaks.com/best-bitcoin-roulette-sites | head -1')
#9---------------------------------------------------------------------------------------------------
browser.implicitly_wait(15)
browser.get("https://cryptomaniaks.com/best-way-to-buy-bitcoin")
print ("Navigating to #9 best-way-to-buy-bitcoin site")
f.write('Navigating to #9 best-way-to-buy-bitcoin site \n')
#browser.save_screenshot('/Users/scott/Desktop/SCREENSHOTSIMP/ScreenShot11.png')
browser.save_screenshot(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'SCREENSHOTSIMP', 'ScreenShot11.png'))
print ("Capturing screenshot #11")
f.write('Capturing screenshot #11 \n')
#----------------------------------------------------------------------------------------------------
#os.system('curl -Is https://cryptomaniaks.com/best-way-to-buy-bitcoin | head -1 | awk '{print "best-way-to-buy-bitcoin " $2}'')
os.system('curl -Is https://cryptomaniaks.com/best-way-to-buy-bitcoin | head -1')
print ("Return Code https://cryptomaniaks.com/best-way-to-buy-bitcoin")
#10--------------------------------------------------------------------------------------------------
browser.implicitly_wait(15)
browser.get("https://cryptomaniaks.com/guides/best-crypto-tools-checklist")
print ("Navigating to #10 best-bitcoin-lending-sites")
f.write('Navigating to #10 best-bitcoin-lending-sites \n')
#browser.save_screenshot('/Users/scott/Desktop/SCREENSHOTSIMP/ScreenShot12.png')
browser.save_screenshot(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'SCREENSHOTSIMP', 'ScreenShot12.png'))
print ("Capturing screenshot #12")
f.write('Capturing screenshot #12 \n')
#----------------------------------------------------------------------------------------------------
print ("Return Code https://cryptomaniaks.com/guides/best-crypto-tools-checklist")
os.system('curl -Is https://cryptomaniaks.com/guides/best-crypto-tools-checklist | head -1')
#11--------------------------------------------------------------------------------------------------
browser.implicitly_wait(15)
browser.get("https://cryptomaniaks.com/guides/best-crypto-tools-checklist")
print ("Navigating to #11 best-crypto-tools-checklist site")
f.write('Navigating to #11 best-crypto-tools-checklist site \n')
#browser.save_screenshot('/Users/scott/Desktop/SCREENSHOTSIMP/ScreenShot13.png')
browser.save_screenshot(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'SCREENSHOTSIMP', 'ScreenShot13.png'))
print ("Capturing screenshot #13")
f.write('Capturing screenshot #13 \n')
#----------------------------------------------------------------------------------------------------
#os.system('curl -Is https://cryptomaniaks.com/guides/best-crypto-tools-checklist | head -1 | awk '{print "best-crypto-tools-checklist " $2}'')
print ("Return Code https://cryptomaniaks.com/guides/best-crypto-tools-checklist")
os.system('curl -Is https://cryptomaniaks.com/guides/best-crypto-tools-checklist | head -1')
#12--------------------------------------------------------------------------------------------------
browser.implicitly_wait(15)
browser.get("https://cryptomaniaks.com/recommended-websites-tools")
print ("Navigating to #12 recommended-websites-tools site")
f.write('Navigating to #12 recommended-websites-tools site \n')
#browser.save_screenshot('/Users/scott/Desktop/SCREENSHOTSIMP/ScreenShot14.png')
browser.save_screenshot(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'SCREENSHOTSIMP', 'ScreenShot14.png'))
print ("Capturing screenshot #14")
f.write('Capturing screenshot #14 \n')
#----------------------------------------------------------------------------------------------------
#os.system('curl -Is https://cryptomaniaks.com/recommended-websites-tools | head -1 | awk '{print "recommended-websites-tools " $2}'')
print ("Return Code https://cryptomaniaks.com/recommended-websites-tools")
os.system('curl -Is https://cryptomaniaks.com/recommended-websites-tools | head -1')
#13--------------------------------------------------------------------------------------------------
browser.get("https://cryptomaniaks.com/best-cryptocurrencies-to-buy")
print ("Navigating to #13 best-cryptocurrencies-to-buy site")
f.write('Navigating to #13 best-cryptocurrencies-to-buy site \n')
#browser.save_screenshot('/Users/scott/Desktop/SCREENSHOTSIMP/ScreenShot15.png')
browser.save_screenshot(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'SCREENSHOTSIMP', 'ScreenShot15.png'))
print ("Capturing screenshot #15")
f.write('Capturing screenshot #15 \n')
#----------------------------------------------------------------------------------------------------
#os.system('curl -Is https://cryptomaniaks.com/best-cryptocurrencies-to-buy | head -1 | awk '{print "13 best-cryptocurrencies-to-buy " $2}'')
print ("Return Code https://cryptomaniaks.com/best-cryptocurrencies-to-buy")
os.system('curl -Is https://cryptomaniaks.com/best-cryptocurrencies-to-buy | head -1')
#14--------------------------------------------------------------------------------------------------
browser.get("https://cryptomaniaks.com/how-much-to-invest-bitcoin")
print ("Navigating to #14 how-much-to-invest-bitcoin site")
f.write('Navigating to #14 how-much-to-invest-bitcoin site \n')
#browser.save_screenshot('/Users/scott/Desktop/SCREENSHOTSIMP/ScreenShot16.png')
browser.save_screenshot(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'SCREENSHOTSIMP', 'ScreenShot16.png'))
print ("Capturing screenshot #16")
f.write('Capturing screenshot #16 \n')
#----------------------------------------------------------------------------------------------------
#os.system('curl -Is https://cryptomaniaks.com/how-much-to-invest-bitcoin | head -1 | awk '{print "how-much-to-invest-bitcoin " $2}'')
print ("Return Code https://cryptomaniaks.com/how-much-to-invest-bitcoin")
os.system('curl -Is https://cryptomaniaks.com/how-much-to-invest-bitcoin | head -1')
#15--------------------------------------------------------------------------------------------------
browser.get("https://cryptomaniaks.com/best-bitcoin-poker-sites") 
print ("Navigating to #15 best-bitcoin-poker-sites")
f.write('Navigating to #15 best-bitcoin-poker-sites \n')
#browser.save_screenshot('/Users/scott/Desktop/SCREENSHOTSIMP/ScreenShot17.png')
browser.save_screenshot(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'SCREENSHOTSIMP', 'ScreenShot17.png'))
print ("Capturing screenshot #17")
f.write('Capturing screenshot #17 \n')
#----------------------------------------------------------------------------------------------------
#os.system('curl -Is https://cryptomaniaks.com/best-bitcoin-poker-sites | head -1 | awk '{print "best-bitcoin-poker-sites " $2}'')
print ("Return Code https://cryptomaniaks.com/best-bitcoin-poker-sites")
os.system('curl -Is https://cryptomaniaks.com/best-bitcoin-poker-sites | head -1')
#16--------------------------------------------------------------------------------------------------
browser.get("https://cryptomaniaks.com/fr/acheter-bitcoin") 
print ("Navigating to #16 fr-acheter-bitcoin site")
f.write('Navigating to #16 fr-acheter-bitcoin site \n')
#browser.save_screenshot('/Users/scott/Desktop/SCREENSHOTSIMP/ScreenShot18.png')
browser.save_screenshot(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'SCREENSHOTSIMP', 'ScreenShot18.png'))
print ("Capturing screenshot #18")
f.write('Capturing screenshot #18 \n')
#----------------------------------------------------------------------------------------------------
#os.system('curl -Is https://cryptomaniaks.com/fr/acheter-bitcoin| head -1 | awk '{print "fr-acheter-bitcoin site " $2}'')
print ("Return Code https://cryptomaniaks.com/fr/acheter-bitcoin")
os.system('curl -Is https://cryptomaniaks.com/fr/acheter-bitcoin | head -1')
#----------------------------------------------------------------------------------------------------
#-----------------GAMBLING--------------------------------------
browser.get("https://cryptomaniaks.com/gambling#") 
print ("Navigating to CRYPTO GAMBLING site")
f.write('Navigating to CRYPTO GAMBLING site \n')
browser.save_screenshot('/Users/scott/Desktop/SCREENSHOTSIMP/ScreenShot19.png')
print ("Capturing screenshot #15")
f.write('Capturing screenshot #15 \n')
#-----------------------------------------------------------------------------------------------------
#os.system('curl -Is https://cryptomaniaks.com/gambling# | head -1 | awk '{print "gambling " $2}'')
print ("Return Code https://cryptomaniaks.com/gambling#")
os.system('curl -Is https://cryptomaniaks.com/gambling# | head -1')
#----------------------------------------------------------------------------------------------------
#===============================================================
#-----------------TIMING PLUS CLEANUP--------------------------- 
#print("--- %s seconds ---" % (time.time() - start_time))
#print ("The elapsed time is %s" % (time.time() - start_time))
#f.write("--- %s seconds ---" % (time.time() - start_time))
#f.write("The elapsed time is %s" % (time.time() - start_time))
start = timeit.default_timer()
end = timeit.timeit()
#print ("The elapsed time is %s" % (time.time() - start))
#pwd
#---------------------------------------------------------------
print ("CLOSE FILE")
f.write('CLOSE FILE \n')
f.close()
Send_Mail()
browser.quit()
#--------------------------------------------------------------------------------------------------
