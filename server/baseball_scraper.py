import requests 
from bs4 import BeautifulSoup

def get_probable_pitchers(url='https://baseballsavant.mlb.com/probable-pitchers'):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    games = soup.find_all('div', {'class': 'probable-pitchers__matchup'})
    pitchers_data = []
    for game in games:
        pitcher = game.find('div', {'class': 'probable-pitchers__pitcher-name'}).text.strip()
        team = game.find('span', {'class': 'probable-pitchers__team-name'}).text.strip()
        handedness = game.find('span', {'class': 'probable-pitchers__pitcher-hand'}).text.strip()
        opponent_team = game.find('div', {'class': 'probable-pitchers__opponent-name'}).text.strip()
        pitchers_data.append({
            'pitcher': pitcher,
            'team': team,
            'handedness': handedness,
            'opponent_team': opponent_team
        })

    # Print the data to the console
    for data in pitchers_data:
        print(data)
    return pitchers_data

get_probable_pitchers()

