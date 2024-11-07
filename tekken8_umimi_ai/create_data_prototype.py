import keyboard
import numpy as np
import cv2
import time
import os

from utils.grabscreen import grab_screen
from utils.getkeys import key_check
import utils.getKeyXbox as keyXbox

file_name2 = r"C:\Users\matth\PycharmProjects\trainingDataUmimiBot\data\frame_time.npy"
file_name = r"C:\Users\matth\PycharmProjects\trainingDataUmimiBot\data\target_data.npy"

directory_name = os.path.dirname(file_name)

if not os.path.exists(directory_name):
    os.makedirs(directory_name)

def get_data():
    if os.path.isfile(file_name):
        print('File exists, loading previous data!')
        targets = list(np.load(file_name, allow_pickle=True))
    else:
        print('File does not exist, starting fresh!')
        targets = []

    return targets

def save_data(targets):
    np.save(file_name, targets)
    #np.save(file_name2, frame_time)


targets = get_data()
while True:
    keys = key_check()
    print("waiting press B to start")
    if keys == "B":
        print("Starting")
        break

hitboxKeys = keyXbox.XboxController()
count = 0

# Initialize frame counter
fps_interval = 1.0/ 60.0
frame_count = 0

last_input = hitboxKeys.read()
while True:
    time.sleep(fps_interval)  # simulate the rate of a 60fps game
    frame_count += 1  # counting frames
    count += 1

    keys = key_check()
    hitboxKeys_input = hitboxKeys.read()  # reads hitbox input returns a list

    # If there's any change in inputs reset the frame counter
    for i in range(len(hitboxKeys_input)):
        if last_input[i] != hitboxKeys_input[i]:
            frame_count = 1
            break

    hitboxKeys_input.append(frame_count)
    print(
        f"back: {hitboxKeys_input[0]}, forward: {hitboxKeys_input[1]},up:{hitboxKeys_input[2]}, down:{hitboxKeys_input[3]},one:{hitboxKeys_input[4]}, "
        f"two: {hitboxKeys_input[5]},three: {hitboxKeys_input[6]}, four: {hitboxKeys_input[7]}, RT: {hitboxKeys_input[8]}, RB: {hitboxKeys_input[9]}, \n frame: {hitboxKeys_input[10]}")
    targets.append(
        f"{hitboxKeys_input[0]}, {hitboxKeys_input[1]}, {hitboxKeys_input[2]}, {hitboxKeys_input[3]}, {hitboxKeys_input[4]}, {hitboxKeys_input[5]}, {hitboxKeys_input[6]}, {hitboxKeys_input[7]}, {hitboxKeys_input[8]}, {hitboxKeys_input[9]}, {hitboxKeys_input[10]}\n")

    last_input = hitboxKeys_input

    if keys == "H":
        break

    #print('loop took {} seconds'.format(time.time() - last_time))

save_data(targets)

# Initialize the frame counter
frame_count = 0


