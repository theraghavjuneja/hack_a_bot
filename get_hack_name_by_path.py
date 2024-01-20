import json
def return_the_hackathon(file_path,parameters):
    with open(file_path,'r') as file:
        data=json.load(file)
    return data[parameters].get('hackathonName')