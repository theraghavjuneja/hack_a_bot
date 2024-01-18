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

# wait=WebDriverWait(driver,10)
# left_namesw=wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME,'MuiFormLabel-root.MuiInputLabel-root.MuiInputLabel-animated.MuiFormLabel-colorPrimary.MuiInputLabel-root.MuiInputLabel-animated.css-2vzt7s')))
left_names = driver.find_elements(By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[3]/div/div[3]/div/div[2]/div[3]/div[2]/div[1]/p')
paragraphs = driver.find_elements(By.CLASS_NAME, 'MuiTypography-root.MuiTypography-body1.css-w4oa02')
start_dates=driver.find_elements(By.CLASS_NAME,'MuiTypography-root.MuiTypography-body1.css-1udcvx7')

for paragraph in paragraphs:
    print(paragraph.text)
print()
for name in left_names:
    a=name.text
    print(a)
print()
for date in start_dates:
    a=date.text
    print(a)
# left_names=driver.find_elements(By.CLASS_NAME,'MuiTypography-root.MuiTypography-body1.css-w4oa02')
# for name in left_names:
#     a=name.text
#     print(a)

driver.close()
# ok so now I have got all the required things My task is to make a corresponding file 


