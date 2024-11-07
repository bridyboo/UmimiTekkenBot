import cv2
import json
import numpy as np
from PIL import Image
import os


Training_data_folder = r"C:\Users\matth\PycharmProjects\trainingDataUmimiBot\TrainingData"

# json for notation count file
notation_counts_file_path = (r"C:\Users\matth\PycharmProjects\trainingDataUmimiBot\TrainingData"
                             r"\TrainingDatanotation_counts.json")

input_index_position = ["back", "forward", "up", "down", "one", "two", "three", "four", "RT", "RB"]


data = np.load(r"C:\Users\matth\PycharmProjects\trainingDataUmimiBot\data\training_data.npy", allow_pickle=True)
targets = np.load(r"C:\Users\matth\PycharmProjects\trainingDataUmimiBot\data\target_data.npy", allow_pickle=True)

print(f'Image Data Shape: {data.shape}')
print(f'targets Shape: {targets.shape}')

# Lets see how many of each type of move we have.
unique_elements, counts = np.unique(targets, return_counts=True)
print(np.asarray((unique_elements, counts)))

# Initialize a dictionary to store counts for each unique notation combination
notation_counts = {}

# Store both data and targets in a list.
# We may want to shuffle down the road.

holder_list = []
for i, image in enumerate(data):
    holder_list.append([data[i], targets[i]])

# Load existing notation counts from the file if it exists
if os.path.exists(notation_counts_file_path):
    with open(notation_counts_file_path, 'r') as file:
        notation_counts = json.load(file)
else:
    notation_counts = {}


# Open a file to write the inputs
with open("input_data.txt", 'w') as input_file:
    last_input = None
    for data in holder_list:
        data[1] = [int(value) for value in data[1].split(',')]  # converts string to int IMPORTANT

        pressed_notations = [input_index_position[i] for i in range(len(data[1])) if data[1][i] == 1]

        if not pressed_notations:
            pressed_notations = ['neutral']

        #if pressed_notations == last_input:
        #    continue  # do not record multiple inputs

        if last_input == pressed_notations and 'neutral' not in pressed_notations:
            continue  # do not record multiple inputs

        last_input = pressed_notations
        print(pressed_notations)

        notation_str = '-'.join(pressed_notations)

        # Write the notation string followed by a newline character to the file
        input_file.write(notation_str + '\n')

# Save the updated notation counts to the file
#with open(notation_counts_file_path, 'w') as file:
 #   json.dump(notation_counts, file)