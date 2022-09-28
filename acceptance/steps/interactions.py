from behave import *
from acceptance.locators.home_page import HomePageLocators
from acceptance.locators.standings_page import StandingsPageLocators
from acceptance.page_models.home_page import HomePage
from acceptance.page_models.leaders_page import LeadersPage
from acceptance.page_models.traditional_player_page import TraditionalPlayerPage

use_step_matcher('re')


@when('I click "Standings" on the menu')
def step_impl(context):
    context.browser.find_element(*HomePageLocators.standings_menu).click()
    eastern_conference = context.browser.find_element(*StandingsPageLocators.eastern_conference)
    eastern_conference.is_displayed()


@when('I click an "(.*)" on the menu')
def step_impl(context, item):
    menu = context.browser.find_element_by_link_text(item)
    menu.is_displayed()
    menu.click()


@when('I filter player stats for "(.*)" and "(.*)"')
def step_impl(context, team_a, team_b):
    page = TraditionalPlayerPage(context.browser)
    page.filter(team_a, team_b)


@when('I search for a player "(.*)"')
def step_impl(context, search_text):
    page = HomePage(context.browser)
    page.search(search_text)


@when("I compare the top (.*) players points, rebounds and assists")
def step_impl(context, number):
    page = LeadersPage(context.browser)
    page.compare_player_records(int(number))
