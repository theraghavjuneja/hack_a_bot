import json
import re

def return_the_hackathon(file_path, college_name):
    with open(file_path, 'r') as file:
        data = json.load(file)

    hackathon_names = []

    # Regular expression to match variations of the college name
    college_pattern = re.compile(rf'^{re.escape(college_name)}(\d+)?$')

    # Iterate through each entry in the data
    for key, value in data.items():
        # Check if the college name matches the pattern
        if college_pattern.match(key):
            hackathon_name = value.get('hackathonName')
            if hackathon_name:
                hackathon_names.append(hackathon_name)

    return hackathon_names