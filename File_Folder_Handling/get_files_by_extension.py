import os

# Set the starting folder path
# ROOT_FOLDER = "path/to/starting/folder"
# Set the extensions to filter
FILE_EXTENSIONS = [".h", ".he"]


def get_files_with_extensions(folder, extensions):
    file_l = []
    for root, dirs, files in os.walk(folder):
        for file in files:
            _, ext = os.path.splitext(file)
            if ext.lower() in extensions:
                file_l.append(os.path.join(root, file))
    return file_l


# Get the list of files with the specified extensions
file_list = get_files_with_extensions(ROOT_FOLDER, FILE_EXTENSIONS)

# Print the list of files
for file in file_list:
    print(file)
