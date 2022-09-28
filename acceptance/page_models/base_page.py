from acceptance.locators.base_page import BasePageLocators


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @property
    def url(self):
        return 'https://stats.nba.com'

    @property
    def title(self):
        return self.find_element(*BasePageLocators.TITLE)

    @property
    def search_text_field(self):
        return self.find_element(BasePageLocators.search_field)

    @property
    def find_element(self, by, value):
        return self.driver.find_element(by, value)

