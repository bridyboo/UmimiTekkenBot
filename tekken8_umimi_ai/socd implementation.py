from utils.directkeys import PressKey, ReleaseKey, W, D, A
import keyboard
from utils.getkeys import key_check
import time

# Sleep time after actions
sleepy = 0.1

# Wait for me to push B to start.
keyboard.wait('B')
time.sleep(sleepy)

while True:

    keyboard.press('A')
    # End simulation by hitting h
    keys = key_check()
    if keys == "H":
        break