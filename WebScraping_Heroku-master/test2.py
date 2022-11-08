import pandas as pd
import csv
from selenium import webdriver
from bs4 import BeautifulSoup
from more_itertools import unique_everseen
    
filename = 'temp.csv'
f = open(filename, 'w')

PATH = 'C:\Program Files (x86)\chromedriver.exe'
# Step 1: Create a session and load the page
driver = webdriver.Chrome(executable_path = PATH)
driver.get('https://avherald.com/h?list=&opt=0')

# Wait for the page to fully load
driver.implicitly_wait(5)

# Step 2: Parse HTML code and grab tables with Beautiful Soup
soup = BeautifulSoup(driver.page_source, 'lxml')
tables = soup.find_all('table')


#Need to figure out why it creates duplicates
for table in tables:
    try:
        type = table.find('img')['title']
        incident = table.find ('span', class_="headline_avherald").text
        link = table.find('a')['href']
        f.write(type + ', ' + incident  + '|' + ' LINK: ' +  'avherald.com' + link  + '\n')    
    except:
        continue 

f.close 
#Temp solution
with open('temp.csv', 'r') as f, open('av.csv', 'w') as out_file:
    out_file.writelines(unique_everseen(f))






