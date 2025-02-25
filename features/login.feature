Feature: Login Functionality
  As a user,
  I want to log into the application
  So that I can access my account.

  Scenario: Successful login with valid credentials
    Given I am on the login page
    When I enter "standard_user" as username and "secret_sauce" as password
    And I click the login button
    Then I should see the dashboard