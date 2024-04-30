import requests
from bs4 import BeautifulSoup

def scrape_pitchers():
    url = 'https://baseballsavant.mlb.com/probable-pitchers'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    data_section = soup.find('div', {'class': 'some-class'})  # Update with correct class
    pitchers_data = []

    for entry in data_section.find_all('tr'):  # Assuming each pitcher's data is in a row
        name = entry.find('td', {'class': 'pitcher-name'}).text.strip()
        team = entry.find('td', {'class': 'team-name'}).text.strip()
        handedness = entry.find('td', {'class': 'pitcher-handedness'}).text.strip()
        # More data extraction as necessary

        pitcher_info = {
            'Name': name,
            'Team': team,
            'Handedness': handedness
            # Add more fields as extracted above
        }
        pitchers_data.append(pitcher_info)

    return pitchers_data
