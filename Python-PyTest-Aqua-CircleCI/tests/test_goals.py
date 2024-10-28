import pytest
from faker import Faker
from pytest_steps import test_steps

from helpers.goals_methods import create_goal, get_goal, update_goal, delete_goal, create_key_result, edit_key_result, \
    delete_key_result, get_goals
from fixtures.fixtures import headers, base_url, create_goal_data, create_key_result_data

fake = Faker()

class TestGoalsAPI:

    @staticmethod
    def _setup_goal(base_url, headers, create_goal_data):
        response, created_data = create_goal(base_url, headers, create_goal_data)
        assert response.status_code == 200, f"Failed to create goal, response: {response.text}"
        goal_id = response.json().get('goal', {}).get('id')
        assert goal_id is not None, "Goal ID should be present"
        return goal_id, created_data

    @staticmethod
    def _setup_key_result(base_url, headers, goal_id, create_key_result_data):
        key_result_response, key_result_data = create_key_result(base_url, headers, goal_id, create_key_result_data)
        assert key_result_response.status_code == 200, f"Failed to create key result, response: {key_result_response.text}"
        key_result_id = key_result_response.json().get('key_result', {}).get('id')
        assert key_result_id is not None, "Key Result ID should be present"
        return key_result_id, key_result_data

    @test_steps('Get all goals')
    def test_get_goals(self, headers, base_url):
        response = get_goals(base_url, headers)
        assert response.status_code == 200, f"Failed to get goals, response: {response.text}"
        assert 'goals' in response.json(), "Response should contain 'goals' key"
        yield

    @test_steps('Create a new goal')
    def test_create_goal(self, create_goal_data, headers, base_url):
        goal_id, created_data = self._setup_goal(base_url, headers, create_goal_data)
        print(f"Created goal ID: {goal_id}")
        yield

    @test_steps('Create a new goal', 'Check new goal by goal_id')
    def test_get_goal(self, create_goal_data, headers, base_url):
        goal_id, created_data = self._setup_goal(base_url, headers, create_goal_data)
        print(f"Created goal ID: {goal_id}")
        yield
        get_response = get_goal(base_url, headers, goal_id)
        assert get_response.status_code == 200, f"Failed to fetch created goal, response: {get_response.text}"
        goal = get_response.json().get('goal', {})
        assert goal.get('name') == created_data['name'], "Goal name doesn't match"
        assert goal.get('description') == created_data['description'], "Goal description doesn't match"
        assert goal.get('color') == created_data['color'], "Goal color doesn't match"
        assert str(goal.get('due_date')) == str(created_data['due_date']), "Goal due date doesn't match"
        yield

    @test_steps('Create a new goal', 'Update goal by goal_id', 'Check updated goal by goal_id')
    def test_update_goal(self, create_goal_data, headers, base_url):
        goal_id, created_data = self._setup_goal(base_url, headers, create_goal_data)
        yield
        update_response, updated_data = update_goal(base_url, headers, goal_id)
        assert update_response.status_code == 200, f"Failed to update goal, response: {update_response.text}"
        yield
        get_response = get_goal(base_url, headers, goal_id)
        goal = get_response.json().get('goal', {})
        assert goal.get('name') == updated_data['name'], "Updated goal name doesn't match"
        assert goal.get('description') == updated_data['description'], "Updated goal description doesn't match"
        yield

    @test_steps('Create a new goal', 'Delete goal by goal_id', 'Check deleted goal by goal_id', 'Try to delete again deleted goal by goal_id')
    def test_delete_goal(self, create_goal_data, headers, base_url):
        goal_id, created_data = self._setup_goal(base_url, headers, create_goal_data)
        yield
        delete_response = delete_goal(base_url, headers, goal_id)
        assert delete_response.status_code == 200, f"Failed to delete goal, response: {delete_response.text}"
        yield
        get_response = get_goal(base_url, headers, goal_id)
        assert get_response.status_code in [404, 403], "Deleted goal should not be found"
        yield
        delete_again_response = delete_goal(base_url, headers, goal_id)
        assert delete_again_response.status_code == 404, f"Expected 404 for deleting already deleted goal, got: {delete_again_response.status_code}"
        yield

    @test_steps('Create a new goal', 'Create a new key result by goal_id', 'Check created key result by name')
    def test_create_key_result(self, create_goal_data, create_key_result_data, headers, base_url):
        goal_id, created_data = self._setup_goal(base_url, headers, create_goal_data)
        yield
        key_result_id, key_result_data = self._setup_key_result(base_url, headers, goal_id, create_key_result_data)
        yield
        get_response = get_goal(base_url, headers, goal_id)
        goal = get_response.json().get('goal', {})
        key_result = next((kr for kr in goal.get('key_results', []) if kr['id'] == key_result_id), None)
        assert key_result is not None, "Key result should be present"
        assert key_result['name'] == key_result_data['name'], "Key result name doesn't match"
        yield

    @test_steps('Create a new goal', 'Create a new key result by goal_id', 'Update key result by key_result_id', 'Check updated key result by name')
    def test_edit_key_result(self, create_goal_data, create_key_result_data, headers, base_url):
        goal_id, created_data = self._setup_goal(base_url, headers, create_goal_data)
        yield
        key_result_id, key_result_data = self._setup_key_result(base_url, headers, goal_id, create_key_result_data)
        yield
        edit_response, updated_data = edit_key_result(base_url, headers, key_result_id)
        assert edit_response.status_code == 200, f"Failed to edit key result, response: {edit_response.text}"
        yield
        get_response = get_goal(base_url, headers, goal_id)
        updated_key_result = next((kr for kr in get_response.json().get('goal', {}).get('key_results', []) if kr['id'] == key_result_id), None)
        assert updated_key_result is not None, "Updated key result should be present"
        assert updated_key_result['name'] == updated_data['name'], "Updated key result name doesn't match"
        yield

    @test_steps('Create a new goal', 'Create a new key result by goal_id', 'Delete key result by key_result_id', 'Try to delete again deleted key result by key_result_id')
    def test_delete_key_result(self, create_goal_data, create_key_result_data, headers, base_url):
        goal_id, created_data = self._setup_goal(base_url, headers, create_goal_data)
        yield
        key_result_id, key_result_data = self._setup_key_result(base_url, headers, goal_id, create_key_result_data)
        yield
        delete_response = delete_key_result(base_url, headers, key_result_id)
        assert delete_response.status_code == 200, f"Failed to delete key result, response: {delete_response.text}"
        yield
        get_response = get_goal(base_url, headers, goal_id)
        deleted_key_result = next((kr for kr in get_response.json().get('goal', {}).get('key_results', []) if kr['id'] == key_result_id), None)
        assert deleted_key_result is None, "Deleted key result should not be present"
        yield
        delete_again_response = delete_key_result(base_url, headers, key_result_id)
        assert delete_again_response.status_code == 404, f"Expected 404 for deleting already deleted key result, got: {delete_again_response.status_code}"
        yield