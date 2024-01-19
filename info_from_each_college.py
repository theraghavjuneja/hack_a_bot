# I have got all the sites . Here I am extracting the things from there
# already have a list from each_site_extraction which I will be integrating over here 

# IMPORT-STATEMENTS
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import json
# url = 'https://whereuelevate.com/drills/bennett-university-industry-hackathon'  

# webdriver_path = r'D:\DOWNLOADS\chromedriver-win64\chromedriver.exe'  # Update this with the actual path
# driver = webdriver.Chrome(executable_path=webdriver_path)
# driver.get(url)


def extract_element(url,class_name):
    webdriver_path = r'D:\DOWNLOADS\chromedriver-win64\chromedriver.exe'  # Update this with the actual path
    driver = webdriver.Chrome(executable_path=webdriver_path)
    driver.get(url)
    heading_text_locator = WebDriverWait(driver, 300).until(EC.presence_of_all_elements_located((By.CLASS_NAME, class_name)))
    text_list = []
    
    for heading in heading_text_locator:
        text_list.append(heading.text)
    driver.quit()
    return text_list
# def get_non_matching_labels(driver):
#     find_class = driver.find_elements(By.CLASS_NAME, 'MuiFormLabel-root.MuiInputLabel-root.MuiInputLabel-animated.MuiFormLabel-colorPrimary.MuiInputLabel-root.MuiInputLabel-animated.css-12po370')

#     
#     label_result = ''
#     if find_class:
#         label_result = find_class[0].text

#     all_labels = driver.find_elements(By.CLASS_NAME, 'MuiTypography-root.MuiTypography-body1.css-w4oa02')
#     non_matching_labels = [element.text for element in all_labels if element.text != label_result]

#     return non_matching_labels

# headings=extract_element('MuiFormLabel-root.MuiInputLabel-root.MuiInputLabel-animated.MuiFormLabel-colorPrimary.MuiInputLabel-root.MuiInputLabel-animated.css-2vzt7s') 
# start_dates_list=extract_element('MuiTypography-root.MuiTypography-body1.css-1udcvx7')

def get_paragraphs_without_label(link,driver, paragraph_selector, label_selector):
    webdriver_path = r'D:\DOWNLOADS\chromedriver-win64\chromedriver.exe'  # Update this with the actual path
    driver = webdriver.Chrome(executable_path=webdriver_path)
    driver.get(link)
    paragraphs = driver.find_elements_by_css_selector(paragraph_selector)
    paragraphs_without_label = []

    for paragraph in paragraphs:
        if not paragraph.find_elements_by_css_selector(label_selector):
            paragraphs_without_label.append(paragraph.text)
    driver.quit()
    return paragraphs_without_label
# the paragraph and label selector which I need to search for
# paragraph_selector = '.MuiTypography-root.MuiTypography-body1.css-w4oa02'
# label_selector = 'label.MuiFormLabel-root.MuiInputLabel-root.MuiInputLabel-animated.MuiFormLabel-colorPrimary.MuiInputLabel-root.MuiInputLabel-animated.css-12po370'
# get_labels=get_paragraphs_without_label(driver,paragraph_selector,label_selector)
def split_list(startIndex, original_list):
    sublist1 = original_list[startIndex::2]
    sublist2 = original_list[startIndex + 1::2]
    return sublist1, sublist2
# modes,end_dates=split_list(0,get_labels)

# now there is another thing i need to do 
# if __name__=="__main__":
#     print("The headings result")
#     for heading in headings:
#         print(heading)
#     print()
#     print("Start dates result")
#     for dates in start_dates_list:
#         print(dates)
#     print("Important labels")
#     # for labels in get_labels:
#     #     print(labels)
#     print("mode")
#     for mode in modes:
#         print(mode)
#     print("ENd date")
#     for end_date in end_dates:
#         print(end_date)
        
# driver.quit()

