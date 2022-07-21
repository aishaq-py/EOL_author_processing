from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import random as ra
import re
import time
#from EOL_test import surname

driver_path = "C:\Program Files (x86)\Google\Driver\chromedriver.exe"
search_term = "longitudinal cost reform health" + " "
#search_term = input("Raw author list: ")


#Initialise Chrome
driver = webdriver.Chrome(executable_path=driver_path)
g_scholar = driver.get("https://scholar.google.com")
time.sleep(ra.randint(10,20))
search_bar = driver.find_element_by_name("q")
#search_bar.send_keys(search_term + surname)
search_bar.send_keys(search_term)
search_bar.send_keys(Keys.RETURN)

def set_year(year):
    year_dropbox = driver.find_element_by_id("gs_res_ab_yy-b")
    year_dropbox.click()
    year_select = driver.find_element_by_xpath("//a[contains(@href, '/scholar?as_ylo=" + str(year) + "')]")
    year_select.click()

set_year(2017)
time.sleep(ra.randint(20,30))
    
cite_btn = driver.find_elements_by_class_name("gs_or_cit")
n_entries = len(cite_btn)
author_list = []    
author_cleanup = re.compile('\.\s.{1,}')

def author_search(cite_btn,author_list):
    for i in cite_btn:
        temp_name = "x"
        i.click()
        time.sleep(2)
        cite_formats = driver.find_elements_by_class_name("gs_citr")
        entry = cite_formats[4].text
        temp_name = re.sub(author_cleanup,"",entry)
        temp_name = temp_name.split(",")
        for j in temp_name:
            author_list.append(j)
        close_cite = driver.find_element_by_id("gs_cit-x")
        close_cite.click()
    return author_list
    
pages = driver.find_elements_by_class_name("gs_nma")
for i in pages:
    i.click()
    time.sleep(1.5)
# =============================================================================
# for i in pages:
#     i.click()
#     author_search(cite_btn,author_list)   
# 
# author_list = list(set(author_list))
# =============================================================================
