from selenium import webdriver
import time

auth_driver = webdriver.Chrome(executable_path='C:/Users/Grinder/PycharmProjects/selenium_tasks/chromedriver.exe')
auth_driver.get('https://www.gmail.com/')
time.sleep(5)
auth_driver.close()