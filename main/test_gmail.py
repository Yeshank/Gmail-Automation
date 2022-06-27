import time

from selenium.webdriver.common.by import By

from page_object.compose_page import ComposePage
from page_object.home_page import HomePage
from page_object.login_page import LoginPage
from page_object.mail_page import MailPage
from page_object.sent_page import SentPage
from utitlities.Base_class import BaseClass


class TestMain(BaseClass):

    def test_gmail(self):
        # Code from Implicit wait of 5 second
        self.driver.implicitly_wait(10)

        loginpage = LoginPage(self.driver)

        # Entering the MailId
        loginpage.get_mailid_inpt().send_keys('xyz@gmail.com')

        # click on next button
        loginpage.get_id_nxt_btn().click()

        time.sleep(2)  # Mandatory

        # Entering the password
        loginpage.get_pass_inpt().send_keys('sjcnjn#214545')

        # click on next button
        homepage = loginpage.get_pass_nxt_btn()

        # click on profile button
        self.element_wait_presence(HomePage.profile_btn)
        homepage.get_profile_btn().click()

        # Switching to frame to get the loggined ID
        self.driver.switch_to.frame('account')
        self.element_wait_presence(HomePage.id)
        assert homepage.get_id().text == 'xyz@gmail.com'
        self.driver.switch_to.default_content()

        # clicking on Compose button and getting the object of ComposePage class
        self.element_wait_clickable(HomePage.compose_btn)
        composepage = homepage.get_compose_btn()

        # Sending input to To field
        self.element_wait_presence(ComposePage.to_inpt)
        composepage.get_to_inpt().send_keys('xyz@gmail.com')

        # Sending input to Subject_field
        self.element_wait_presence(ComposePage.subject_inpt)
        composepage.get_subject_inpt().send_keys('Gmail Automation using pytest')

        # sending input to body field
        self.element_wait_presence(ComposePage.body_inpt)
        for i in range(0, 50):
            composepage.get_body_inpt().send_keys('Hello World\n')

        # Clicking on send Button
        self.element_wait_clickable(ComposePage.send_btn)
        sentpage = composepage.get_send_btn()

        # Waiting to send the message
        time.sleep(5)

        # Clicking on sent Option
        self.element_wait_clickable(SentPage.sent_btn)
        sentpage.get_sent_btn().click()

        # Getting all the mails of sent page
        self.element_wait_presence(SentPage.sent_mails)
        sent_mails = sentpage.get_sent_mails()
        time.sleep(2)  # Mandatory
        self.element_wait_presence(SentPage.sent_mails)
        time.sleep(2)
        # Clicking on the sent mail
        sent_mails[0].click()


        self.driver.get_screenshot_as_file('SentMailScreenshot.png')
        time.sleep(2) # waiting to take screen shot

        # Clicking on the inbox option
        self.element_wait_clickable(SentPage.inbox_btn)
        sentpage.get_inbox_btn().click()

        # Getting all the inbox messages
        self.element_wait_presence(HomePage.all_mail_titles)
        mailpage = homepage.get_all_mail_titles()

        # getting the title of recieved mail
        self.element_wait_presence(MailPage.rec_mail_title)
        rec_mail_title = mailpage.get_rec_mail_title().text

        print(rec_mail_title)

        # Checking that athe sent mail and recived mail is same or not
        assert rec_mail_title == 'Gmail Automation using pytest'

        # Clicking on More Option
        self.element_wait_clickable(MailPage.more_option_btn)
        mailpage.get_more_option_btn().click()

        # Clicking on reply option
        self.element_wait_clickable(MailPage.reply_option)
        mailpage.get_reply_option().click()

        # Clicking on prompt cancel button
        self.element_wait_clickable(MailPage.prompt_cancel_btn)
        mailpage.get_prompt_cancel_btn().click()

        # Clicking on Discard button
        self.element_wait_clickable(MailPage.discard_btn)
        mailpage.get_discard_btn().click()

        # Clicking on profile button to signout
        self.element_wait_clickable(HomePage.profile_btn)
        homepage.get_profile_btn().click()

        # Clicking on signout button
        self.driver.switch_to.frame('account')
        self.element_wait_clickable(MailPage.sign_out_btn)
        googlepage = mailpage.get_sign_out_btn()
        self.driver.switch_to.default_content()

        # Going to Google.com website
        self.driver.get('https://www.google.com/')

        # Getting the signin text from that page
        sign_in_text = googlepage.get_sign_out_option_text().text
        # Checking that the sent option is available or not
        assert sign_in_text == 'Sign in'


        print(" Successfull   ")