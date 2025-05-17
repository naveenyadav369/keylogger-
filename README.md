# keylogger-
# 🛡️ Simple Python Keylogger

> **⚠️ Ethical Notice:**  
> This project is intended **strictly for educational purposes and authorized testing**. Unauthorized usage to monitor others without explicit consent is **illegal and unethical**. Always respect privacy and comply with your local laws.

---

## 📌 Description

This is a simple **Python-based keylogger** that captures and logs keystrokes typed on the keyboard. It is useful for:
- Educational demonstration of keylogging techniques
- Monitoring your own keyboard input for automation or testing
- Learning how keylogging works for ethical hacking and cybersecurity training

Keystrokes are saved to a text file (`keylog.txt`) in real-time.

---

## 🔧 Features

- Captures all printable characters
- Logs special keys like `Enter`, `Backspace`, etc.
- Saves keystrokes to a log file
- Press `ESC` to safely stop the logger
- Minimal and beginner-friendly code

---

## 🧪 Requirements

- Python 3.x
- `pynput` module

Install the required package:

pip install pynput

 Prerequisites
Ensure Python is installed (Python 3 recommended):
python3 --version

If not installed, use:
sudo apt update
sudo apt install python3 python3-pip

📁 Step 1: Clone or Download the Project
If uploaded to GitHub:
git clone https://github.com/naveenyadav369/keylogger-.git
cd keylogger-

Or if you downloaded it manually, just extract the .zip and cd into the folder:


cd keylogger-
📦 Step 2: Install Required Dependencies
Install packages from requirements.txt:


pip3 install -r requirements.txt
This installs:

pynput – Used for listening to keyboard events.

▶️ Step 3: Run the Keylogger
Now execute the keylogger script:


python3 keylogger.py
The script will start logging keystrokes. It may create a log file or print the output depending on how it's written.

🛑 Step 4: Stop the Keylogger
To stop the script:

Press Ctrl + C in the terminal where it’s running

Or, find the process using:


ps aux | grep keylogger
And kill it:


kill <process_id>
📄 Sample requirements.txt

pynput==1.7.6
📋 Sample File Structure

keylogger-/
├── keylogger.py
└── requirements.txt

✅ Optional Tips
To run it in background, you can use:


nohup python3 keylogger.py &
To log output to a file, modify your script to write to a .txt file.



