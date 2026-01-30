import os
import shutil


def copy_static(source, destination):
    # Delete destination folder contents if it exists
    if os.path.exists(destination):
        shutil.rmtree(destination)

    # Recreate destination folder
    os.mkdir(destination)

    # Copy everything from source -> destination
    for item in os.listdir(source):
        source_path = os.path.join(source, item)
        dest_path = os.path.join(destination, item)

        if os.path.isfile(source_path):
            print(f"Copying file: {source_path} -> {dest_path}")
            shutil.copy(source_path, dest_path)
        else:
            print(f"Copying directory: {source_path} -> {dest_path}")
            copy_static(source_path, dest_path)
