import shutil
import os
import random
import pickle
from PIL import Image
import csv

raw_folder = "C:\\Users\\PC\\Desktop\\project_thay_linh\\local\\car_bike_detection\\car_bike_detection\\xml_to_textYolo\\vehicle_vietnam\\daytime-dataset\\daytime"

# with open('C:/Users/PC/Desktop/project_thay_linh/local/car_bike_detection/car_bike_detection/xml_to_textYolo/Image-Files-To-CSV-With-Labels/output.csv','rb') as f:
#     file_list = pickle.load(f)

# def count_images_in_directory(directory):
#     image_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff']
#     image_count = 0

#     for filename in os.listdir(directory):
#         if any(filename.lower().endswith(ext) for ext in image_extensions):
#             image_count += 1

#     return image_count

# def list_image_files(directory):
#     image_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff']
#     image_files = []

#     for filename in os.listdir(directory):
#         if any(filename.lower().endswith(ext) for ext in image_extensions):
#             image_files.append(directory+'\\'+filename)

#     return image_files

# Thay đổi đường dẫn thư mục dưới đây bằng đường dẫn thư mục bạn muốn kiểm tra
# directory_path = raw_folder
# image_count = count_images_in_directory(directory_path)
# image_files = list_image_files(directory_path)

# print(image_files)

# print(f"Số lượng file ảnh trong thư mục '{directory_path}' là {image_count}")

# total_files = len(file_list) # Tổng số file có nhãn trong thư mục train
# total_files = image_count # Tổng số file có nhãn trong thư mục train

# print("Tổng số file  = ", total_files)

# Anh em tạo sẵn thư mục này nếu chưa có nhé :D Mình khỏi viết hàm check ở đây hehe
train_folder = "C:\\Users\\PC\\Desktop\\project_thay_linh\\local\\car_bike_detection\\car_bike_detection\\xml_to_textYolo\\vehicle_vietnam\\mydata2\\images\\train"
val_folder = "C:\\Users\\PC\\Desktop\\project_thay_linh\\local\\car_bike_detection\\car_bike_detection\\xml_to_textYolo\\vehicle_vietnam\\mydata2\\images\\valid"

train_labels_folder = "C:\\Users\\PC\\Desktop\\project_thay_linh\\local\\car_bike_detection\\car_bike_detection\\xml_to_textYolo\\vehicle_vietnam\\mydata2\\labels\\train"
val_labels_folder = "C:\\Users\\PC\\Desktop\\project_thay_linh\\local\\car_bike_detection\\car_bike_detection\\xml_to_textYolo\\vehicle_vietnam\\mydata2\\labels\\valid"


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
        


# model.eval()

# with open('Submission.csv', 'a+', newline='') as f:  # 'a+' means append to a file
#  thewriter = csv.writer(f)
 
#  with torch.no_grad():
#    for data in test_loader:
#      output=model(data)
#      label = output.argmax().item()  # this your label
#      print(label)
#      thewriter.writerow([label])
