# from here I will get the labels corresponding to the each college
from info_from_each_college import get_paragraphs_without_label
from info_from_each_college import split_list
from data_from_web import get_all_links
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json
webdriver_path = r'D:\DOWNLOADS\chromedriver-win64\chromedriver.exe'  
driver = webdriver.Chrome(executable_path=webdriver_path)
list_of_links = get_all_links('MuiGrid-root.MuiGrid-container.jobFeature-title-bg.css-5dis7f')
list_of_links=list_of_links[:-3]

paragraph_selector = '.MuiTypography-root.MuiTypography-body1.css-w4oa02'
label_selector = 'label.MuiFormLabel-root.MuiInputLabel-root.MuiInputLabel-animated.MuiFormLabel-colorPrimary.MuiInputLabel-root.MuiInputLabel-animated.css-12po370'

json_data={"modes":[],"end_dates":[]}
for index,link in enumerate(list_of_links):
    print(f"Printing the{index}")
    get_labels=get_paragraphs_without_label(link,driver,paragraph_selector,label_selector)
    modes,end_dates=split_list(0,get_labels)
    print("The list of mode is")
    print(modes)
    print("The list of dates is")
    print(end_dates)
    json_data["modes"].append(modes)
    json_data["end_dates"].append(end_dates)

with open('labelss.json', 'w') as json_file:
    json.dump(json_data, json_file, indent=2)

print("JSON file has been created.")