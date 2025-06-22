import os
import re
print("Name: Sahil\nUSN: 1AY24AI093")
def get_numbered_files(folder, prefix, extension):
    pattern = re.compile(rf"^{re.escape(prefix)}(\d+)\.{re.escape(extension)}$")
    numbered_files = []
    for file in os.listdir(folder):
        match = pattern.match(file)
        if match:
            number = int(match.group(1))
            numbered_files.append((number, file))
    return sorted(numbered_files)
def close_gaps(folder, prefix, extension):
    print("\n--- Closing Gaps ---")
    numbered_files = get_numbered_files(folder, prefix, extension)
    expected = 1
    for actual_number, filename in numbered_files:
        if actual_number != expected:
            new_name = f"{prefix}{expected:03}.{extension}"
            print(f"Renaming {filename} → {new_name}")
            os.rename(os.path.join(folder, filename), os.path.join(folder, new_name))
        expected += 1
    print("Gap closing complete.\n")
def insert_gap(folder, prefix, extension, insert_at):
    print(f"\n--- Inserting Gap at {insert_at:03} ---")
    numbered_files = get_numbered_files(folder, prefix, extension)
    # Rename in reverse to avoid overwriting
    for number, filename in reversed(numbered_files):
        if number >= insert_at:
            new_name = f"{prefix}{number + 1:03}.{extension}"
            print(f"Renaming {filename} → {new_name}")
            os.rename(os.path.join(folder, filename), os.path.join(folder, new_name))
    print("Gap insertion complete.\n")
if __name__ == "__main__":
    folder = "."  
    prefix = input("Enter file prefix (e.g., spam): ").strip()
    extension = input("Enter file extension (e.g., txt): ").strip()
    mode = input("Choose mode - (C)lose gaps or (I)nsert gap? ").strip().lower()
    if mode == 'c':
        close_gaps(folder, prefix, extension)
    elif mode == 'i':
        insert_at = int(input("Enter position number to insert gap at (e.g., 2): "))
        insert_gap(folder, prefix, extension, insert_at)
    else:
        print("Invalid mode. Choose 'C' or 'I'.")
