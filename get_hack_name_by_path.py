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
def return_all_the_detail(file_path, college_name):
    with open(file_path, 'r') as file:
        data = json.load(file)

    matching_colleges = [key for key in data.keys() if key.startswith(college_name)]

    if not matching_colleges:
        return f"Details not found for {college_name}"

    result = []
    for matching_college in matching_colleges:
        
        college_details = data[matching_college]
        hackathon_name=college_details.get('hackathonName')
        mode = college_details.get('mode')
        team_size = college_details.get('teamSize')
        registrations = college_details.get('numberOfRegistrations')

        result.append(f"For {hackathon_name}, the event is being conducted in {mode} mode, with a recommended size of {team_size}, and total of {registrations} students are there.  ")

    return '\n'.join(result)
def return_only_matching_hackathon(file_path,college_name,hackathon_name):
    with open(file_path, 'r') as file:
        data = json.load(file)

    matching_colleges = [key for key in data.keys() if key.startswith(college_name)]
    if not matching_colleges:
        return f"Details not found for {college_name}"
    result=[]
    for matching_college in matching_colleges:
        college_details=data[matching_college]
        compared_hack_name=college_details.get('hackathonName')
        if(compared_hack_name!=hackathon_name):
            # since I dont need to process the other hackathons here
            break
        else:
            hackathon_name=college_details.get('hackathonName')
            mode = college_details.get('mode')
            team_size = college_details.get('teamSize')
            registrations = college_details.get('numberOfRegistrations')

            result.append(f"For {hackathon_name}, the event is being conducted in {mode} mode, with a recommended size of {team_size}, and total of {registrations} students are there.  ")

    return '\n'.join(result)