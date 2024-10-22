Feature: Space Tags Management with Random Data

  Scenario: Fetch space tags
    When I fetch space tags
    Then Check that status code is 200

  Scenario: Create a new space tag with random name
    When I create a space tag with random name
    Then Check that status code is 200
    When I fetch space tags
    Then Check that status code is 200
    And the response should contain the created random tag for space

  Scenario: Edit an existing space tag with random name
    When I create a space tag with random name
    And I edit the space tag with random new name
    Then Check that status code is 200
    When I fetch space tags
    Then Check that status code is 200
    And the response should contain the updated random tag for space

  Scenario: Delete a space tag
    When I create a space tag with random name
    And I delete the space tag
    Then Check that status code is 200
    When I fetch space tags
    Then Check that status code is 200
    And the response should not contain the deleted tag for space

  @wip
  Scenario Outline: Create space tag from file
    When Create a space tag form file <file>
    Then Check that status code is <status>
    When I fetch space tags
    Then Check that status code is 200
    And the response should contain the created random tag for space
    Examples:
      | file                      |  status  |
      | create_tag.json           |   200    |
      | create_invalid_tag.json   |   400    |
