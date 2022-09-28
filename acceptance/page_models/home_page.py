from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from acceptance.locators.base_page import BasePageLocators
from acceptance.locators.home_page import HomePageLocators
from acceptance.page_models.base_page import BasePage


class HomePage(BasePage):
    @property
    def url(self):
        return super(HomePage, self).url+'/'

    @property
    def click_standings_menu(self):
        return self.driver.find_element(*HomePageLocators.standings_menu)

    def search(self, search_text):
        try:
            ele = self.driver.find_element(*HomePageLocators.search_box_text)
            ele.click()
            wait = WebDriverWait(self.driver, 10)
            element = wait.until(EC.presence_of_element_located(BasePageLocators.search_field))
            element.send_keys(search_text)
            search = self.driver.find_element(By.LINK_TEXT, search_text)
            search.click()
        except TimeoutException:
            print("Loading took too much time!")




