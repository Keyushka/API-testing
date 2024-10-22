Feature: Task Tags Management with Known Values

  Scenario: Add a random tag to task
    When I add tag with random name to task
    Then Check that status code is 200
    When I fetch task details
    Then Check that status code is 200
    And the response should contain the random tag for task

  Scenario: Remove a random tag from task
    When I remove tag with random name from task
    Then Check that status code is 200
    When I fetch task details
    Then Check that status code is 200
    And the response should not contain the deleted tag for space random tag for task
