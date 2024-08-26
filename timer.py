from time import sleep
from threading import Thread
from gui import launch_app
from utils import load_globals, save_globals, load_timings

timings = []

def subtract_x(value):
    # Subtract a given value from the current timer value
    globals = load_globals()
    globals['timer'] -= value
    save_globals(globals)

def add_x(value):
    # Add a given value to the current timer value
    globals = load_globals()
    globals['timer'] += value
    save_globals(globals)

def format_timer(seconds):
    # Format the timer in minutes and seconds (MM:SS format)
    minutes = seconds // 60
    seconds = seconds % 60
    return f"{minutes:02}:{seconds:02}"

def run_timer():
    timings = load_timings()
    globals = load_globals()

    # Stop the running timer if it's already active
    if globals['running'] == 1:
        globals['stop_timer'] = 1
        globals['running'] = 0
        save_globals(globals)
        sleep(1)
        globals['stop_timer'] = 0
        globals['running'] = 0
        save_globals(globals)
        return

    # Initialize and start the timer
    globals['timer'] = 0
    globals['running'] = 1
    save_globals(globals)

    while globals['stop_timer'] == 0:
        globals = load_globals()
        formatted_time = format_timer(globals['timer'])
        print(f"Current Timer: {formatted_time}")

        if not timings:
            print("No events in the timings list.")
        else:
            for timing in timings:
                event_time = timing["time"] * 60
                before = timing["before"]
                repeat = timing["repeat"]
                overall_time = globals['timer']
                name = timing['name']
                path = timing["path"]
                priority = globals['priority']

                # Check if an event should occur based on the timer and priority
                if priority < count_priority(repeat, event_time):
                    if not repeat:
                        if overall_time == event_time - before:
                            globals['stop_gui'] = 1
                            globals['priority'] = 100
                            save_globals(globals)
                            print(f"Event '{name}' happening in {before} seconds!")
                            launch_app(path, before)

                    if repeat:
                        # Adjust for repeated events
                        while overall_time > event_time:
                            event_time += timing["time"] * 60
                        if overall_time == event_time - before:
                            globals['stop_gui'] = 1
                            globals['priority'] = count_priority(repeat, event_time)
                            save_globals(globals)
                            print(f"Event '{name}' happening in {before} seconds!")
                            launch_app(path, before)

        # Increment the timer every second
        sleep(1)
        globals = load_globals()
        globals['timer'] += 1
        save_globals(globals)

def start_run_timer():
    # Start the timer in a separate thread
    timer_thread = Thread(target=run_timer)
    timer_thread.start()

def count_priority(repeat, event_time):
    # Calculate the priority of an event based on its repeat status and event time
    if repeat:
        return event_time / 60
    return 100  # Default priority for non-repeated events