import requests
import sys
import json

def extract_data(): # from rapidapi
    with open('./data.json', 'r') as f:
        api_key = json.load(f)["rapidapi-key"] # your api-key from rapidapi.com

    url_odds = "https://odds.p.rapidapi.com/v4/sports/mma_mixed_martial_arts/odds"
    querystring = {"regions":"us","markets":"h2h,spreads","oddsFormat":"decimal","include":"event", "dateFormat":"iso"}
    headers = {
        "X-RapidAPI-Key": api_key,
        "X-RapidAPI-Host": "odds.p.rapidapi.com"
    }

    response = requests.get(url_odds, headers=headers, params=querystring)

    if response.status_code == 200:
        return response.json()
    else:
        sys.exit(f'Error w/ request status code: {response.status_code}')

def get_event_data(date): # from sportsdata.io
    with open('./data.json', 'r') as f:
        api_key = json.load(f)["sportsdata-key"] # your api-key from sportsdata.io

    url_event_id = "https://api.sportsdata.io/v3/mma/scores/json/Schedule/UFC/2023"

    response = requests.get(url_event_id, headers={"Ocp-Apim-Subscription-Key": api_key})

    if response.status_code == 200:
        sample = response.json()

        for i in range(len(sample)):
            if sample[i]["Day"][:10] == date:
                return sample[i]["EventId"]
            
    else:
        sys.exit(f'Error w/ request status code: {response.status_code}')

def get_event_result(eventID):
    with open('./data.json', 'r') as f:
        api_key = json.load(f)["sportsdata-key"]

    url_event_result = f"https://api.sportsdata.io/v3/mma/scores/json/Event/{eventID}"

    response = requests.get(url_event_result, headers={"Ocp-Apim-Subscription-Key": api_key})

    if response.status_code == 200:
        sample = response.json()

        winners = []
        print('winners: ', end='')

        for i in range(len(sample["Fights"])):
            if sample["Fights"][i]["Fighters"][0]["Winner"] == True:
                winners.append(f'{sample["Fights"][i]["Fighters"][0]["FirstName"]} {sample["Fights"][i]["Fighters"][0]["LastName"]}')
                print(f'{sample["Fights"][i]["Fighters"][0]["FirstName"]} {sample["Fights"][i]["Fighters"][0]["LastName"]}', end=', ')
            elif sample["Fights"][i]["Fighters"][1]["Winner"] == True:
                winners.append(f'{sample["Fights"][i]["Fighters"][1]["FirstName"]} {sample["Fights"][i]["Fighters"][1]["LastName"]}')
                print(f'{sample["Fights"][i]["Fighters"][1]["FirstName"]} {sample["Fights"][i]["Fighters"][1]["LastName"]}', end=', ')
            else: pass

        return winners

    else:
        sys.exit(f'Error w/ request status code: {response.status_code}')

# main_data = extract_data()

if __name__ == "__main__":
    get_event_result(get_event_data('2023-01-14'))
