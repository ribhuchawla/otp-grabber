import sqlite3
import re
import time
import os
import pyperclip

def get_latest_otp():
    db_path = os.path.expanduser("~/Library/Messages/chat.db")
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT text FROM message ORDER BY date DESC LIMIT 10")
    messages = cursor.fetchall()
    conn.close()

    for (text,) in messages:
        if text:
            match = re.search(r'\b\d{4,8}\b', text)
            if match:
                return match.group()
    return None

last_otp = None
print("✅ OTP Grabber is running...")

while True:
    try:
        otp = get_latest_otp()
        if otp and otp != last_otp:
            pyperclip.copy(otp)
            os.system(f"osascript -e 'display notification \"Copied OTP: {otp}\" with title \"OTP Grabber\"'")
            print(f"📋 Copied OTP: {otp}")
            last_otp = otp
    except Exception as e:
        print(f"⚠️ Error: {e}")
    time.sleep(5)

