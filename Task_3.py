import shutil
import os


path = input("Enter Path: ")   # Get the path from the user


files = os.listdir(path)   # List all files in the directory


# Iterate through each file
for file in files:

    
    filename, extension = os.path.splitext(file)  # Split the filename and extension
    
    extension = extension[1:]    # Remove the leading dot from the extension

    # Check if the extension directory exists
    if os.path.exists(os.path.join(path, extension)):

        # Move the file to the extension directory
        shutil.move(os.path.join(path, file), os.path.join(path, extension, file))


    else:

        # Create the directory for the extension
        os.makedirs(os.path.join(path, extension))
        
        # Move the file to the newly created directory
        shutil.move(os.path.join(path, file), os.path.join(path, extension, file))
