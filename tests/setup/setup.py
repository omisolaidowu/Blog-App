from selenium import webdriver
import pytest


# @pytest.fixture(scope="module")
# def driver():
#     driver = webdriver.Chrome()
#     yield driver
#     driver.implicitly_wait('20')
#     driver.quit()

from selenium import webdriver

from dotenv import load_dotenv
import os
load_dotenv('.env')

username = "omisolaidowu"
access_key = "qAsUF6J3KaaU1gdGoCKceZxlLznkxAOpZkbQ7q30bQ9bliH9mc"

desired_caps = {
		'LT:Options' : {
			"user" : username,
			"accessKey" : access_key,
			"build" : "Django Functional Testing",
			"name" : "Django Test",
			"platformName" : "Windows 10",
            "tunnel": True

		},
		"browserName" : "FireFox",
		"browserVersion" : "103.0",
        
	}
gridURL = "https://{}:{}@hub.lambdatest.com/wd/hub".format(username, access_key)

class testSet: 
       
    def __init__(self) -> None:
        self.driver = webdriver.Remote(command_executor=gridURL, desired_capabilities= desired_caps)
        # self.driver = webdriver.Chrome()
        
    def testSetup(self):
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
    def tearDown(self):
        if (self.driver != None):
            print("Cleaning the test environment")
            self.driver.quit()