Feature: Search

  Scenario: Search PyPI
    Given I navigate to the PyPi Home page
    When I search for "Selenium"
    Then I am taken to the PyPi Search Results page

