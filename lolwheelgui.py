import PySimpleGUI as sg
import base64
import json

def load_champion_data():
    #champ_list = []
    with open('champion_data.json', 'r') as file:
        data = json.load(file)
        #takes the champion_data.json and parses it through champ id, returning name 
        champ_list = {str(champ_id): data[champ_id]['name'] for champ_id in data} 
    return champ_list

def get_champ_data():
    champ_list = load_champion_data()
    # returns only the champ names and removes its id
    return [champ_list.get(str(champ_id), (f"Unknown Champ({champ_id})")) for champ_id in champ_list]

champion_list = get_champ_data()
print(champion_list)

#champion_list = ["aatrox","ivern"]


# takes in champion name in lowercase
# returns base64 encoded image
def card_load(champion_name_lowercase):
    image_file = f"Assets/{champion_name_lowercase.lower()}/skins/base/{champion_name_lowercase.lower()}loadscreen.png"
    #image_file = f"champion_assets/{champion_name_lowercase.lower()}_loading.png"

    #rb is binary mode, we need this to convert to base 64 ideally
    with open(image_file,"rb") as opened_file:
        
        image_bytes = opened_file.read() # these are the bytes
        
        base64_image_bytes = base64.b64encode(image_bytes)
    
    return base64_image_bytes # this is the image in base64
    #now image should be readable by pysimplegui


     

    
# setup the five slots

slot1 = [card_load("mystery"), "?"]

slot2 = [card_load("mystery"), "?"]

slot3 = [card_load("mystery"), "?"]

slot4 = [card_load("mystery"), "?"]

slot5 = [card_load("mystery"), "?"]


# slot variable:
# array
# base 64data , name

#example

# slot1 = [aatrox_base64, "Aatrox"]
# unflipped:
# slot1 [preflip_base64, "Champion 1"]

# example used to show set slots
# for i in range(0,5):
#     slot{i} = card_load(champion(i))

# slot1
# slot2
# slot3
# slot4
# slot5

# All the stuff inside your window.
layout = [  [sg.Image(slot1[0], key="-slot1_champion_image-"), sg.Image(slot2[0], key="-slot2_champion_image-"), sg.Image(slot3[0], key="-slot3_champion_image-"), sg.Image(slot4[0], key="-slot4_champion_image-"), sg.Image(slot5[0], key="-slot5_champion_image-")],
            [sg.Text(slot1[1] ,key='-slot1_champion_name-'), sg.Text(slot2[1] ,key='-slot2_champion_name-'), sg.Text(slot3[1] ,key='-slot3_champion_name-'), sg.Text(slot4[1] ,key='-slot4_champion_name-'), sg.Text(slot5[1] ,key='-slot5_champion_name-')],
            [sg.Button('Reveal'), sg.Button('Shuffle', key='shuffle_button')],
            [sg.Button('Ok')] ]


# Create the Window
window = sg.Window('Window Title', layout)

next_reveal= 0
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Ok': # if user closes window or clicks cancel
        break
    if next_reveal>=2:
        window['shuffle_button'].update(visible = False)
    if event == 'shuffle_button' and next_reveal<3: # can only shuffle if see less than 3
        print("next reveal",next_reveal)
        window[f"-slot1_champion_image-"].update(card_load("mystery"))
        window[f"-slot1_champion_name-"].update("?")

        window[f"-slot2_champion_image-"].update(card_load("mystery"))
        window[f"-slot2_champion_name-"].update("?")

        champion_list = champion_list[5:]
        next_reveal=0
        print("samoyed")
    if event == 'Reveal':
        next_card_base64 = card_load(champion_list[next_reveal])
        next_card_name = champion_list[next_reveal]
        window[f"-slot{next_reveal+1}_champion_image-"].update(next_card_base64)
        window[f"-slot{next_reveal+1}_champion_name-"].update(next_card_name) 
        next_reveal = (next_reveal+1)%5
    

window.close()


# 