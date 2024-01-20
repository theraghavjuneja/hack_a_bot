import json
def get_from_json(file_path, key):
    with open(file_path, 'r') as file:
        data = json.load(file)
        return data.get(key, {})
print(get_from_json('universities.json','Bennett University (Times of India Group)'))