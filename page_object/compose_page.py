from selenium.webdriver.common.by import By

from page_object.sent_page import SentPage


class ComposePage:

    def __init__(self, driver):
        self.driver =  driver

    to_inpt = (By.CSS_SELECTOR, "div[class='wO nr l1'] textarea")
    subject_inpt = (By.CSS_SELECTOR, "input[class='aoT']")
    body_inpt = (By.CSS_SELECTOR, "div[class='Am Al editable LW-avf tS-tW']")
    send_btn = (By.CSS_SELECTOR, "div[class='T-I J-J5-Ji aoO v7 T-I-atl L3']")

    def get_to_inpt(self):
        return self.driver.find_element(*ComposePage.to_inpt)

    def get_subject_inpt(self):
        return self.driver.find_element(*ComposePage.subject_inpt)

    def get_body_inpt(self):
        return self.driver.find_element(*ComposePage.body_inpt)

    def get_send_btn(self):
        self.driver.find_element(*ComposePage.send_btn).click()
        sentpage = SentPage(self.driver)
        return sentpage