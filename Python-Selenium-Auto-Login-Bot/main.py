# Used to import the webdriver from selenium
from selenium import webdriver
import os
import time

def startBot(username, password, url):
    # Provide the full path of chromedriver
    path = "C:\\Users\\hp\\Downloads\\chromedriver.exe"

    # Giving the path of chromedriver to selenium webdriver
    driver = webdriver.Chrome(path)

    # Opening the website in chrome
    driver.get(url)
    time.sleep(2)

    # Find username field and enter username
    driver.find_element_by_name(
        "id/class/name of username").send_keys(username)

    # Find password field and enter password
    driver.find_element_by_name(
        "id/class/name of password").send_keys(password)

    # Click on login button
    driver.find_element_by_css_selector(
        "id/class/name/css selector of login button").click()


# ---------------- Driver Code ---------------- #

# Enter your login credentials
username = "Enter your username"
password = "Enter your password"

# URL of the login page
url = "Enter the URL of login page of website"

# Call the function
startBot(username, password, url)