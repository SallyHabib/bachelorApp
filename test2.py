import urllib3
import facebook
import requests
from selenium import webdriver

from getpass import getpass
import json
import urllib
import os

#usr=input('enter your email : ')
#pwd=getpass('enter your pass: ')

FACEBOOK_APP_ID = '188725925227536'

driver = webdriver.Chrome(executable_path=r'C:\Python27\selenium\webdriver\chromedriver_win32\chromedriver')
#driver.get("https://www.facebook.com")
driver.get('https://www.facebook.com/v2.12/dialog/oauth?client_id={}&redirect_uri={}&response_type={}&scope={}'.format(FACEBOOK_APP_ID,'http://localhost:8080/','code','email,publish_actions'))

#user=driver.find_element_by_id('email')
#user.send_keys(usr)

#user=driver.find_element_by_id('pass')
#user.send_keys(pwd)

#login=driver.find_element_by_id('u_0_3')
#login.submit()

# appID="1583861328394595"
# appSecret="b218fd24b40469f2af993d24435eff0d"
access_token="EAACrpS27rBABAANCxwbnJjHw0TZCMQEHsleDumxyXqWj6fKSUqEeAt1xRZClmv1uWWaZCVuY0spD1pOm5i37ccfGTZClsxEcC5U9ZAl0uw2P8CRa46og4PZAOr9j2484xEz3HjMNKZBeoyPRAScgh6JtumhSTgB971jbO7f0fiqDQ6FtzepA790zIy3k5K59oMZD"
#token=os.getenv('FACEBOOK_TEMP_TOKEN')
#print(token)
graph = facebook.GraphAPI(access_token)
profile = graph.get_object("me")
name = profile['name']
#bd= profile['email']
#print(profile.keys)
print(name)
for x in profile.keys():
      print x

