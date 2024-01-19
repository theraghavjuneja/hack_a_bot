import json
import concurrent.futures
from selenium import webdriver
from selenium.webdriver.common.by import By
from data_from_web import get_all_links
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def extract_element(url, class_name):
    webdriver_path = r'D:\DOWNLOADS\chromedriver-win64\chromedriver.exe'  # Update this with the actual path
    driver = webdriver.Chrome(executable_path=webdriver_path)
    driver.get(url)
    try:
        heading_text_locator = WebDriverWait(driver, 25).until(EC.presence_of_all_elements_located((By.CLASS_NAME, class_name)))
        text_list = [heading.text for heading in heading_text_locator]
    finally:
        driver.quit()
    return text_list

def process_link(link):
    print(f"Processing link: {link}")
    headings = extract_element(link, 'MuiFormLabel-root.MuiInputLabel-root.MuiInputLabel-animated.MuiFormLabel-colorPrimary.MuiInputLabel-root.MuiInputLabel-animated.css-2vzt7s')
    print("Heading:", headings)
    start_dates_list = extract_element(link, 'MuiTypography-root.MuiTypography-body1.css-1udcvx7')
    print("Starting dates:", start_dates_list)

    # Create dictionary with link as key and headings and start_dates_list as values
    result_dict = {
        "start_dates": start_dates_list,
        "heading": headings
    }

    # Write the result to a JSON file
    with open(f"{link.replace('/', '_')}.json", 'w') as json_file:
        json.dump(result_dict, json_file)

list_of_links = get_all_links('MuiGrid-root.MuiGrid-container.jobFeature-title-bg.css-5dis7f')

# Using concurrent.futures to run tasks in parallel
with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.map(process_link, list_of_links)
