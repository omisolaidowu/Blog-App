import pytest
from selenium import webdriver

from django.urls import reverse

# from tests.setup.setup import driver

from tests.setup.setup import testSet

from django.test import LiveServerTestCase


setup = testSet()

# driver = webdriver.Chrome()

# driver.get('https://www.python.org/')

# @pytest.mark.django_db
username = "omisolaidowu"
access_key = "qAsUF6J3KaaU1gdGoCKceZxlLznkxAOpZkbQ7q30bQ9bliH9mc"

class TestUserLoginFormSuccess(LiveServerTestCase):
   # host = "https://localhost.lambdatest.com"
   # host = "192.168.150.1:8080/"
   # host = "https://{}:{}@hub.lambdatest.com/wd/hub".format(username, access_key)
   # port = 8000
   def test_view(self):
      setup.testSetup()

      driver = setup.driver
      driver.implicitly_wait(10)
      driver.get(self.live_server_url+'/login')
      print(driver.title)
      setup.tearDown()
      
      # url = 'https://www.python.org/'
      # response = driver.get(url)
   # assert response.status_code == 200