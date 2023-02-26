import requests
import sys

def extract_data():
    url = "https://odds.p.rapidapi.com/v4/sports/mma_mixed_martial_arts/odds"

    querystring = {"regions":"us","markets":"h2h,spreads","oddsFormat":"decimal","include":"event", "dateFormat":"iso"}

    headers = {
        "X-RapidAPI-Key": "5cdea7daa4msh0875746a30d7fc4p140724jsnac41d2adbba3",
        "X-RapidAPI-Host": "odds.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    if response.status_code == 200:
        return response.json()
    else:
        sys.exit(f'Error w/ request status code: {response.status_code}')

main_data = extract_data()

if __name__ == "__main__":
    print(extract_data())