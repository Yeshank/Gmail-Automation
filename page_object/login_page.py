from selenium.webdriver.common.by import By

from page_object.home_page import HomePage


class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    mailid_inpt = (By.XPATH, "//*[@id='identifierId']")
    id_nxt_btn = (By.XPATH, "//*[@id='identifierNext']/div/button/span")
    pass_inpt = (By.XPATH, "//*[@id='password']/div[1]/div/div[1]/input")
    pass_nxt_btn = (By.CSS_SELECTOR,
                    "button[class='VfPpkd-LgbsSe VfPpkd-LgbsSe-OWXEXe-k8QpJ VfPpkd-LgbsSe-OWXEXe-dgl2Hf nCP5yc AjY5Oe DuMIQc qfvgSe qIypjc TrZEUc lw1w4b']")

    def get_mailid_inpt(self):
        return self.driver.find_element(*LoginPage.mailid_inpt)

    def get_id_nxt_btn(self):
        return self.driver.find_element(*LoginPage.id_nxt_btn)

    def get_pass_inpt(self):
        return self.driver.find_element(*LoginPage.pass_inpt)

    def get_pass_nxt_btn(self):
        self.driver.find_element(*LoginPage.pass_nxt_btn).click()
        return HomePage(self.driver)
