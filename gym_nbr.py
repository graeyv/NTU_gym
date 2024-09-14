import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime

# scrape nbr of people in gym
def scrape_gym_nbr():

    url = 'https://rent.pe.ntu.edu.tw/'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the div with class 'ICI' and containing the text '現在人數'
    div = soup.select_one("div.ICI:-soup-contains('現在人數')")
    
    if div:
        number = div.find('span').text
        return number
    return None

# store data
def store_data():
    number = scrape_gym_nbr()
    if number:
        # Store the number with a timestamp in a CSV file
        with open('scraped_data.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([datetime.now(), number])
    else:
        print("No number found or error in scraping.")

# run store data function
store_data()

