from selenium.webdriver.common.by import By


class BasePageLocators:
    TITLE = By.TAG_NAME, "h1"
    search_field = (By.XPATH, "//input[@ng-model='search']")