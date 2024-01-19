from data_from_web import extraction
from data_from_web import features_sublist
from data_from_web import get_all_links
from info_from_each_college import extract_element
import json
hackathon_names_list=[]
college_names_list=[]
features_list=[]
extraction(hackathon_names_list,college_names_list,features_list)

mode=[]
teamSize=[]
numberOfRegistrations=[]
features_sublist(0,features_list,mode)
features_sublist(1,features_list,teamSize)
features_sublist(2,features_list,numberOfRegistrations)
hackathon_data={}
for i in range(len(college_names_list[:-3])):
    college=college_names_list[i]
    already_present=[key for key in hackathon_data.keys() if key.startswith(college)]
    if(len(already_present)==0):
        hackathon_data[college]={
        "hackathonName":hackathon_names_list[i],
        "mode":mode[i],
        "teamSize":teamSize[i],
        "numberOfRegistrations":numberOfRegistrations[i]
        }
    else:
        key=college+str(len(already_present)+1)
        hackathon_data[key]={
            "hackathonName":hackathon_names_list[i],
            "mode":mode[i],
            "teamSize":teamSize[i],
            "numberOfRegistrations":numberOfRegistrations[i]
        }
json_file_path="hackathon_data_json.json"
with open(json_file_path, 'w') as json_file:
    json.dump(hackathon_data, json_file, indent=2)

print(f"The JSON data has been written to {json_file_path}")
