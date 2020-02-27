Feature: test it
  @test
  Scenario: earn
    Given I have 2 dollars
    When I earn 5 dollars
    Then I should have 7 dollars
