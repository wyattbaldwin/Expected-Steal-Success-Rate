#This script scrapes data from mlb.com and creates or edits a .csv file

import requests
from bs4 import BeautifulSoup
import csv
import random
import time

# URL of the website to scrape
base_url = "https://www.mlb.com/stats/stolen-bases/all-time-by-season"

# Number of pages to scrape
num_pages = 3798

# Name of the CSV file to save the data to
filename = "stolen_bases.csv"

fixed_columns = ['PLAYER', 'YEAR', 'TEAM', 'G', 'AB', 'R', 'H', '2B', '3B', 'HR', 'RBI', 'BB', 'SO', 'SB', 'CS', 'AVG', 'OBP', 'SLG', 'OPS']

with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
    csv_writer = csv.writer(csvfile)
    for page_num in range(1, num_pages + 1):
        time.sleep(random.uniform(1, 37)) # sleep random time between 1 and 37 sec
        # Construct the full URL
        url = base_url + '?page=' + str(page_num)
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        # Find the next page button
        next_button = soup.find('button', {'class': 'button-3wq5VxsJ paginationSide-3bpX4evu'})
        # if the next page button not found, stop looping
        if not next_button:
            break
        next_url = next_button.get('href')
        url = next_url
        # Extract the data from the website
        table = soup.find('table')
        table_rows = table.find_all('tr')
        for tr in table_rows:
            th_tag = tr.find('th', {'class': 'pinned-col-3lxtuFnc'})
            if th_tag:
                a_tag = th_tag.find('a', {'class': 'bui-link'})
                if a_tag:
                    player_name = " ".join(a_tag.stripped_strings)
                else:
                    player_name = ""
            else:
                player_name = ""
            if page_num == 1 and len(fixed_columns) > 0:  # this will help us only to extract the header of the table in the first page
                csv_writer.writerow(fixed_columns)
                fixed_columns = []
            td = tr.find_all('td')
            data = [i.get_text(strip=True) for i in td]
            data.insert(0, player_name)
            csv_writer.writerow(data)
        print("Scraped page", page_num)
    print("Scraping complete!")
