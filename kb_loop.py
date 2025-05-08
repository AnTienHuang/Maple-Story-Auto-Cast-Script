#!/usr/bin/env python3
"""
macOS Keyboard Long Press Loop Script
This script long-presses the 'Z' key and repeats indefinitely.
"""

import pyautogui
import time
import random

# Add a small delay before starting to give you time to switch windows
print("Script will start in 5 seconds. Switch to your target window.")
time.sleep(5)

try:
    while True:
        # Add randomness to avoid anti-cheat dectection
        n = random.randint(2, 5)
        # Add movement to avoid afk detection
        pyautogui.keyDown('right')
        time.sleep(n)
        pyautogui.keyUp('right')
        time.sleep(n)
        pyautogui.press('down')
        time.sleep(1)
        pyautogui.press('left')
        time.sleep(1)
        print("Pressing and holding 'Z' key...")
        pyautogui.keyDown('Z')
        time.sleep(n)
        pyautogui.keyUp('Z')
        print(f"Released 'Z' key, waiting for {n} seconds...")
        
        # cool down
        time.sleep(n * 5)
        
except KeyboardInterrupt:
    pyautogui.keyUp('Z')
    print("\nScript terminated by user.")