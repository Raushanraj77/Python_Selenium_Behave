Feature: Searching google with Selenium

  Scenario: user searching google
     Given that user is in Google
      When user types 'Selenium'
      Then results should have selenium HQ page