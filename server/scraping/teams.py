import requests
from bs4 import BeautifulSoup

def scrape_teams():
    url = 'https://www.fangraphs.com/leaders/major-league?pos=all&stats=bat&lg=all&qual=y&type=8&season=2024&month=0&season1=2024&ind=0&pageitems=2000000000&team=0%2Cts'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    table = soup.find('table', class_='rgMasterTable')
    headers = [header.text for header in table.find_all('th')]
    teams_data = []

    for row in table.find_all('tr')[1:]:  # Skip the header row
        cols = row.find_all('td')
        team_data = {headers[i]: cols[i].text.strip() for i in range(len(cols))}
        teams_data.append(team_data)
    
    return teams_data
