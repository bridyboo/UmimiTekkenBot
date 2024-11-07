import pydirectinput
import keyboard
import time

from utils.getkeys import key_check

input_index_position = ["back", "forward", "up", "down", "one", "two", "three", "four", "RT", "RB"]
input_data = r"C:\Users\matth\PycharmProjects\trainingDataUmimiBot\tekken8_umimi_ai\input_data.txt1"
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


def press_keys(input_combination, duration, previous_input_combination):
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

	duration = duration / 60
	pressed_keys = set()

	if input_combination == 'neutral':
		# Release all pressed keys
		for key in key_mappings:
			keyboard.release(key_mappings[key])
		pressed_keys.clear()
		# Sleep for the specified duration
		time.sleep(duration)
		print('press: neutral')
		return pressed_keys

	elif previous_input_combination == 'neutral':
		# Press keys directly for the specified duration
		for input_name in input_combination.split('-'):
			if input_name in key_mappings:
				key = key_mappings[input_name]
				keyboard.press(key)
		time.sleep(duration)
		print('press: ', key)
		return pressed_keys

	else:
		# Split the input combination into individual inputs
		inputs = input_combination.split('-')

		# Split the previous input combination into individual inputs
		previous_inputs = previous_input_combination.split('-')

		# Press new keys and release keys not being pressed in the current input
		for input_name in inputs:
			if input_name in key_mappings:
				key = key_mappings[input_name]
				# Press key only if it was not pressed in the previous inputs
				if input_name not in previous_inputs:
					keyboard.press(key)
					print('press:', key)
					pressed_keys.add(key)

		# Release keys that are not being pressed in the current input
		for key in previous_inputs:
			if key not in inputs:
				keyboard.release(key_mappings[key])
				print("release:", key)
			# pressed_keys.remove(key)

	# Wait for the specified duration
	time.sleep(duration)
	return pressed_keys


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
	previous_notation = 'neutral'
	with open(input_data, "r") as move_history:
		# 999 frames is 16.65 seconds
		# Iterate over each input and press the keys
		for inputs in move_history:
			time.sleep(1 / 60)
			# Split the line by '\t' to separate the notation and duration
			notation, duration_str = inputs.strip().split('\t')

			# Extract the duration
			duration = int(duration_str.split(":")[1].strip())

			# Use the notation and sleep for the duration
			print("Notation:", notation)
			print("Sleep duration:", duration)
			keys = key_check()

			press_keys(notation.strip(), duration, previous_notation)  # Strip newline characters from the input string
			print("new input----------")

			previous_notation = notation.strip()
			if keys == "H":
				break

	for keys in key_mappings:
		keyboard.release(key_mappings[keys])


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
# manual()