from add_timing import add_timing

def add_user_timing():
    # Prompts the user to enter a new timing and attempts to add it.
    # Handles input format and calls add_timing function.
    user_input = input('Enter new timing like this: "name, time, before, repeat, path"\n'
                       'Example: "wisdom, 7, 30, True, /path/to/image.png"\n')
    try:
        name, time, before, repeat, path = user_input.split(',')
        name = name.strip()
        time = int(time.strip())
        before = int(before.strip())
        repeat = repeat.strip().lower() == 'true'
        path = path.strip()
        
        result = add_timing(name, time, before, repeat, path)
        if result == 0:
            print(f"Added new timing: {name} at {time} minutes, {before} seconds before, repeat: {repeat}, path: {path}")
        elif result == 1:
            print("Timing was not added due to a duplicate entry.")
        
    except ValueError:
        print("Invalid input format. Please enter the timing in the correct format and try again.")
