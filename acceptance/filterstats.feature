
Feature: StatsFilters
  In order to compare stats of players
  As A fan
  I want to interact with the advanced filter functions

  Scenario: Average points per game for two teams
    Given I am on the players traditional page
    When I filter player stats for "Atlanta Hawks" and "VS Denver Nuggets"
    Then I should see a stats table filtered by "ATLANTA HAWKS" and "VS DENVER NUGGETS"

  Scenario Outline:
    Given I am on the players traditional page
    When I filter player stats for "<team_a>" and "<team_b>"
    Then I should see a stats table filtered by "<result_a>" and "<result_b>"
    Examples:
    |team_a|team_b|result_a|result_b|
    |Atlanta Hawks|VS Denver Nuggets|ATLANTA HAWKS|VS DENVER NUGGETS|
    |Boston Celtics|VS Golden State Warriors|BOSTON CELTICS|VS GOLDEN STATE WARRIORS|
