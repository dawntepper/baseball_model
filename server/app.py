from flask import Flask
import db
from flask_cors import CORS
from scraping.players import scrape_players
from scraping.teams import scrape_teams
from scraping.pitchers import scrape_pitchers

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

@app.route('/scrape/players')
def handle_scrape_players():
    data = scrape_players()
    db.save_players(data)
    return {'status': 'success'}

@app.route('/scrape/teams')
def handle_scrape_teams():
    data = scrape_teams()
    db.save_teams(data)
    return {'status': 'success'}

@app.route('/scrape/pitchers')
def handle_scrape_pitchers():
    pitchers = scrape_pitchers()
    db.save_pitchers(pitchers)
    return {'status': 'success'}

if __name__ == '__main__':
    app.run(debug=True)
