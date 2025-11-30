import os

folder_name = "task8_folder"
file_path = os.path.join(folder_name, "inside.txt")

# Create folder if not exists
if not os.path.exists(folder_name):
    os.mkdir(folder_name)
    print("Folder created:", folder_name)
else:
    print("Folder already exists:", folder_name)

# Create file inside folder
with open(file_path, "w") as f:
    f.write("This file is inside a folder.\n")

print("File created inside folder:", file_path)
