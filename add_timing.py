import json
import os

def add_timing(name, time, before, repeat, path):
    # Adds a new timing to 'timings.json'. Checks for duplicates before adding.
    # Args:
    #     name (str): The name of the timing.
    #     time (int): The time in minutes.
    #     before (int): The time in seconds before the event.
    #     repeat (bool): Whether the timing should repeat.
    #     path (str): The path associated with the timing.
    # Returns:
    #     int: 0 if successful, 1 if a duplicate entry was found.
    new_timing = {
        "name": name,
        "time": time,
        "before": before,
        "repeat": repeat,
        "path": path
    }
    
    if not os.path.exists('timings.json'):
        with open('timings.json', 'w') as file:
            json.dump([], file)
    
    with open('timings.json', 'r') as file:
        all_timings = json.load(file)
        
    for timing in all_timings:
        if timing["name"] == new_timing["name"]:
            print(f"Duplicate found: {new_timing['name']}")
            return 1
    
    all_timings.append(new_timing)
    
    with open('timings.json', 'w') as file:
        json.dump(all_timings, file, indent=4)
    return 0
