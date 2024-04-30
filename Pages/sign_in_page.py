from selenium.webdriver.common.by import By

from pages.base_page import page

class target_tc_link(Page):
    TCLINK = (By.XPATH, "\\a[@href='/c/terms-conditions/-/N-4sr7l']")

    def home_page_for_target(self):
        self.open('https://www.target.com')

    def click_target_tc_link(self):
        self.click(self.TCLINK)

    def verify_on_tc_page(self):
        self.verify_url('https://www.target.com/c/terms-conditions/-/N-4sr7l')
