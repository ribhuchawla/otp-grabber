#!/bin/zsh
cd "$(dirname "$0")"
source otp_env/bin/activate
python3 otp_grabber.py

