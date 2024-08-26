from json import dump

def save_defaults():
    # Saves default global settings to 'globals.json'.
    global_data = {
        "running": 0,
        "stop_timer": 0,
        "timer": 0,
        "stop_gui": 0, 
        "priority": 0
    }
    
    with open('globals.json', 'w') as file:
        dump(global_data, file, indent=4)
