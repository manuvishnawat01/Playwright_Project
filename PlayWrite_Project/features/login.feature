Feature: User Login Functionality

  Scenario Outline: Verify login with multiple valid user credentials
    Given I launch the login page
    When I login with email "<email>" and password "<password>"
    Then I should see the logged in user indicator
    And I logout from the application

    Examples:
      | email                         | password    |
      | user1_playwright@example.com  | password123 |
      | user2_playwright@example.com  | password123 |
      | user3_playwright@example.com  | password123 |
