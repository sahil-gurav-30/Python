import re
print("Name: Sahil\nUSN: 1AY24AI093")
def mad_libs(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        return
    except Exception as e:
        print(f"An error occurred: {e}")
        return
    placeholders = re.findall(r'\b(ADJECTIVE|NOUN|ADVERB|VERB)\b', content)
    if not placeholders:
        print("No placeholders found in the file.")
        return
    counts = {'NOUN': 0, 'ADJECTIVE': 0, 'ADVERB': 0, 'VERB': 0}
    replacements = []
    for placeholder in placeholders:
        counts[placeholder] += 1
        current_count = counts[placeholder]
        if placeholder == "NOUN":
            prompt = f"Enter noun #{current_count}: "
        elif placeholder == "ADJECTIVE":
            prompt = f"Enter an adjective #{current_count}: "
        elif placeholder == "ADVERB":
            prompt = f"Enter an adverb #{current_count}: "
        elif placeholder == "VERB":
            prompt = f"Enter a verb #{current_count}: "
        user_input = input(prompt)
        replacements.append(user_input)
    new_content = content
    for i, placeholder in enumerate(placeholders):
        new_content = new_content.replace(placeholder, replacements[i], 1)
    print("\nHere's your Mad Libs story:\n")
    print(new_content)
    output_path = file_path.replace('.txt', '_madlibs.txt')
    try:
        with open(output_path, 'w') as file:
            file.write(new_content)
        print(f"\nStory saved to '{output_path}'")
    except Exception as e:
        print(f"Could not save the file: {e}")

if __name__ == "__main__":
    input_file = input("Enter the path to your Mad Libs template file: ")
    mad_libs(input_file)
