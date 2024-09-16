import json
from mastery_lookup import get_summoner_puuid, get_mastery_score
from champion_image_handler import get_champion_image_paths

# load json file
def load_champion_data():
    with open('Assets/champion-summary.json', 'r') as file:
        data = json.load(file)
    return {int(champ['id']): champ['name'] for champ in data}

# parses the json file and recieve only champion names
def get_champion_name(champion_ids):
    champion_data = load_champion_data()
    return [champion_data.get(champion_id, 'Unknown') for champion_id in champion_ids]

# load champion_role json which would allow sorting champions to specific role
def load_champion_roles():
    with open('champion_role.json', 'r') as file:
        data = json.load(file)
    return data


def player_champion_list(mastery_score, role):
    champion_names = get_champion_name(mastery_score)
    image_paths = get_champion_image_paths(champion_names)
    champion_roles = load_champion_roles()
    
    player_champs = {}
    for champ_id, champ_name in zip(mastery_score, champion_names):
        #edge cases becuase of unconventional names 
        # (original name does not correlate to png name)
        name_mappings = {
            'Aurelion Sol': 'Aurelionsol',
            "K'Sante": 'Ksante',
            "Kha'Zix": 'Khazix',
            "Jarvan IV": 'Jarvaniv',
            "Master Yi": 'Masteryi',
            "Kai'Sa": 'Kaisa',
            "Lee Sin": 'Leesin',
            "Dr. Mundo": 'Drmundo',
            "Twisted Fate": 'twistedfate',
            "Kog'Maw": "kogmaw",
            "Rek'Sai": "reksai",
        }
        original_name = champ_name
        champ_name = name_mappings.get(champ_name, champ_name)
        
        #checks if the champ is in the specified role,
        # if yes save it to the json, else skip champ
        if original_name in champion_roles[role]:
            player_champs[str(champ_id)] = {
                "name": champ_name,
                "image_path": image_paths.get(champ_name, None)
            }
    
    with open('champion_data.json', 'w', encoding='utf-8') as file:
        json.dump(player_champs, file, indent=2)

    print(f"Found images for {len(image_paths)} out of {len(champion_names)} champions")
    print(f"Found {len(player_champs)} champions for {role} role")
    return player_champs




