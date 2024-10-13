import json

# Reading the spaces.json file
with open('spaces.json', 'r', encoding='utf-8') as json_file:
    data = json.load(json_file)

total_lists_found = 0
test_lists_found = 0

print("\n======== Lists with names starting with 'test': ========")

# Iterating through all folders and lists
for folder in data['folders']:
    for list_item in folder['lists']:
        total_lists_found += 1

        # If the list name starts with "test", output the space.name and space.id
        if list_item['name'].lower().startswith('test'):
            test_lists_found += 1
            print(f"{test_lists_found}. List ID: {list_item['id']}")
            print('Space Name:', list_item['space']['name'])
            print('Space ID:', list_item['space']['id'])

print("\n======== Summary ========")
print(f"Total lists found: {total_lists_found}")
print(f"Lists with names starting with 'test': {test_lists_found}")
