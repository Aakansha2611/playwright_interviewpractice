Feature: OrderTransaction
  Test related to order transaction

  Scenario Outline: Verify order success details shown in message page
    Given place the order with <username> and <password>
    And user is on landing page
    When I login to portal with <username> and <password>
    And navigate to order page
    And select the order
    Then order message is successfully displayed

    Examples:
      | username                   | password |
      | akanshasoni.2611@gmail.com | Anu@2611 |
