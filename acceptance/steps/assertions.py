import time
from behave import *
from acceptance.locators.standings_page import StandingsPageLocators
from acceptance.page_models.leaders_page import LeadersPage
from acceptance.page_models.player_page import PlayerPage
from acceptance.page_models.traditional_player_page import TraditionalPlayerPage

use_step_matcher('re')


@then("I should overall information for all teams in the current regular season")
def step_impl(context):
    time.sleep(3)
    ec_teams = context.browser.find_elements(*StandingsPageLocators.eastern_teams)
    assert isinstance(ec_teams, list)


@then('I should navigate to the correct page "(.*)"')
def step_impl(context, url):
    expected_url = url
    actual_url = context.browser.current_url
    assert expected_url == actual_url
    context.browser.quit()


@then('I should see a stats table filtered by "(.*)" and "(.*)"')
def step_impl(context, team_a, team_b):
    page = TraditionalPlayerPage(context.browser)
    pill1 = page.filtered_pills[0]
    pill2 = page.filtered_pills[1]
    assert pill1.text == team_a
    assert pill2.text == team_b
    context.browser.quit()


@then('I should navigate to the players "(.*)" page')
def step_impl(context, player_name):
    page = PlayerPage(context.browser)
    first_name = page.player_first_name
    last_name = page.player_last_name
    full_name = first_name.text + " " + last_name.text
    assert full_name == player_name
    page.driver.quit()


@then("these stats should match what is on their personal player page")
def step_impl(context):
    a = context.browser.leaders_data
    b = context.browser.players_data
    assert a == b
