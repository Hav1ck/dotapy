# gui.py
import customtkinter
from PIL import Image
import threading
import time
from utils import load_globals, save_globals
from tkinter import TclError

def launch_app(path, before):
    # Start a separate thread to launch the app with a delay
    timer_thread = threading.Thread(target=launch_app2, args=(path, before,))
    timer_thread.start()

def launch_app2(path, before):
    # Wait for 2 seconds before launching the GUI
    time.sleep(2)
    globals = load_globals()
    globals['stop_gui'] = 0
    save_globals(globals)
    gui(path, before)

def gui(path, before):
    # Define the dimensions of the GUI window
    HEIGHT = 100
    WIDTH = 100
    gui_timer = 0

    def update_gui():
        nonlocal gui_timer, before
        globals_data = load_globals()

        # Update the timer and check if the GUI should be stopped
        if gui_timer <= before:
            gui_timer += 1
            if app.winfo_exists():
                app.after(1000, update_gui)

        if globals_data['stop_gui'] == 1:
            # If stop_gui flag is set, destroy the GUI
            globals_data['stop_gui'] = 0
            save_globals(globals_data)
            if app.winfo_exists():
                print("stop gui destroy")
                app.destroy()
        elif gui_timer > before:
            # After the timer expires, destroy the GUI
            globals_data['priority'] = 0
            save_globals(globals_data)
            if app.winfo_exists():
                print("else destroy")
                app.destroy()

    # Create the main application window using customtkinter
    app = customtkinter.CTk()
    app.title("timer")
    app.resizable(False, False)

    # Position the window at the center-top of the screen
    screen_width = app.winfo_screenwidth()
    x_position = int((screen_width / 2) - (WIDTH / 2))
    y_position = 50
    app.geometry(f"{WIDTH}x{HEIGHT}+{x_position}+{y_position}")

    # Set window properties: always on top and transparent background
    app.overrideredirect(True)
    app.attributes("-topmost", True)
    app.wm_attributes("-transparentcolor", "black")
    app.configure(bg='black')

    # Load the image to display in the GUI
    img = Image.open(path).convert('RGBA')
    Label1 = customtkinter.CTkLabel(master=app, text="", image=customtkinter.CTkImage(img, size=(100, 100)), bg_color='black')
    Label1.place(x=0, y=0)

    # Start updating the GUI
    update_gui()

    # Start the GUI event loop and handle exceptions if the window is already closed
    try:
        app.mainloop()
    except TclError:
        print("GUI already destroyed")