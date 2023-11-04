import shutil
import os
import random
import pickle
from PIL import Image
import csv

raw_folder = "daytime-dataset\\daytime"


train_folder = "mydata2\\images\\train"
val_folder = "mydata2\\images\\valid"

train_labels_folder = "\\mydata2\\labels\\train"
val_labels_folder = "\\mydata2\\labels\\valid"


# print(f"Danh sách các file ảnh trong thư mục '{directory_path}':")
image_files = [file for file in os.listdir(raw_folder) if file.lower().endswith(".jpg")]
    

# Tạo ra index cho train, val
total_files_validation = int(0.2 * len(image_files)) # 20% cho validation
validaiton_files = random.choices(image_files, k=total_files_validation)

print("Số bản ghi validation = " , len(validaiton_files))

# Copy images và labels to validation folder
for file in validaiton_files:
    print("Validation file ", file)
    # Copy images
    shutil.copy(os.path.join(raw_folder, file), os.path.join(val_folder, file))

    # Copy labels
    shutil.copy(os.path.join(raw_folder, file[:-3] + 'txt'), os.path.join(val_labels_folder, file[:-3] + 'txt'))


# Copy images và labels to train folder
for file in image_files:
    if not (file in validaiton_files):
        print("Train file ", file)
        # Copy images
        shutil.copy(os.path.join(raw_folder, file), os.path.join(train_folder, file))

        # Copy labels
        shutil.copy(os.path.join(raw_folder, file[:-3] + 'txt'), os.path.join(train_labels_folder, file[:-3] + 'txt'))
        


