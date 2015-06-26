# Created by chaitanyavisa at 25/06/2015
Feature: Amazon search Feature
  In order to ensure Amazon search works I want to run a search for Software Testing

  Scenario: Search for Software Testing
  Given I'm on Amazon Home page
  When I search for Software Testing
  Then the browser title should have software testing

