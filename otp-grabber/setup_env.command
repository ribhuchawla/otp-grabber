#!/bin/zsh
cd "$(dirname "$0")"
python3 -m venv otp_env
source otp_env/bin/activate
pip install pyperclip
echo "✅ Virtual environment set up!"

