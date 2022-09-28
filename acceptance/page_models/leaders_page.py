import time

from selenium.webdriver.common.by import By

from acceptance.page_models.base_page import BasePage
from acceptance.locators.leaders_page import LeadersPageLocators


class LeadersPage(BasePage):
    @property
    def url(self):
        return super(LeadersPage, self).url + '/leaders'

    @property
    def get_first_row(self):
        return self.driver.find_element(*LeadersPageLocators.first_row)

    @property
    def get_first_row(self):
        return self.driver.find_element(*LeadersPageLocators.windows_back)

    def compare_player_records(self, number):
        # create emptylist
        self.driver.leaders_data = []
        # get rows in table
        table = self.driver.find_element(*LeadersPageLocators.leaders_table)
        t_body = table.find_element(By.TAG_NAME, "tbody")

        rows = t_body.find_elements(By.TAG_NAME, "tr")
        for row in rows:
            player = row.find_elements(By.TAG_NAME, "td")[1]
            points = row.find_elements(By.TAG_NAME, "td")[4]
            assists = row.find_elements(By.TAG_NAME, "td")[16]
            rebounds = row.find_elements(By.TAG_NAME, "td")[17]

            # add each player and details ( points, assists and rebounds) into a tuple and then add to list
            data = (player.text, points.text, assists.text, rebounds.text)
            while len(self.driver.leaders_data) < number:
                self.driver.leaders_data.append(data)
                break

        # getting records of player and details( points, assists and rebounds) from their page
        # into tuple and then list
        self.driver.players_data = []
        for leader in self.driver.leaders_data:
            link_text = leader[0]
            player = self.driver.find_element_by_link_text(link_text)
            page_link = player.get_attribute('href')
            self.driver.get(page_link)
            time.sleep(2)

            first_row = self.driver.find_element(By.XPATH, "//div[@class='nba-stat-table__overflow']/table/tbody/tr")
            first_row.is_displayed()
            name = leader[0]
            page_pts = first_row.find_elements(By.TAG_NAME, "td")[3]
            page_assists = first_row.find_elements(By.TAG_NAME, "td")[15]
            page_rebounds = first_row.find_elements(By.TAG_NAME, "td")[16]
            p_page_info = (name, page_pts.text, page_rebounds.text, page_assists.text)
            self.driver.players_data.append(p_page_info)
            self.driver.execute_script("window.history.go(-1)")
            time.sleep(1)
