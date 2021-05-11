import shutil
import os
import random
import pickle
 
raw_folder_image = "F:\\Khoa\\Hoc\\Tri_Tue_Nhan_Tao\\Pascal\\VOCdevkit\\VOC2007\\JPEGImages"
raw_folder_labels = "F:\\Khoa\\Hoc\\Tri_Tue_Nhan_Tao\\Pascal\\VOCdevkit\\VOC2007\\Annotations_txt"
 
train_folder = "F:\\Khoa\\Hoc\\Tri_Tue_Nhan_Tao\\Pascal\\images\\train"
val_folder = "F:\\Khoa\\Hoc\\Tri_Tue_Nhan_Tao\\Pascal\\images\\val"
 
train_labels_folder = "F:\\Khoa\\Hoc\\Tri_Tue_Nhan_Tao\\Pascal\\labels\\train"
val_labels_folder = "F:\\Khoa\\Hoc\\Tri_Tue_Nhan_Tao\\Pascal\\labels\\val"
 
file_list = os.listdir(raw_folder_image)
# print(file_list)
total_files = len(file_list)

total_files_validation = int(0.2 * total_files) # 20% for validation
validaiton_files = random.choices(file_list, k=total_files_validation)

train_files = []
for file in file_list:
    if file not in validaiton_files:
        train_files.append(file)
print("Number of validation: " , len(validaiton_files))
print("Number of train: ", len(train_files))
 
try:
    print("Copping validation files...")
    for file in validaiton_files:
        print(os.path.join(raw_folder_image, file))
        shutil.copy2(os.path.join(raw_folder_image, file), val_folder)
        shutil.copy2(os.path.join(raw_folder_labels, file[:-3] + 'txt'), val_labels_folder)
        # print("File validation {} copied successfully.".format(file))
    print("Copied successfully validation files...")
    print("Copping train files...")
    for file in train_files:
        print(os.path.join(raw_folder_image, file))
        shutil.copy2(os.path.join(raw_folder_image, file), train_folder)
        shutil.copy2(os.path.join(raw_folder_labels, file[:-3] + 'txt'), train_labels_folder)
        # print("File train {} copied successfully.".format(file))
    print("Copied successfully train files...")
  
# If source and destination are same
except shutil.SameFileError:
    print("Source and destination represents the same file.")
  
# If destination is a directory.
except IsADirectoryError:
    print("Destination is a directory.")
  
# If there is any permission issue
except PermissionError:
    print("Permission denied.")
  
# For other errors
# except:
#     print("Error occurred while copying file.")