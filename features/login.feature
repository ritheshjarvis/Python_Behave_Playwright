Feature: Login Functionality
  As a user,
  I want to log into the application
  So that I can access my account.

  Scenario: Successful login with valid credentials
    Given I am on the login page
    When I enter "standard_user" as username and "secret_sauce" as password
    And I click the login button
    Then I should see the dashboard
    When I clicked on the Add to cart button
    Then I clicked on the Shopping cart badge icon
    When I clicked on the Checkout button
    Then 'Chekout: Your Information' page is displayed
    When I enter 'First Name' as "Rithesh"
    And I enter 'Last Name' as "B Rao"
    And I enter 'Zip Postal Code' as "575007"
    And I clicks 'Continue' button
    And I clicks 'Finish' button
    Then 'Thank you for your order!' message is displayed
