import requests


def league_input(): # Entry point
    return grab_info('eng.1')

def grab_info(league):
    league_code = 'eng.1'
    year = 2024  # Set the year to 2024
    standings_data = {}  # Initialize a dictionary to hold the standings

    try:
        url = f"https://site.web.api.espn.com/apis/v2/sports/soccer/{league_code}/standings?season={year}"
        response = requests.get(url)
        data = response.json()
        league_name = data['name']
        standings_data['league_name'] = league_name
        standings_data['season_year'] = year
        standings_data['teams'] = []  # List to hold team data

        # Access the standings entries
        entries = data['children'][0]['standings']['entries']
        for team in entries:
            stats = team["stats"]
            team_name = team['team']['name']

            # Extract relevant statistics
            gp = next(s["value"] for s in stats if s["name"] == "gamesPlayed")
            w = next(s["value"] for s in stats if s["name"] == "wins")
            d = next(s["value"] for s in stats if s["name"] == "ties")
            l = next(s["value"] for s in stats if s["name"] == "losses")
            f = next(s["value"] for s in stats if s["name"] == "pointsFor")
            a = next(s["value"] for s in stats if s["name"] == "pointsAgainst")
            gd = next(s["value"] for s in stats if s["name"] == "pointDifferential")
            p = next(s["value"] for s in stats if s["name"] == "points")

            # Append team data to the teams list
            standings_data['teams'].append({
                'team_name': team_name,
                'games_played': gp,
                'wins': w,
                'ties': d,
                'losses': l,
                'points_for': f,
                'points_against': a,
                'point_differential': gd,
                'points': p
            })

    except Exception as e:
        print(f"Error processing year {year}: {e}")
        return {'code': 500, 'message': 'Internal server error.'}

    return standings_data