import requests
from faker import Faker

fake = Faker()

goals_url = '/team/9012430611/goal'

def get_goals(base_url, headers):
    response = requests.get(f"{base_url}{goals_url}", headers=headers)
    return response

def create_goal(base_url, headers, data):
    # Генеруємо рандомні дані для Goal
    data['name'] = fake.company()
    data['description'] = fake.sentence()
    data['color'] = fake.hex_color()
    data['due_date'] = int(fake.future_datetime().timestamp() * 1000)

    response = requests.post(f"{base_url}{goals_url}", headers=headers, json=data)
    return response, data  # Повертаємо відповідь та створені дані

def get_goal(base_url, headers, goal_id):
    response = requests.get(f"{base_url}/goal/{goal_id}", headers=headers)
    return response

def update_goal(base_url, headers, goal_id):
    updated_data = {
        "name": fake.company(),
        "description": fake.sentence()
    }
    response = requests.put(f"{base_url}/goal/{goal_id}", headers=headers, json=updated_data)
    return response, updated_data  # Повертаємо відповідь та оновлені дані

def delete_goal(base_url, headers, goal_id):
    response = requests.delete(f"{base_url}/goal/{goal_id}", headers=headers)
    return response

def create_key_result(base_url, headers, goal_id, data):
    data['name'] = fake.word()
    response = requests.post(f"{base_url}/goal/{goal_id}/key_result", headers=headers, json=data)
    return response, data  # Повертаємо відповідь та створені дані

def edit_key_result(base_url, headers, key_result_id):
    updated_data = {
        "name": fake.word()
    }
    response = requests.put(f"{base_url}/key_result/{key_result_id}", headers=headers, json=updated_data)
    return response, updated_data  # Повертаємо відповідь та оновлені дані

def delete_key_result(base_url, headers, key_result_id):
    response = requests.delete(f"{base_url}/key_result/{key_result_id}", headers=headers)
    return response
