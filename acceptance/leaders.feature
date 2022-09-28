
Feature: Leaders
  As a fan
  In order to view best performing players of the season
  I want to interact with the leaders page

  Scenario: view top three performances information
    Given I am on the leaders page
    When I compare the top 3 players points, rebounds and assists
    Then these stats should match what is on their personal player page