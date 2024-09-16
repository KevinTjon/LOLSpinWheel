import requests
from riot_api_key import DEV_API_KEY

API_KEY = DEV_API_KEY # API key from riot_api_key.py
REGION_1a = 'americas' # NOTE SOME GET REQUESTS USES 'americas' AND OTHERS USES 'na1' but both are still for NA region
REGION_1b = 'na1'

gameName = "Wagga" # TEST SUMMONER NAME
tagLine = "bagga"

# GET PUUID from summoner name, using LOL account name (eg. "Wagga#bagga")
def get_summoner_puuid(gameName, tagLine):
    url = f'https://{REGION_1a}.api.riotgames.com/riot/account/v1/accounts/by-riot-id/{gameName}/{tagLine}'
    headers = {'X-Riot-Token': API_KEY}
    response = requests.get(url, headers=headers)
    return response.json()

count = 50 # Limits the number of top champions returned
# GET TOP MASTERED CHAMPIONS limited to count
def get_mastery_score(puuid):
    url = f'https://{REGION_1b}.api.riotgames.com/lol/champion-mastery/v4/champion-masteries/by-puuid/{puuid}/top'
    headers = {'X-Riot-Token': API_KEY}
    params = {'count': count}
    response = requests.get(url, params=params, headers=headers)
    
    champion_ids = []
    mastery_data = response.json()
    for i in range(len(mastery_data)):
        champion_id = mastery_data[i]['championId']
        champion_ids.append(champion_id)
    
    return champion_ids

