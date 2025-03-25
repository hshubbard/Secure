import subprocess
import sys
import time

# Function to install missing packages
def install_package(package):
    try:
        __import__(package)  # Try importing
    except ImportError:
        print(f"{package} not found. Installing...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])

# Ensure pynput is installed before using it
install_package("pynput")

# Utilize pynput library after importing
from pynput.mouse import Button, Controller 


mouse = Controller()

# Read pointer position
print('The current pointer position is {}'.format(
    mouse.position))
time.sleep(1)

# Set pointer position
mouse.position = (0, 0)
print('Pointer position: {}'.format(
    mouse.position))
time.sleep(1)

# Move pointer relative to current position
for i in range(1080 // 40):
    for j in range (1920):
        mouse.move(1, 0)
        print('Pointer position: {}'.format(
    mouse.position))
    mouse.move(-1920, 40)


