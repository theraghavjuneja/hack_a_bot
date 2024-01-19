# I have got all the sites . Here I am extracting the things from there
# already have a list from each_site_extraction which I will be integrating over here 

# IMPORT-STATEMENTS
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json
url = 'https://whereuelevate.com/drills/bennett-university-industry-hackathon'  

webdriver_path = r'D:\DOWNLOADS\chromedriver-win64\chromedriver.exe'  # Update this with the actual path
driver = webdriver.Chrome(executable_path=webdriver_path)
driver.get(url)


def extract_element(class_name):
    heading_text_locator = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, class_name)))
    text_list = []
    
    for heading in heading_text_locator:
        text_list.append(heading.text)
    
    return text_list
def get_non_matching_labels(driver):
    find_class = driver.find_elements(By.CLASS_NAME, 'MuiFormLabel-root.MuiInputLabel-root.MuiInputLabel-animated.MuiFormLabel-colorPrimary.MuiInputLabel-root.MuiInputLabel-animated.css-12po370')

    # Assuming there's only one element, get its text
    label_result = ''
    if find_class:
        label_result = find_class[0].text

    all_labels = driver.find_elements(By.CLASS_NAME, 'MuiTypography-root.MuiTypography-body1.css-w4oa02')
    non_matching_labels = [element.text for element in all_labels if element.text != label_result]

    return non_matching_labels

headings=extract_element('MuiFormLabel-root.MuiInputLabel-root.MuiInputLabel-animated.MuiFormLabel-colorPrimary.MuiInputLabel-root.MuiInputLabel-animated.css-2vzt7s') 
start_dates_list=extract_element('MuiTypography-root.MuiTypography-body1.css-1udcvx7')
for heading in headings:
    print(heading)
print()
for dates in start_dates_list:
    print(dates)


things=get_non_matching_labels()
for thing in things:
    print(thing)

# <label class="MuiFormLabel-root MuiInputLabel-root MuiInputLabel-animated MuiFormLabel-colorPrimary MuiInputLabel-root MuiInputLabel-animated css-12po370">Bennett University, Greater Noida </label>

# 3rd one has a different approach
# find_class=driver.find_elements(By.CLASS_NAME,'MuiFormLabel-root.MuiInputLabel-root.MuiInputLabel-animated.MuiFormLabel-colorPrimary.MuiInputLabel-root.MuiInputLabel-animated.css-12po370')
# # corrsponding to one element only
# label_result=''
# for element in find_class:
#     label_result=element.text

# all_labels=driver.find_elements(By.CLASS_NAME,'MuiTypography-root.MuiTypography-body1.css-w4oa02')
# for element in all_labels:
#     if(element.text==label_result):
#         pass
#     else:
#         print(element.text)


