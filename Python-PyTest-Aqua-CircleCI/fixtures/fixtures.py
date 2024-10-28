import pytest
import json
from faker import Faker
from config import settings

fake = Faker()

@pytest.fixture
def headers():
    return {
        "Authorization": settings.TOKEN,
        "Content-Type": "application/json"
    }

@pytest.fixture
def base_url():
    return settings.BASE_URL

@pytest.fixture
def create_goal_data():
    with open('fixtures/create_goal.json') as file:
        data = json.load(file)
    data['name'] = fake.name()
    return data

@pytest.fixture
def create_key_result_data():
    with open('fixtures/create_key_result.json') as file:
        data = json.load(file)
    data['name'] = fake.name()
    return data
