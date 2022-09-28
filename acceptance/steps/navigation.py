import time

from behave import *
from behave import then
from selenium import webdriver

from acceptance.locators.standings_page import StandingsPageLocators
from acceptance.page_models.base_page import BasePage
from selenium.webdriver.chrome.options import Options
from acceptance.page_models.home_page import HomePage
from acceptance.page_models.leaders_page import LeadersPage
from acceptance.page_models.traditional_player_page import TraditionalPlayerPage

use_step_matcher('re')


@given("I am on the nba stats page")
def step_impl(context):
    context.browser = webdriver.Chrome()
    page = HomePage(context.browser)
    page.driver.get(page.url)
    context.browser.maximize_window()


@given("I am on the players traditional page")
def step_impl(context):
    context.browser = webdriver.Chrome()
    page = TraditionalPlayerPage(context.browser)
    page.driver.get(page.url)
    context.browser.maximize_window()


@given("I am on the leaders page")
def step_impl(context):
    context.browser = webdriver.Chrome()
    page = LeadersPage(context.browser)
    page.driver.get(page.url)
    context.browser.maximize_window()
