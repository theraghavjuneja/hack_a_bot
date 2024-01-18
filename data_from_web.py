# import statements
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json

# HERE IS THE URL OF WEBSITE FROM I AM UPLOADING DOCS
url = 'https://whereuelevate.com/drills'  

webdriver_path = r'D:\DOWNLOADS\chromedriver-win64\chromedriver.exe'  # Update this with the actual path
driver = webdriver.Chrome(executable_path=webdriver_path)
driver.get(url)

hackathon_names_list=[]
college_names_list=[]
# Features list has currently 3 features mode,team_size and registration
features_list=[]

def extract_text_content(driver,class_name,target_list,timeout=20):
    try:
        elements=WebDriverWait(driver,timeout).until(EC.presence_of_all_elements_located((By.CLASS_NAME,class_name)))
        for element in elements:
            text_content=element.text
            target_list.append(text_content)
    except Exception as e:
        # need to handle here what's wrong over here and what's not wrong
        # or I can just directly print the exception 
        pass


def extraction(hackathon_names_list,college_names_list,features_list):
    extract_text_content(driver, 'MuiTypography-root.MuiTypography-body1.jobListingTitle.css-19f8owz', hackathon_names_list,timeout=20)
    extract_text_content(driver, 'MuiTypography-root.MuiTypography-body1.jobListingSubTitle.css-1yq81z9', college_names_list,timeout=20)
    extract_text_content(driver, 'MuiTypography-root.MuiTypography-body1.featuredCardTxt.css-v12ejh', features_list,timeout=20)


extraction(hackathon_names_list,college_names_list,features_list)


# now features_list is separated to mode and teamSize as well as the numberOfRegistrations list


mode=[]
teamSize=[]
numberOfRegistrations=[]

def features_sublist(startIndex,features_list,sublist):
    for i in range(startIndex,len(features_list),3):
        sublist.append(features_list[i])

features_sublist(0,features_list,mode)
features_sublist(1,features_list,teamSize)
features_sublist(2,features_list,numberOfRegistrations)

print(mode)
print(teamSize)



    
    
    