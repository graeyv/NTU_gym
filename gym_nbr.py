import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime

# Scrape the number of people in the gym
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

# Store data in a CSV file
def store_data():
    number = scrape_gym_nbr()
    if number:
        # Create or append to the CSV file with a timestamp and the scraped number
        with open('scraped_data.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([datetime.now(), number])
    else:
        print("No number found or error in scraping.")

# Run the store_data function
store_data()


