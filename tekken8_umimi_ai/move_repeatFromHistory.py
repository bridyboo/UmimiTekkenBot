import keyboard
import time
from utils.getkeys import key_check

input_index_position = ["back", "forward", "up", "down", "one", "two", "three", "four", "RT", "RB"]
input_data = r"C:\Users\matth\PycharmProjects\trainingDataUmimiBot\tekken8_umimi_ai\input_data.txt"
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

def press_keys(input_combination, duration, pressed_keys):
    for key in pressed_keys:
        keyboard.release(key)

    # Release all pressed keys if neutral
    if input_combination == 'neutral':
        time.sleep(duration)
        return set()

    for input_name in input_combination.split('-'):
        if input_name in key_mappings:
            key = key_mappings[input_name]
            keyboard.press(key)
            pressed_keys.add(key)

    time.sleep(duration)
    return pressed_keys

def main():
    previous_notation = 'neutral'
    pressed_keys = set()
    while True:

        with open(input_data, "r") as move_history:
            for inputs in move_history:
                start_time = time.perf_counter()

                notation, duration_str = inputs.strip().split('\t')
                duration = int(duration_str.split(":")[1].strip()) / 60

                pressed_keys = press_keys(notation.strip(), duration, pressed_keys)
                print("input: ", inputs)
                end_time = time.perf_counter()
                elapsed_time = end_time - start_time
                if elapsed_time < 1/60:
                    time.sleep(1/60 - elapsed_time)

                previous_notation = notation.strip()
                if keyboard.is_pressed('H'):
                    break
        if keyboard.is_pressed('H'):
            break

    for key in pressed_keys:
        keyboard.release(key)

if __name__ == "__main__":
    print("Waiting until 'B'")
    keyboard.wait('B')
    time.sleep(1.0)
    main()
