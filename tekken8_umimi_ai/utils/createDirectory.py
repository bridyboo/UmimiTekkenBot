import cv2
import numpy as np
from PIL import Image
import os


Training_data_folder = r"C:\Users\matth\PycharmProjects\trainingDataUmimiBot\TrainingData"

data = np.load(r"C:\Users\matth\PycharmProjects\trainingDataUmimiBot\data\training_data.npy", allow_pickle=True)
targets = np.load(r"C:\Users\matth\PycharmProjects\trainingDataUmimiBot\data\target_data.npy", allow_pickle=True)

input_index_position = ["back", "forward", "up", "down", "one", "two", "three", "four", "RT", "RB"]

holder_list = []
for i, image in enumerate(data):
    holder_list.append([data[i], targets[i]])

count_up = 0
count_left = 0
count_right = 0
count_jump = 0
count_dict = 0

for data in holder_list:
    data[1] = [int(value) for value in data[1].split(',')]  # converts string to int
    image_data = np.array(data[0], dtype=np.uint8)  # Convert to uint8
    image_data = Image.fromarray(image_data)  # Convert to PIL Image

    #print(data[1])
    #print(range(len(data[1]))
    pressed_notations = [input_index_position[i] for i in range(len(data[1])) if data[1][i] == 1]

    if not pressed_notations:
        pressed_notations = ['neutral']

    notation_str = '-'.join(pressed_notations)

    unique_dir = rf"{Training_data_folder}\{notation_str}"
    os.makedirs(unique_dir, exist_ok=True)



