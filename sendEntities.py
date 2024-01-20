import requests
import json
def get_universities_from_json(json_path):
    with open(json_path,'r') as file:
        data=json.load(file)
    universities=list(data.keys())
    return universities
if __name__=="__main__":
    # checking if it actually able to return me the keys
    l1=get_universities_from_json('hackathon_data_json.json')
    print(l1)
def create_entities(project_id,entity_type,entitiy_values):
    base_url=f'https://dialogflow.cloud.google.com/#/agent/hackahon-chatbot-tx9j/entities'