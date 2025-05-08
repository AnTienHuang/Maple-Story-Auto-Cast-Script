# Key Automation Script
A Python script that automates keyboard inputs by simulating long presses of multiple keys in sequence.
Description
This script uses PyAutoGUI to simulate long presses of the 'Z' key, left arrow key, and right arrow key, with configurable timing between presses and sequences. It's designed to run on macOS and provides a way to automate repetitive keyboard input patterns.

# Features
- Long presses of 'Z', left arrow, and right arrow keys in sequence
- Configurable duration for how long each key is held down
- Adjustable delays between key presses and sequences
- Safety feature to ensure keys are released if the script is interrupted
- Built-in delay at the start to allow for switching to your target application

# Requirements
Python 3.x
PyAutoGUI library

# Installation
1. Install Python 3 from python.org if not already installed
2. Install the required PyAutoGUI package:
```pip3 install pyautogui```
3. Download the script and make it executable:
```chmod +x kb_loop.py```

# Usage
1. Open your terminal and navigate to the directory containing the script
2. Run the script:
```python3 kb_loop.py```
3. You'll have 5 seconds to switch to your target application before the script begins
4. To stop the script, press Ctrl+C in the terminal window

# Customisation
You can customise the script by modifying these values:
- Key press duration: Change the time.sleep(1) value between keyDown() and keyUp() calls
- Delay between keys: Adjust the time.sleep(0.5) values between different key presses
- Sequence interval: Modify the time.sleep(5) value at the end of each sequence
- Keys used: Replace 'Z', 'left', and 'right' with other keys as needed

# Important Notes
- Using automation scripts may violate the Terms of Service for some applications, particularly games
- Some applications might have anti-cheat systems that detect and block automated inputs
- The script's effectiveness depends on the target application and how it processes keyboard inputs
- Always ensure you have permission to use automation tools with your target application

# Troubleshooting

## Permissions: 
For macOS, you may need to grant Terminal (or your Python IDE) accessibility permissions in System Preferences > Security & Privacy > Privacy > Accessibility
## Key recognition: 
Some applications may not recognise simulated key presses the same way as physical key presses
Focus issues: The script sends keystrokes to whichever application has focus, so make sure your target app stays in focus

# License
This script is provided as-is under the MIT License. Feel free to modify and distribute as needed.

# Disclaimer
This script is provided for educational purposes only. Use at your own risk. The authors are not responsible for any consequences resulting from the use of this script.
