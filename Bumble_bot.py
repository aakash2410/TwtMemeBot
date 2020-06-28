from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time
import os
import random

chrome_options = Options()
chrome_options.add_argument("-incognito")
browser = webdriver.Chrome(options=chrome_options)
url = 'https://bumble.com/'
browser.get(url)
SignInButton = browser.find_element_by_link_text('Sign In')
SignInButton.click()
time.sleep(3)
NumberLogin = browser.find_element_by_class_name('button.button--narrow.button--size-m.color-primary.button--transparent')
NumberLogin.click()
Number = os.environ.get('MyNumber')
Password = os.environ.get('MyPassword')
Number_block = browser.find_element_by_id('phone')
Number_block.click()
time.sleep(3)
Number_block.send_keys(Number)
Number_block.send_keys(Keys.RETURN)
time.sleep(3)
Password_block = browser.find_element_by_id('pass')
Password_block.click()
Password_block.send_keys(Password)
Password_block.send_keys(Keys.RETURN)
time.sleep(7)
LikeButton = browser.find_element_by_css_selector('div.encounters-action.tooltip-activator.encounters-action--like')
DislikeButton = browser.find_element_by_css_selector('div.encounters-action.tooltip-activator.encounters-action--dislike')


def RightSwiping():
    LikeButton.click()
    time.sleep(random.randint(3,5))


def LeftSwiping():
    DislikeButton.click()
    time.sleep(random.randint(3, 8))


def SwipeBot():
    while True:
        try:
            RightSwiping()
        except:
            browser.close()


SwipeBot()
browser.close()
