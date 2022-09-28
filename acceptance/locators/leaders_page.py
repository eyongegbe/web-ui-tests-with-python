from selenium.webdriver.common.by import By


class LeadersPageLocators:
    leaders_table = By.CSS_SELECTOR, "div.nba-stat-table > div.nba-stat-table__overflow > table"
    first_row = By.XPATH, "//div[@class='nba-stat-table__overflow']/table/tbody/tr"
    window_back = "window.history.go(-1)"
