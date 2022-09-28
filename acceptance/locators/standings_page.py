from selenium.webdriver.common.by import By

"""
locators for standings page stored here
"""


class StandingsPageLocators:
    eastern_conference = By.XPATH, "*//table[@class='conference east']"
    eastern_teams = By.XPATH, "*//table[@class='conference east']/tbody/tr/th/a/span"
