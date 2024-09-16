from mastery_lookup import get_summoner_puuid, get_mastery_score
from champion_lookup import get_champion_name, player_champion_list

def main(game_name,tag_line,role):
    game_name = game_name # Riot Summoner name (without the #)
    tag_line = tag_line # Tagline after the # (eg. Na1)
    role = role.lower()

    
    print(f"\nGetting player's data")
    response = get_summoner_puuid(game_name, tag_line)
    puuid = response['puuid']
    
    print(f"Getting mastery data")
    mastery_score = get_mastery_score(puuid)
    
    champion_names = get_champion_name(mastery_score)
    
    print(f"Top champs for {role} role: ")
    player_champs = player_champion_list(mastery_score,role)
    
    for i, (champ_id, champ_data) in enumerate(player_champs.items()):
        print(f"{i}. {champ_data['name']}")
    
        print(f"\nChampion data for {role} role saved to champion_data_{role}.json")

