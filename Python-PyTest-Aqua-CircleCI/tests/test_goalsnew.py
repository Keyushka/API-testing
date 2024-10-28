# import pytest
# from faker import Faker
# from pytest_steps import test_steps
# from helpers.goals_methods import create_goal, get_goal, update_goal, delete_goal, create_key_result, edit_key_result, delete_key_result
# from fixtures.fixtures import headers, base_url, create_goal_data, create_key_result_data
#
# # Створюємо інстанс Faker
# fake = Faker()
#
# # Основний клас для тестування
# class TestGoalsAPI:
#
#     # @test_steps('Create a new goal', 'Validate goal creation')
#     def test_create_goal(self, create_goal_data, headers, base_url):
#         # Крок 1: створюємо нову ціль
#         response = create_goal(base_url, headers, create_goal_data)
#         assert response.status_code == 200, f"Failed to create goal, response: {response.text}"
#         goal_id = response.json().get('goal', {}).get('id')
#         assert goal_id is not None, "Goal ID should be present"
#         print(f"Created goal ID: {goal_id}")
#         # yield  # Переходимо до наступного кроку
#
#         # Крок 2: перевіряємо створену ціль
#         get_response = get_goal(base_url, headers, goal_id)
#         assert get_response.status_code == 200, f"Failed to fetch created goal, response: {get_response.text}"
#         goal = get_response.json().get('goal', {})
#         assert goal.get('name') == create_goal_data['name'], "Created goal name doesn't match"
#         assert goal.get('description') == create_goal_data['description'], "Goal description doesn't match"
#
#     # @test_steps('Create a new goal', 'Update the goal')
#     def test_update_goal(self, create_goal_data, headers, base_url):
#         # Крок 1: створюємо нову ціль
#         create_goal_data['name'] = fake.company()
#         create_goal_data['description'] = "Description for goal update"
#         create_response = create_goal(base_url, headers, create_goal_data)
#         assert create_response.status_code == 200, f"Failed to create goal, response: {create_response.text}"
#         goal_id = create_response.json().get('goal', {}).get('id')
#         # yield  # Переходимо до наступного кроку
#
#         # Крок 2: оновлюємо ціль
#         update_response = update_goal(base_url, headers, goal_id)
#         assert update_response.status_code == 200, f"Failed to update goal, response: {update_response.text}"
#
#         # Перевіряємо оновлення
#         get_response = get_goal(base_url, headers, goal_id)
#         goal = get_response.json().get('goal', {})
#         assert goal.get('name') == create_goal_data['name'], "Updated goal name doesn't match"
#         assert goal.get('description') == create_goal_data['description'], "Updated goal description doesn't match"
#
#     # @test_steps('Create a new goal', 'Delete the goal')
#     def test_delete_goal(self, create_goal_data, headers, base_url):
#         # Крок 1: створюємо нову ціль
#         create_goal_data['name'] = fake.company()
#         create_goal_data['description'] = "Description for goal delete"
#         create_response = create_goal(base_url, headers, create_goal_data)
#         assert create_response.status_code == 200, f"Failed to create goal, response: {create_response.text}"
#         goal_id = create_response.json().get('goal', {}).get('id')
#         # yield  # Переходимо до наступного кроку
#
#         # Крок 2: видаляємо ціль
#         delete_response = delete_goal(base_url, headers, goal_id)
#         assert delete_response.status_code == 200, f"Failed to delete goal, response: {delete_response.text}"
#
#         # Перевіряємо, що ціль видалено
#         get_response = get_goal(base_url, headers, goal_id)
#         assert get_response.status_code in [404, 403], "Deleted goal should not be found"
#
#     # @test_steps('Create a new goal', 'Create a key result')
#     def test_create_key_result(self, create_goal_data, create_key_result_data, headers, base_url):
#         # Крок 1: створюємо нову ціль
#         create_goal_data['name'] = fake.company()
#         create_response = create_goal(base_url, headers, create_goal_data)
#         assert create_response.status_code == 200, f"Failed to create goal, response: {create_response.text}"
#         goal_id = create_response.json().get('goal', {}).get('id')
#         # yield  # Переходимо до наступного кроку
#
#         # Крок 2: створюємо ключовий результат
#         create_key_result_data['goal_id'] = goal_id
#         create_key_result_data['name'] = fake.bs()
#
#         key_result_response = create_key_result(base_url, headers, goal_id, create_key_result_data)
#         assert key_result_response.status_code == 200, f"Failed to create key result, response: {key_result_response.text}"
#         key_result_id = key_result_response.json().get('key_result', {}).get('id')
#
#         get_response = get_goal(base_url, headers, goal_id)
#         goal = get_response.json().get('goal', {})
#         key_result = next((kr for kr in goal.get('key_results', []) if kr['id'] == key_result_id), None)
#         assert key_result is not None, "Key result should be present"
#         assert key_result['name'] == create_key_result_data['name'], "Key result name doesn't match"
#
#     # @test_steps('Create a new goal', 'Edit the key result')
#     def test_edit_key_result(self, create_goal_data, create_key_result_data, headers, base_url):
#         # Крок 1: створюємо нову ціль
#         create_goal_data['name'] = fake.company()
#         create_response = create_goal(base_url, headers, create_goal_data)
#         assert create_response.status_code == 200, f"Failed to create goal, response: {create_response.text}"
#         goal_id = create_response.json().get('goal', {}).get('id')
#         # yield  # Переходимо до наступного кроку
#
#         # Крок 2: створюємо ключовий результат
#         create_key_result_data['goal_id'] = goal_id
#         create_key_result_data['name'] = fake.bs()
#
#         key_result_response = create_key_result(base_url, headers, goal_id, create_key_result_data)
#         key_result_id = key_result_response.json().get('key_result', {}).get('id')
#         # yield  # Переходимо до наступного кроку
#
#         # Крок 3: редагуємо ключовий результат
#         edit_response = edit_key_result(base_url, headers, key_result_id)
#         assert edit_response.status_code == 200, f"Failed to edit key result, response: {edit_response.text}"
#
#         get_response = get_goal(base_url, headers, goal_id)
#         updated_key_result = next((kr for kr in get_response.json().get('goal', {}).get('key_results', []) if kr['id'] == key_result_id), None)
#         assert updated_key_result is not None, "Updated key result should be present"
#         assert updated_key_result['name'] == create_key_result_data['name'], "Updated key result name doesn't match"
#
#     # @test_steps('Create a new goal', 'Delete the key result')
#     def test_delete_key_result(self, create_goal_data, create_key_result_data, headers, base_url):
#         # Крок 1: створюємо нову ціль
#         create_goal_data['name'] = fake.company()
#         create_response = create_goal(base_url, headers, create_goal_data)
#         assert create_response.status_code == 200, f"Failed to create goal, response: {create_response.text}"
#         goal_id = create_response.json().get('goal', {}).get('id')
#         # yield  # Переходимо до наступного кроку
#
#         # Крок 2: створюємо ключовий результат
#         create_key_result_data['goal_id'] = goal_id
#         create_key_result_data['name'] = fake.bs()
#
#         key_result_response = create_key_result(base_url, headers, goal_id, create_key_result_data)
#         key_result_id = key_result_response.json().get('key_result', {}).get('id')
#         # yield  # Переходимо до наступного кроку
#
#         # Крок 3: видаляємо ключовий результат
#         delete_response = delete_key_result(base_url, headers, key_result_id)
#         assert delete_response.status_code == 200, f"Failed to delete key result, response: {delete_response.text}"
#
#         get_response = get_goal(base_url, headers, goal_id)
#         deleted_key_result = next((kr for kr in get_response.json().get('goal', {}).get('key_results', []) if kr['id'] == key_result_id), None)
#         assert deleted_key_result is None, "Deleted key result should not be present"
