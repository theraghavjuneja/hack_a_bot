from selenium import webdriver

url = 'https://whereuelevate.com/drills/innovacion-unviel'  

webdriver_path = r'D:\DOWNLOADS\chromedriver-win64\chromedriver.exe' 
driver = webdriver.Chrome(executable_path=webdriver_path)
driver.get(url)

# will also have to give a link inside the get_overview from where it will extract the text

def get_overview():
    div_element = driver.find_element_by_id('overview')
    paragraphs = div_element.find_elements_by_xpath('.//p')
    for paragraph in paragraphs:
        print(paragraph.text)
    print(len(paragraphs))
get_overview()







# Close the WebDriver
driver.quit()
