from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
import time
import os
import json


class SearchServices:

    def __init__(self, user_login, user_password):
        self.login = user_login
        self.password = user_password
        self.user_driver = webdriver.Chrome(executable_path=os.path.abspath(os.path.join('chromedriver.exe')))

    def auth_user(self):
        self.user_driver.get('https://pay.kvartplata.ru/pk/login.action')
        self.user_driver.find_element_by_xpath('//*[@id="userName"]').send_keys(self.login)
        self.user_driver.find_element_by_xpath('//*[@id="userPass"]').send_keys(self.password)
        self.user_driver.find_element_by_xpath('//*[@id="submitButton"]').click()

    def close_browser(self):
        self.user_driver.close()

    def search_transliteration(self, srv_name):
        self.auth_user()
        self.user_driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[2]/a[2]/div[2]/span').click()
        self.user_driver.find_element_by_xpath('//*[@id="srvName"]').send_keys(srv_name)
        self.user_driver.find_element_by_xpath('//*[@id="findForm"]/div/div[2]/table/tbody/tr[3]/td/a[2]').click()
        time.sleep(5)

    def search_for_name(self, srv_name):
        self.auth_user()
        self.user_driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[2]/a[2]/div[2]/span').click()
        self.user_driver.find_element_by_xpath('//*[@id="srvName"]').send_keys(srv_name)
        self.user_driver.find_element_by_xpath('//*[@id="findForm"]/div/div[2]/table/tbody/tr[3]/td/a[2]').click()
        time.sleep(5)

    def search_spam(self, city, street, house, num):
        self.auth_user()
        self.user_driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[2]/a[2]/div[2]/span').click()
        self.user_driver.find_element_by_xpath('//*[@id="findForm"]/div/div[1]/div[2]/h2').click()
        self.user_driver.find_element_by_xpath('//*[@id="cityName"]').send_keys(city)
        self.user_driver.find_element_by_xpath('//*[@id="streetName"]').send_keys(street)
        self.user_driver.find_element_by_xpath('//*[@id="house"]').send_keys(house)
        self.user_driver.find_element_by_xpath('//*[@id="apartment"]').send_keys(num)
        self.user_driver.find_element_by_xpath('//*[@id="findForm"]/div/div[2]/table/tbody/tr[3]/td/a[2]').click()
        time.sleep(5)

    def search_connection_serv(self, srv_name, acc, payment):
        self.auth_user()
        self.user_driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[2]/a[2]/div[2]/span').click()
        self.user_driver.find_element_by_xpath('//*[@id="srvType"]').click()
        self.user_driver.find_element_by_xpath('//*[@id="srvType"]/option[17]').click()
        self.user_driver.find_element_by_xpath('//*[@id="srvName"]').send_keys(srv_name)
        self.user_driver.find_element_by_xpath('//*[@id="findForm"]/div/div[2]/table/tbody/tr[3]/td/a[2]').click()
        self.user_driver.switch_to.frame(self.user_driver.find_element_by_class_name('fancybox-iframe'))
        self.user_driver.find_element_by_xpath('//*[@id="ACCOUNT"]').send_keys(acc)
        self.user_driver.find_element_by_xpath('//*[@id="orderSum"]').click()
        self.user_driver.find_element_by_xpath('//*[@id="orderSum"]').send_keys(payment)
        self.user_driver.find_element_by_xpath('//*[@id="saveTemplate"]').is_selected()
        self.user_driver.find_element_by_xpath('//*[@id="_nextBtn"]').click()
        WebDriverWait(self.user_driver, 5).until(
            expected_conditions.element_to_be_clickable((By.XPATH, '//*[@id="_basketBtn"]')))
        self.user_driver.find_element_by_xpath('//*[@id="_basketBtn"]').click()

    def search_serv_from_dropdown_list(self, srv_name, acc, payment):
        self.auth_user()
        self.user_driver.find_element_by_c('/html/body/div[1]/div[3]/div[2]/a[2]/div[2]/span').click()
        self.user_driver.find_element_by_xpath('//*[@id="srvType"]').click()
        self.user_driver.find_element_by_xpath('//*[@id="srvType"]/option[1]').click()
        self.user_driver.find_element_by_xpath('//*[@id="srvName"]').send_keys(srv_name)
        self.user_driver.find_element_by_xpath('//*[@id="ui-id-437"]').click()
        self.user_driver.find_element_by_xpath('//*[@id="ACCOUNT"]').send_keys(acc)
        self.user_driver.find_element_by_xpath('//*[@id="_nextBtn"]').click()
