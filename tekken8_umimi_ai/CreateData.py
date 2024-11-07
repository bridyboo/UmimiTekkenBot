import numpy as np
import cv2
import time
import os

from utils.grabscreen import grab_screen
from utils.getkeys import key_check
import utils.getKeyXbox as keyXbox


file_name = r"C:\Users\matth\PycharmProjects\trainingDataUmimiBot\data\training_data.npy"
file_name2 = r"C:\Users\matth\PycharmProjects\trainingDataUmimiBot\data\target_data.npy"

directory_name = os.path.dirname(file_name)

if not os.path.exists(directory_name):
    os.makedirs(directory_name)

def get_data():

    if os.path.isfile(file_name):
        print('File exists, loading previous data!')
        image_data = list(np.load(file_name, allow_pickle=True))
        targets = list(np.load(file_name2, allow_pickle=True))
    else:
        print('File does not exist, starting fresh!')
        image_data = []
        targets = []
    return image_data, targets


def save_data(image_data, targets):
    np.save(file_name, image_data)
    np.save(file_name2, targets)


image_data, targets = get_data()
while True:
    keys = key_check()
    print("waiting press B to start")
    if keys == "B":
        print("Starting")
        break

hitboxKeys = keyXbox.XboxController()
count = 0
start_time = time.time()  # Get the start time
while True:
    count +=1
    last_time = time.time()
    image = grab_screen(region=(70, 100, 1600, 900))
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    image = cv2.Canny(image, threshold1=119, threshold2=250)

    image = cv2.resize(image, (424, 424))

    # Debug line to show image
    cv2.imshow("AI Peak", image)
    cv2.waitKey(1)

    # Convert to numpy array
    image = np.array(image)
    image_data.append(image)

    # Calculate the time taken for the loop iteration
    iteration_time = time.time() - start_time

    # If iteration time is less than 1/60 seconds, sleep to maintain 60 FPS
    #if iteration_time < 1 / 60:
    #    time.sleep((1 / 60) - iteration_time)

    start_time = time.time()  # Update the start time for the next iteration

    keys = key_check()
    hitboxKeys_input = hitboxKeys.read()  # reads hitbox input returns a list
    #print(
    #    f"back: {hitboxKeys_input[0]}, forward: {hitboxKeys_input[1]},up:{hitboxKeys_input[2]}, down:{hitboxKeys_input[3]},one:{hitboxKeys_input[4]}, "
    #    f"two: {hitboxKeys_input[5]},three: {hitboxKeys_input[6]}, four: {hitboxKeys_input[7]}, RT: {hitboxKeys_input[8]}, RB: {hitboxKeys_input[9]}")
    targets.append(f"{hitboxKeys_input[0]}, {hitboxKeys_input[1]}, {hitboxKeys_input[2]}, {hitboxKeys_input[3]}, {hitboxKeys_input[4]}, {hitboxKeys_input[5]}, {hitboxKeys_input[6]}, {hitboxKeys_input[7]}, {hitboxKeys_input[8]}, {hitboxKeys_input[9]}\n")

    if keys == "H":
        break

    print('loop took {} seconds'.format(time.time()-last_time))

save_data(image_data, targets)
