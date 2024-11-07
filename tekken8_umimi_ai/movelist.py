import pydirectinput
import keyboard
import time

from utils.getkeys import key_check

input_index_position = ["back", "forward", "up", "down", "one", "two", "three", "four", "RT", "RB"]
input_data = r"C:\Users\matth\PycharmProjects\trainingDataUmimiBot\tekken8_umimi_ai\input_data.txt"


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
	if input_combination == 'neutral':
		pressed_keys = keyboard._pressed_events
		# Release each key
		for key in pressed_keys:
			keyboard.release(key)

		time.sleep(1/60)
		return

	elif '-' in input_combination:
		# Simulate key presses for the active inputs
		inputs = input_combination.split('-')
		for idx, input_name in enumerate(inputs):
			if input_name in key_mappings:
				key = key_mappings[input_name]
				# Press key only if not already pressed
				if key not in pressed_keys:
					keyboard.press(key)
					pressed_keys.add(key)
				# If next input contains a prefix of current input, do not release keys
				if idx < len(inputs) - 1 and inputs[idx + 1].startswith(input_name):
					continue

		# Wait for a short duration (adjust as needed)
		time.sleep(0.05)

		# Release all pressed keys
		for input_name in input_combination.split('-'):
			if input_name in key_mappings:
				key = key_mappings[input_name]
				if key in pressed_keys:
					keyboard.release(key)
					pressed_keys.remove(key)
	else:
		if input_combination in key_mappings:
			key = key_mappings[input_combination]
			# Press key only if not already pressed
			if key not in pressed_keys:
				keyboard.press(key)
				pressed_keys.add(key)
			time.sleep(1/60)
			if key in pressed_keys:
				keyboard.release(key)
				pressed_keys.remove(key)


# movelist
ewgf = ['forward', 'neutral', 'down', 'down-forward-two']
db4 = ['down-back-four']
onetwofourthree = ['one', 'two', 'four', 'three']
pewgf = ['forward', 'neutral', 'down-forward-two']
hellsweep = ['forward', 'neutral', 'down', 'down-forward-four', 'one']
wavedash = ['forward', 'neutral', 'down', 'down-forward']
dash = ['forward', 'forward']
backdash = ['back', 'back']
koreanbd = ['back', 'back', 'down-back', 'back']
koreanbd2 = ['back', 'down-back', 'back']

# Wait for me to push B to start.
print("Waiting until 'B'")
keyboard.wait('B')
time.sleep(1.0)


def main():
	# Read input data from the file and store them in a list
	with open(input_data, "r") as move_history:
		all_inputs = move_history.readlines()


	#999 frames is 16.65 seconds
	# Iterate over each input and press the keys
	for inputs in all_inputs:
		start_time = time.time()  # Get the start time
		keys = key_check()

		# Calculate the time taken for the loop iteration
		iteration_time = time.time() - start_time
		# If iteration time is less than 1/60 seconds, sleep to maintain 60 FPS
		if iteration_time < 1 / 60:
			time.sleep((1 / 60) - iteration_time)

		press_keys(inputs.strip())  # Strip newline characters from the input string
		# Introduce a delay to allow the game to register the input
		#time.sleep(0.003)  # Adjust as needed

		if keys == "H":
			break

def manual():
	count = 0
	while True:
		keys = key_check()
		move = ewgf[count]
		print(move)
		press_keys(move)
		count += 1

		if count >= len(ewgf):
			count = 0
			time.sleep(0.59)

		if keys == "H":
			break


if __name__ == "__main__":
	main()
	#manual()