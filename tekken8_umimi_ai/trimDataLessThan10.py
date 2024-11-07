import os
import shutil
import json

training_data_folder = r"C:\Users\matth\PycharmProjects\trainingDataUmimiBot\TrainingData"
notation_counts_file_path = os.path.join(training_data_folder, "TrainingDatanotation_counts.json")

def delete_folders_with_less_than_10_files(folder_path):
    with open(notation_counts_file_path, 'r') as f:
        notation_counts = json.load(f)

    for root, dirs, files in os.walk(folder_path):
        for directory in dirs:
            dir_path = os.path.join(root, directory)
            if len(os.listdir(dir_path)) < 10:
                shutil.rmtree(dir_path)
                print(f"Deleted folder: {dir_path}")

                # Update notation counts file
                folder_name = os.path.basename(dir_path)
                if folder_name in notation_counts:
                    del notation_counts[folder_name]

    # Rewrite the updated notation counts back to the file
    with open(notation_counts_file_path, 'w') as f:
        json.dump(notation_counts, f, indent=4)

delete_folders_with_less_than_10_files(training_data_folder)
