from selenium.webdriver.common.by import By

from page_object.compose_page import ComposePage
from page_object.mail_page import MailPage


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    profile_btn = (By.CSS_SELECTOR, "div[class='gb_ia gb_kg gb_f']")
    id = (By.CSS_SELECTOR, "div[class='DmBVvf ZWVAt']")
    compose_btn = (By.CSS_SELECTOR, "div[class='T-I T-I-KE L3']")
    all_mail_titles = (By.CSS_SELECTOR, "tbody tr td:nth-child(4)")

    def get_profile_btn(self):
        return self.driver.find_element(*HomePage.profile_btn)

    def get_id(self):
        return self.driver.find_element(*HomePage.id)

    def get_compose_btn(self):
        self.driver.find_element(*HomePage.compose_btn).click()
        composepage = ComposePage(self.driver)
        return composepage

    def get_all_mail_titles(self):
        all_mails = self.driver.find_elements(*HomePage.all_mail_titles)
        all_mails[0].click()
        mailpage = MailPage(self.driver)
        return mailpage