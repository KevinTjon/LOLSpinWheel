import os

def find_champion_image_path(champion_name):
    assets_folder = 'Assets'
    
    for folder in os.listdir(assets_folder):
        folder_path = os.path.join(assets_folder, folder)
        if os.path.isdir(folder_path) and champion_name.lower() in folder.lower():
            base_path = os.path.join(folder_path, 'skins', 'base')
            if os.path.exists(base_path):
                for file in os.listdir(base_path):
                    print(champion_name.lower())
                    if file.startswith(champion_name.lower()) and file.lower().endswith('loadscreen.jpg'):
                        image_path = os.path.join(base_path, file)
                        return image_path
    print(f"Image not found for {champion_name}")
    return None

def get_champion_image_paths(champion_names):
    image_paths = {}
    for name in champion_names:
        #edge cases becuase of space in name
        if name == 'Aurelion Sol': 
            name = 'Aurelionsol'
        if name == "K'Sante":
            name = 'Ksante'
        path = find_champion_image_path(name)
        if path:
            image_paths[name] = path
        else:
            print(f"Image not found for {name}")
    return image_paths