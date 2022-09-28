from selenium.webdriver.common.by import By


class HomePageLocators():
    search_box_text = By.CSS_SELECTOR, "span.stats-search__icon-text"
    TITLE = By.TAG_NAME, 'h1'
    standings_menu = By.LINK_TEXT, 'Standings'
