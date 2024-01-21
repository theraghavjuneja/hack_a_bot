# import json
# def return_the_hackathon(file_path,parameters):
#     with open(file_path,'r') as file:
#         data=json.load(file)
#     return data[parameters].get('hackathonName')


import json
import re

def return_the_hackathon(file_path, college_name):
    with open(file_path, 'r') as file:
        data = json.load(file)

    hackathon_names = []

    college_pattern = re.compile(rf'^{re.escape(college_name)}(\d+)?$')

    
    for key, value in data.items():
        
        if college_pattern.match(key):
            hackathon_name = value.get('hackathonName')
            if hackathon_name:
                hackathon_names.append(hackathon_name)

    return hackathon_names
# def return_all_the_detail(file_path, college_name):
#     with open(file_path, 'r') as file:
#         data = json.load(file)

#     college_details = data.get(college_name)

#     if college_details:
#         mode = college_details.get('mode')
#         team_size = college_details.get('teamSize')
#         registrations = college_details.get('numberOfRegistrations')

#         return f'I got the mode as {mode} mode , team as size of {team_size} and number of registrations which are {registrations}'
#     else:
#         return f"Details not found for {college_name}"
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

        result.append(f"For {hackathon_name}, the event is being conducted in {mode} mode, with a recommended size of {team_size}, and total of {registrations} students are there.  You can now write things like Search for information about the various rounds in this hackathon ")

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
            continue
        else:
            hackathon_name=college_details.get('hackathonName')
            mode = college_details.get('mode')
            team_size = college_details.get('teamSize')
            registrations = college_details.get('numberOfRegistrations')

            result.append(f"For {hackathon_name}, the event is being conducted in {mode} mode, with a recommended size of {team_size}, and total of {registrations} students are there.  ")

    return '\n'.join(result)
def search_index(json_file_path,college_name,hackathon_name):
    with open(json_file_path,'r') as file:
        data=json.load(file)
    matching_colleges = [key for key in data.keys() if key.startswith(college_name)]
    for matching_college in matching_colleges:
        college_details=data[matching_college]
        compared_hack_name=college_details.get('hackathonName')
        if(compared_hack_name!=hackathon_name):
            # since I dont need to process the other hackathons here
            continue
        else:
            # get the index of the matching college
            index = list(data.keys()).index(matching_college)
        
    return index
# currently I am searching or getting only 2 labels here
# def get_labels(json_file_path,index):
#     # remember need to pass that file which has
#     with open(json_file_path,'r') as file:
#         data=json.load(file)
#     # got the index too so now need to search in start dates as well as the indices
#     start_dates=data.get('starting_dates')[index]
#     headings=data.get('headings')[index]
#     return f'I found the following things {", ".join(start_dates)} and {", ".join(headings)}'
import json

def get_labels(json_file_path_of_output, json_file_path_of_labels, index):
    with open(json_file_path_of_output, 'r') as file:
        output_json = json.load(file)
    with open(json_file_path_of_labels) as file:
        labels_json = json.load(file)
        
    headings = output_json.get('headings')[index]
    start_dates = output_json.get('starting_dates')[index]
    modes = labels_json.get('modes')[index]
    ending_dates = labels_json.get('end_dates')[index]
    
    result_statements = []
    for i in range(len(headings)):
        heading = headings[i]
        start_date = start_dates[i]
        mode = modes[i]
        ending_date = ending_dates[i]
        
        result_statement = f"{heading} will take place in {mode} mode whose starting date is {start_date} and ending date is {ending_date}."
        result_statements.append(result_statement)
    
    return result_statements



    # labeled_elements = [f"{heading} will {start_date}" for heading, start_date in zip(headings, start_dates)]

    # return labeled_elements
    