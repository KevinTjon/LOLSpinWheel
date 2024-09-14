from mastery_lookup import get_summoner_puuid, get_mastery_score
from champion_lookup import get_champion_name, player_champion_list

def main():
    game_name = input("Enter the summoner's game name: ")
    tag_line = input("Enter the summoner's tage line: ")
    
    print(f"\nGetting player's data")
    response = get_summoner_puuid(game_name, tag_line)
    puuid = response['puuid']
    
    print(f"Getting mastery data")
    mastery_score = get_mastery_score(puuid)
    
    champion_names = get_champion_name(mastery_score)
    
    print(f"Top champs: ")
    for i, name in enumerate(champion_names, 1):
        print(f"{i}. {name}")
    
    player_champion_list(mastery_score)
    print("\nChampion ID and name saved to champion_data.json")

main()
