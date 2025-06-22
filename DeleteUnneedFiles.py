import os
print("Name: Sahil\nUSN: 1AY24AI093")
def find_large_files(folder, size_limit_mb):
    size_limit = size_limit_mb * 1024 * 1024  # Convert MB to bytes
    print(f"Searching for files larger than {size_limit_mb} MB in '{folder}'...\n")
    for foldername, subfolders, filenames in os.walk(folder):
        for filename in filenames:
            file_path = os.path.join(foldername, filename)
            try:
                file_size = os.path.getsize(file_path)
                if file_size > size_limit:
                    size_mb = round(file_size / (1024 * 1024), 2)
                    print(f"{size_mb} MB - {file_path}")
                    delete = input("Do you want to delete this file? (yes/no): ").strip().lower()
                    if delete == 'yes':
                        os.remove(file_path)
                        print("Deleted.\n")
                    else:
                        print("Skipped.\n")
            except Exception as e:
                print(f"Could not access {file_path}: {e}")
folder_path = input("Enter the folder path to scan: ")
size_limit = float(input("Enter the minimum file size to find (in MB): "))
find_large_files(folder_path, size_limit)
