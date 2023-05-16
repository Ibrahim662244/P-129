from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup as bs
import time
import pandas as pd
import requests

# NASA Exoplanet URL
START_URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"

# Webdriver
page = requests.get(START_URL)
soup = bs(page.text, 'html.parser')
star_table = soup.find('table')
temp_list = []
table_rows = star_table.find_all('tr')

for tr in table_rows:
    td = tr.find_all('td')
    row = [i.text.rstrip( ) for i in td]
    temp_list.append(row)

Star_names = []
Distance = []
Mass = []
Radius = []
Lum = []

for i in range(1, len(temp_list)):
    Star_names.append(temp_list[i][1])
    Distance.append(temp_list[i][3])
    Mass.append(temp_list[i][5])
    Radius.append(temp_list[i][6])
    Lum.append(temp_list[i][7])


# Define pandas DataFrame   
star_df_1 = pd.DataFrame(list(zip(Star_names, Distance, Mass, Radius, Lum)),columns= ['Star_names','Distance', 'Mass', 'Radius', 'Lum'])


# Convert to CSV
star_df_1.to_csv("bright_star.csv")
    


