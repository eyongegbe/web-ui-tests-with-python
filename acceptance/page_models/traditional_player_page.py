import time

from acceptance.locators.traditional_player_page import TraditionalPlayerPageLocators
from acceptance.page_models.base_page import BasePage


class TraditionalPlayerPage(BasePage):
    @property
    def url(self):
        return super(TraditionalPlayerPage, self).url + '/players/traditional/'

    @property
    def advanced_filters(self):
        return self.driver.find_element(*TraditionalPlayerPageLocators.advanced_filters)

    @property
    def all_team_filters(self):
        return self.driver.find_element(*TraditionalPlayerPageLocators.all_teams_filters)

    @property
    def run_filter_btn(self):
        return self.driver.find_element(*TraditionalPlayerPageLocators.run_filter_btn)

    @property
    def select_GSW(self):
        return self.driver.find_element(*TraditionalPlayerPageLocators.golden_state_warriors)

    @property
    def select_houston_rockets(self):
        return self.driver.find_element(*TraditionalPlayerPageLocators.houston_rockets)

    @property
    def stats_table(self):
        return self.driver.find_element(*TraditionalPlayerPageLocators.stats_table)

    @property
    def opponent_teams_filter(self):
        return self.driver.find_element(*TraditionalPlayerPageLocators.opponent_teams_filters)

    @property
    def filtered_pills(self):
        return self.driver.find_elements_by_css_selector("stats-filter-pills > a")

    def filter(self, team_a, team_b):
        a_filters = self.advanced_filters
        a_filters.is_enabled()
        a_filters.click()

        # selecting the first team
        all_teams = self.all_team_filters
        all_teams.click()
        first_team = f"*//select[@name='TeamID']/option[text()='{team_a}']"
        gsw = self.driver.find_element_by_xpath(first_team)
        gsw.click()
        time.sleep(5)

        # selecting the second team
        opponent_filter = self.opponent_teams_filter
        opponent_filter.click()
        second_team = f"*//select[@name='OpponentTeamID']/option[text()='{team_b}']"
        houston = self.driver.find_element_by_xpath(second_team)
        houston.click()
        time.sleep(5)
        self.run_filter_btn.click()
