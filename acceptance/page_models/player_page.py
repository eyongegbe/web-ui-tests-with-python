from acceptance.locators.player_page import PlayerPageLocators
from acceptance.page_models.base_page import BasePage




class PlayerPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @property
    def player_first_name(self):
        return self.driver.find_element(*PlayerPageLocators.player_first_name)

    @property
    def player_last_name(self):
        return self.driver.find_element(*PlayerPageLocators.player_second_name)