# 📱 DroidTap Forge: ADB Touch Automation Lab 🤖

> A precision-engineered Python script designed for educational testing environments to simulate coordinate-based touch interactions and UI workflows on Android devices using **ADB (Android Debug Bridge)**.

---

## 🚀 Step-by-Step Implementation Guide

Follow these steps to set up, map, and execute the automation tool in your testing environment:

### 🛠️ Step 1: Unlock Developer Options
Before interacting with the device programmatically, enable developer privileges:
* Head over to your device **Settings** ⚙️.
* Scroll down and select **About Phone** (or Software Information).
* Locate the **Build Number** and tap it **7 times** consecutively until you see the *"You are now a developer!"* toast message.
* Return to the main Settings menu and open the newly unlocked **Developer Options**.

### 📍 Step 2: Enable Pointer Location for Coordinates
To map the exact touch targets on your dummy lock interface:
* Inside **Developer Options**, find the **Pointer Location** toggle and switch it **ON** 🔍.
* Touch any key on your target screen (e.g., your keypad digits). The top of your screen will instantly display real-time **X and Y pixel coordinates**.
* Note down the exact `(x, y)` coordinates for each digit (`0–9`) from your layout.

### ⚙️ Step 3: Configure the Python Script
1. Open your Python script (`lock_cracker.py`) in your favorite editor.
2. Update the `digit_coords` dictionary with your device's specific pixel coordinates:
   ```python
   digit_coords = {
       '1': (360, 750),
       '2': (540, 750),
       # Add your mapped coordinates for remaining digits here
   }

▶️ Step 4: Run the Automation

Connect your Android device via USB and ensure USB Debugging is authorized.

Verify the connection in your terminal:
Bash

adb devices

Execute your script to stream the touch injection sequence:

Bash

python lock_cracker.py


⚠️ Educational Disclaimer
This tool is strictly built for educational purposes, local UI testing, and automated layout verification within controlled developer environments. Do not use automation scripts against unauthorized or personal production security barriers.
