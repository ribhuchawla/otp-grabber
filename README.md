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

1. **Download this repo or unzip the package**

2. **Run the setup script to initialize the environment**

```bash
cd ~/Library/Application\ Support/otp-grabber
./setup_env.command
```

3. **Grant Full Disk Access to Terminal:**

- Go to **System Settings → Privacy & Security → Full Disk Access**
- Add **Terminal.app** and **/opt/homebrew/bin/python3**
- Quit and reopen Terminal

4. **Install the launch agent**

```bash
cp com.ribhu.otpgrabber.plist ~/Library/LaunchAgents/
launchctl load ~/Library/LaunchAgents/com.ribhu.otpgrabber.plist
```

✅ You’re done! It now runs silently on every boot.

---

## 🧪 How to Test

Send yourself an iMessage like:

```
Your OTP is 987654
```

You should:
- Get a native Mac notification
- Be able to paste the OTP immediately (`Cmd + V`)

---

## 📁 Project Structure

```
otp-grabber/
├── otp_grabber.py              # Core script that reads iMessages
├── setup_env.command           # One-time environment setup
├── com.ribhu.otpgrabber.plist  # LaunchAgent for background execution
└── README.md                   # This file
```

---

## 🛑 Disclaimer

- This tool accesses your local iMessage database.
- Use responsibly and only on your own devices.
- Tested on macOS Ventura and Sonoma with Python 3.11 and 3.13.

---

## 🙌 Credits

Created by [Ribhu Chawla](https://github.com/yourusername)  
PRs welcome!
