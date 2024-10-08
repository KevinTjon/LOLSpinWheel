import os
 # Currently not using in the GUI. Finds the path for the champion assets and save the path to
 # champion_data.json

 # This function iteratively goes through the Assets file to find the loadscreen png for all champs
def find_champion_image_path(champion_name):
    assets_folder = 'Assets'
    
    for folder in os.listdir(assets_folder):
        folder_path = os.path.join(assets_folder, folder)
        if os.path.isdir(folder_path) and champion_name.lower() in folder.lower():
            base_path = os.path.join(folder_path, 'skins', 'base')
            if os.path.exists(base_path):
                for file in os.listdir(base_path):
                    if file.startswith(champion_name.lower()) and file.lower().endswith('loadscreen.png'):
                        image_path = os.path.join(base_path, file)
                        return image_path
    print(f"Image not found for {champion_name}")
    return None

# Attempts to find the specifi champion loadscreen by matching champ name and calling the
# finding_Champion_image_path function
def get_champion_image_paths(champion_names):
    image_paths = {}
    for name in champion_names:
        #edge cases becuase of unconventional names
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
            'Tahm Kench ': 'tahmkench',
        }
        # Use the mapping if it exists, otherwise keep the original name
        name = name_mappings.get(name, name)
        path = find_champion_image_path(name)
        if path:
            image_paths[name] = path
        else:
            print(f"Image not found for {name}")
    return image_paths