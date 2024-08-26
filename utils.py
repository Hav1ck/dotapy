from json import dump, load
from os import path

global_file = "globals.json"  # Path to the global settings file
timing_file = "timings.json"  # Path to the timings file

def load_globals():
    # Loads global settings from 'globals.json'. If the file does not exist, returns default settings.
    if path.exists(global_file):
        with open(global_file, 'r') as file:
            return load(file)
    else:
        return {
            "running": 0,
            "stop_timer": 0,
            "timer": 0,
            "path": '',
            "priority": 0,
            "stop_gui": 0
        }

def save_globals(data):
    # Saves global settings to 'globals.json', excluding the 'timings' key.
    data_to_save = {key: value for key, value in data.items() if key != 'timings'}
    with open(global_file, 'w') as file:
        dump(data_to_save, file, indent=4)

def load_timings():
    # Loads timings from 'timings.json'. If the file does not exist, returns an empty dictionary.
    if path.exists(timing_file):
        with open(timing_file, 'r') as file:
            return load(file)
    else:
        return {}

def get_timer_seconds():
    # Retrieves the timer value from 'globals.json'.
    # Returns the timer value, or 0 if the timer key does not exist.
    with open(global_file, 'r') as file:
        data = load(file)
    return data.get('timer', 0)
