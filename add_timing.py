from json import dump, load
from os import path as os_path

def add_timing(name, time, before, repeat, path):
    # Adds a new timing to 'timings.json'. Checks for duplicates before adding.
    new_timing = {
        "name": name,
        "time": time,
        "before": before,
        "repeat": repeat,
        "path": path
    }
    
    if not os_path.exists('timings.json'):
        with open('timings.json', 'w') as file:
            dump([], file)
    
    with open('timings.json', 'r') as file:
        all_timings = load(file)
        
    for timing in all_timings:
        if timing["name"] == new_timing["name"]:
            print(f"Duplicate found: {new_timing['name']}")
            return 1
    
    all_timings.append(new_timing)
    
    with open('timings.json', 'w') as file:
        dump(all_timings, file, indent=4)
    return 0
