import keyboard
from add_user_timing import add_user_timing
from add_timing import add_timing
from timer import start_run_timer, subtract_x, add_x
from default_globals import save_defaults
from update_checker import check_for_update

if __name__ == "__main__":
    # Check for any available updates to the script
    check_for_update()
    
    # Save the default global settings (e.g., timers and state)
    save_defaults()

    # Add various timings to the timing list
    add_timing("wisdom", 7, 30, True, "assets\\wisdom.png")
    add_timing("active rune", 2, 30, True, "assets\\active_rune.webp")
    add_timing("tormentor", 20, 60, False, "assets\\tormentor.webp")
    add_timing("neutralt1", 7, 10, False, "assets\\neutral.png")
    add_timing("neutralt2", 17, 10, False, "assets\\neutral.png")
    add_timing("neutralt3", 27, 10, False, "assets\\neutral.png")
    add_timing("neutralt4", 37, 10, False, "assets\\neutral.png")
    add_timing("neutralt5", 60, 30, False, "assets\\neutral.png")

    # Bind hotkeys for adding user timings and controlling the timer
    keyboard.add_hotkey('F7', add_user_timing)
    keyboard.add_hotkey('F8', start_run_timer)
    keyboard.add_hotkey('alt+F7', subtract_x, args=(1,))
    keyboard.add_hotkey('alt+F8', add_x, args=(1,))
    keyboard.add_hotkey('ctrl+alt+F7', subtract_x, args=(60,))
    keyboard.add_hotkey('ctrl+alt+F8', add_x, args=(60,))
    keyboard.add_hotkey('ctrl+F7', subtract_x, args=(10,))
    keyboard.add_hotkey('ctrl+F8', add_x, args=(10,))

    # Wait for the 'esc' key to exit the script
    keyboard.wait('esc')
