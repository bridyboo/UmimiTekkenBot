import random
import time
import pathlib
from fastai.vision.all import *
import pyautogui
import pydirectinput
import keyboard
import time
import cv2
from utils.grabscreen import grab_screen
from utils.directkeys import PressKey, ReleaseKey
from utils.getkeys import key_check

input_index_position = ["back", "forward", "up", "down", "one", "two", "three", "four", "RT", "RB"]


# Returns label folder's name to acquire input
def label_func(x): return x.parent.name


# Function responsible for sending input to game
def press_keys(input_combination):
	# Define key mappings for each input
	key_mappings = {
		'back': 'a',
		'forward': 'd',
		'up': 'w',
		'down': 's',
		'one': 'j',
		'two': 'i',
		'three': 'k',
		'four': 'l',
		'RT': 'u',
		'RB': 'o',
	}

	# Store currently pressed keys
	pressed_keys = set()

	# Simulate key presses for the active inputs
	for input_name in input_combination.split('-'):
		if input_name in key_mappings:
			key = key_mappings[input_name]
			keyboard.press(key)
			pressed_keys.add(key)

	# Wait for a short duration (adjust as needed)
	time.sleep(0.05)

	# Release all pressed keys
	for input_name in input_combination.split('-'):
		if input_name in key_mappings:
			key = key_mappings[input_name]
			pydirectinput.keyUp(key)


posix_backup = pathlib.PosixPath
try:
	pathlib.PosixPath = pathlib.WindowsPath

	model_path = Path("C:/Users/matth/PycharmProjects/trainingDataUmimiBot/fine_tuned_model5.0.pkl")
	print("Model Path:", model_path)

	learn_inf = load_learner(model_path)
	print("loaded learner")

	# Sleep time after actions
	sleepy = 0.1

	# Wait for me to push B to start.
	print("Waiting until 'B'")
	keyboard.wait('B')
	time.sleep(sleepy)

	print("Starting model")
	while True:
		image = grab_screen(region=(70, 100, 1600, 900))
		image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
		image = cv2.Canny(image, threshold1=200, threshold2=300)
		image = cv2.resize(image, (224, 224))
		keys = key_check()

		# Debug line to show image
		cv2.imshow("AI Peak", image)
		cv2.waitKey(1)

		start_time = time.time()
		result = learn_inf.predict(image)
		# action = {tuple: 3} ('one-two-three')
		action = result[0]
		print("input: ",action)
		press_keys(action)
		if keys == "H":
			break

finally:
	pathlib.PosixPath = posix_backup

