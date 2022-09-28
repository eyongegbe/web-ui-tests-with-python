
Feature: Search Field
  As A fan
  In order to search for information
  I want to be able to use the search field

  Scenario Outline: Search from home page
    Given  I am on the nba stats page
    When I search for a player "<player>"
    Then I should navigate to the players "<player_name>" page
    Examples:
    |player|player_name|
    |Stephen Curry|Stephen Curry |
    |James Harden |James Harden |
