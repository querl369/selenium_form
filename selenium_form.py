# Open https://the-internet.herokuapp.com/login
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
# Please automate next test cases:
# 1. Login with valid creds (tomsmith/SuperSecretPassword!) and assert you successfully logged in
def login():
    driver = webdriver.Chrome()
    driver.get('https://the-internet.herokuapp.com/login')
    username = driver.find_element_by_css_selector('#username')
    username.send_keys('tomsmith')
    password = driver.find_element_by_css_selector('#password')
    password.send_keys('SuperSecretPassword!')
    login_btn = driver.find_element_by_xpath('//*[@id="login"]/button/i')
    login_btn.click()
    assert 'You logged into a secure area!' in driver.page_source
    driver.quit()
# 2. Login with invalid creds and check validation error
def login_wrong():
    driver = webdriver.Chrome()
    driver.get('https://the-internet.herokuapp.com/login')
    username = driver.find_element_by_css_selector('#username')
    username.send_keys('Moysha')
    password = driver.find_element_by_css_selector('#password')
    password.send_keys('SuperSecretPassword!')
    login_btn = driver.find_element_by_xpath('//*[@id="login"]/button/i')
    login_btn.click()
    assert 'Your username is invalid!' in driver.page_source
    sleep(5)
    driver.quit()
# 3. Logout from app and assert you successfully logged out
def logout():
    driver = webdriver.Chrome()
    driver.get('https://the-internet.herokuapp.com/login')
    username = driver.find_element_by_css_selector('#username')
    username.send_keys('tomsmith')
    password = driver.find_element_by_css_selector('#password')
    password.send_keys('SuperSecretPassword!')
    login_btn = driver.find_element_by_xpath('//*[@id="login"]/button/i')
    login_btn.click()
    assert 'You logged into a secure area!' in driver.page_source
    logout_btn = driver.find_element_by_xpath('//*[@id="content"]/div/a/i')
    logout_btn.click()
    assert 'You logged out of the secure area!' in driver.page_source
    driver.quit()

login()
login_wrong()
logout()