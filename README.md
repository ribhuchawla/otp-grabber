
# OTP Grabber for macOS

Automatically detects OTPs from incoming iMessages on your Mac, copies them to your clipboard, and shows a native macOS notification — all running silently in the background.

✅ Works on all Macs with iMessage enabled  
✅ No need for cloud access or browser extensions  
✅ Launches on login and stays out of your way

---

## 🚀 Features

- Detects 4–8 digit OTPs from iMessages via macOS's local Messages database
- Automatically copies new OTPs to your clipboard
- Sends a native Mac notification: _"Copied OTP: 123456"_
- Lightweight, fast, runs in background
- No external API calls, fully offline

---

## 🧰 Requirements

- macOS with iMessage enabled and synced
- Python 3.8+
- Terminal + Full Disk Access granted to Terminal (one-time setup)

---

## 📦 Setup (First Time Only)

1. **Download or clone this repo:**

    ```bash
    git clone https://github.com/ribhuchawla/otp-grabber.git
    cd otp-grabber-mac
    ```

2. **Run the setup script:**

    ```bash
    ./setup_env.command
    ```

    This creates a Python virtual environment and installs the required packages.

3. **Grant Full Disk Access to Terminal:**

    - Open **System Settings → Privacy & Security → Full Disk Access**
    - Add **Terminal.app** and **python3** (drag from `/opt/homebrew/bin/python3`)
    - Quit and reopen Terminal

4. **Test it manually:**

    ```bash
    ./otp_grabber.command
    ```

    You should see:

    ✅ OTP Grabber is running...  
    📋 Copied OTP: 123456

---

## 🔄 Auto-Launch on Login

To have it run every time you boot your Mac:

- Open **System Settings → General → Login Items**
- Click `+` and add `otp_grabber.command` from the project folder

---

## 🧪 How to Test

Send yourself an iMessage like:

    Your verification code is 987654

You should receive a notification and find `987654` in your clipboard immediately.

---

## 📁 Project Structure

```
otp-grabber/
├── otp_grabber.py          # Core script that reads iMessages
├── otp_grabber.command     # Double-click to run
└── setup_env.command       # One-time environment setup
```

---

## 🛑 Disclaimer

- This tool accesses your local iMessage database.
- Use responsibly and only on your own devices.
- Tested on macOS Ventura and Sonoma with Python 3.11 and 3.13.

---

## 🙌 Credits

Created by Ribhu Chawla(https://github.com/ribhuchawla) to scratch an itch.  
Feel free to fork, extend, or contribute!
