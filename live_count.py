from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json
 
def get_live_count():
    url='https://whereuelevate.com/drills'
    webdriver_path=r'D:\DOWNLOADS\chromedriver-win64\chromedriver.exe'
    driver = webdriver.Chrome(executable_path=webdriver_path)
    driver.get(url)
    locator = (By.CLASS_NAME, 'MuiChip-label.MuiChip-labelSmall.css-1pjtbja')
    timeout=40
    live_count=0
    college_elements=WebDriverWait(driver,timeout).until(
        EC.presence_of_all_elements_located(locator)
    )
    for element in college_elements:
        if element.text =='Live':
            live_count+=1
    return(live_count)

