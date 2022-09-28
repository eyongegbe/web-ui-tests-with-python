Feature: Stats Page
  As a fan
  In order to check my team's performance
  I want to view stats on the NBA stats pages

  Scenario: Can navigate to standings page
    Given I am on the nba stats page
    When I click "Standings" on the menu
    Then I should overall information for all teams in the current regular season


  Scenario Outline: Navigate stats homepage menus
    Given  I am on the nba stats page
    When I click an "<item>" on the menu
    Then I should navigate to the correct page "<url>"
    Examples:
      | item | url |
      |Schedule|https://stats.nba.com/schedule/|
      |Teams    |https://stats.nba.com/teams/   |
      |Players |https://stats.nba.com/players/ |

