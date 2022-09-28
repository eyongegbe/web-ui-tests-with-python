from selenium.webdriver.common.by import By


class PlayerPageLocators():
    player_first_name = By.CSS_SELECTOR, "p.player-summary__first-name"
    player_second_name = By.CSS_SELECTOR, "p.player-summary__last-name"
