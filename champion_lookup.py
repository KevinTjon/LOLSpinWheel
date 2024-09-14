import json
from mastery_lookup import get_summoner_puuid, get_mastery_score
from champion_image_handler import get_champion_image_paths

def load_champion_data():
    with open('Assets/champion-summary.json', 'r') as file:
        data = json.load(file)
    return {int(champ['id']): champ['name'] for champ in data}

def get_champion_name(champion_ids):
    champion_data = load_champion_data()
    return [champion_data.get(champion_id, 'Unknown') for champion_id in champion_ids]

def player_champion_list(mastery_score):
    champion_data = load_champion_data()
    champion_names = get_champion_name(mastery_score)
    image_paths = get_champion_image_paths(champion_names)
    
    player_champs = {}
    for champ_id, champ_name in zip(mastery_score, champion_names):
        player_champs[str(champ_id)] = {
            "name": champ_name,
            "image_path": image_paths.get(champ_name, None)
        }
    
    with open('champion_data.json', 'w', encoding='utf-8') as file:
        json.dump(player_champs, file, indent=2)

    print(f"Found images for {len(image_paths)} out of {len(champion_names)} champions")





