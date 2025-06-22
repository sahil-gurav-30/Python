import os
import shutil
print("Name: Sahil\nUSN: 1AY24AI093")
def selective_copy():
    source_folder = input("Enter the path to the source folder: ").strip()
    file_extension = input("Enter the file extension to look for (e.g., .jpg): ").strip().lower()
    destination_folder = input("Enter the path to the destination folder: ").strip()
    os.makedirs(destination_folder, exist_ok=True)
    for foldername, subfolders, filenames in os.walk(source_folder):
        for filename in filenames:
            if filename.lower().endswith(file_extension):
                source_file_path = os.path.join(foldername, filename)
                print(f"Copying {source_file_path}...")
                shutil.copy2(source_file_path, destination_folder)
    print("\nAll matching files have been copied.")
selective_copy()
