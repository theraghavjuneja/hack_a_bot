from data_from_web import extraction
from data_from_web import features_sublist
from data_from_web import get_all_links
from info_from_each_college import extract_element
import json
# hackathon_names_list=[]
# college_names_list=[]
# features_list=[]
# extraction(hackathon_names_list,college_names_list,features_list)

# mode=[]
# teamSize=[]
# numberOfRegistrations=[]
# features_sublist(0,features_list,mode)
# features_sublist(1,features_list,teamSize)
# features_sublist(2,features_list,numberOfRegistrations)


json_data = {"headings": [], "starting_dates": []}

list_of_links = get_all_links('MuiGrid-root.MuiGrid-container.jobFeature-title-bg.css-5dis7f')
list_of_links=list_of_links[:-3]
for index, link in enumerate(list_of_links):
    print(f"{index} which is being printed")
    
    # Extract headings
    headings = extract_element(link, 'MuiFormLabel-root.MuiInputLabel-root.MuiInputLabel-animated.MuiFormLabel-colorPrimary.MuiInputLabel-root.MuiInputLabel-animated.css-2vzt7s')
    print("Heading:", headings)
    json_data["headings"].append(headings)
    
    # Extract starting dates
    start_dates_list = extract_element(link, 'MuiTypography-root.MuiTypography-body1.css-1udcvx7')
    print("Starting dates:", start_dates_list)
    json_data["starting_dates"].append(start_dates_list)

# Save the data to a JSON file
with open('output.json', 'w') as json_file:
    json.dump(json_data, json_file, indent=2)

print("JSON file has been created.")
    



# NOW I NEED TO EXTRACT THE THINGS FROM EACH ELEMENT
# VIZ HEADING, START_DATES_LISTWHICH CAN BE EXTRACTED EASILY