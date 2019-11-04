from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
import time
import os
import json


class GmailTasks:

    def __init__(self, credentials_json: str):
        self.login = ''
        self.password = ''
        self.load_credentials(credentials_json)

    def auth_user(self):
        auth_driver = webdriver.Chrome(executable_path=os.path.abspath(os.path.join('chromedriver.exe')))
        auth_driver.get('https://www.gmail.com/')
        auth_driver.find_element_by_xpath('//*[@id="identifierId"]').send_keys(self.login)
        auth_driver.find_element_by_xpath('//*[@id="identifierNext"]/span/span').click()
        WebDriverWait(driver=auth_driver, timeout=3).until(
            expected_conditions.presence_of_element_located((By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input')))
        auth_driver.switch_to.window(auth_driver.window_handles[0])
        time.sleep(3)
        auth_driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input').send_keys(self.password)
        WebDriverWait(driver=auth_driver, timeout=3).until(
            expected_conditions.presence_of_element_located((By.XPATH, '//*[@id="passwordNext"]/span/span')))
        auth_driver.find_element_by_xpath('//*[@id="passwordNext"]/span/span').click()
        time.sleep(5)
        auth_driver.close()
        return auth_driver

    def load_credentials(self, credentials_json: str):
        credentials = json.loads(credentials_json)
        if 'login' in credentials:
            self.login = credentials['login']
        if 'password' in credentials:
            self.password = credentials['password']


class Utils:

    def format_json_str(self, json_str):
        credentials_json = json.loads(json_str)
        formated_json = json.dumps(credentials_json, indent=4)
        return formated_json

    def save_str_to_file(self, file_path, content):
        with open(file_path, "w") as credentials_file:
            print(content, file=credentials_file)
