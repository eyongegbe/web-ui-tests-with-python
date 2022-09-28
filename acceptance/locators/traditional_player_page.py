from selenium.webdriver.common.by import By
"""
locators for traditional player page view
"""

class TraditionalPlayerPageLocators:
    advanced_filters = By.LINK_TEXT, "Advanced Filters"
    all_teams_filters = By.XPATH, "*//select[@name='TeamID']"
    opponent_teams_filters = By.XPATH, "*//select[@name='OpponentTeamID']"
    golden_state_warriors = By.XPATH, "*//select[@name='TeamID']/option[text()='Golden State Warriors']"
    houston_rockets = By.XPATH, "*//select[@name='OpponentTeamID']/option[text()='VS Houston Rockets']"
    run_filter_btn = By.CSS_SELECTOR, "a.run-it"
    stats_table = By.CSS_SELECTOR, "div.nba-stat-table__overflow"
    filtered_pills = By.CSS_SELECTOR, "stats - filter - pills > a"
