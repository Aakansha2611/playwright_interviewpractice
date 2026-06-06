Feature: Order transaction
  Test related to same

  Scenario: Verify order success is shown in page
    Given place the order with username and password
    And the user is on landing page
    When I login to portal with username and password
    And navigate to order page
    Then order message is displayed
