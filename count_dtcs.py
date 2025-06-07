import json
import os

def count_dtcs_in_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return len(data)
    except UnicodeDecodeError:
        try:
            # Try with a different encoding if UTF-8 fails
            with open(file_path, 'r', encoding='latin-1') as f:
                data = json.load(f)
                return len(data)
        except Exception as e:
            print(f"Error reading {os.path.basename(file_path)}: {str(e)}")
            return 0
    except Exception as e:
        print(f"Error reading {os.path.basename(file_path)}: {str(e)}")
        return 0

# Get all JSON files in the current directory
json_files = [f for f in os.listdir('.') if f.endswith('.json')]

# Sort files alphabetically
json_files.sort()

# Print header
print("\nDTC Count by Brand:")
print("-" * 30)

# Process each file
for file_name in json_files:
    count = count_dtcs_in_file(file_name)
    brand = file_name.replace('.json', '')
    print(f"{brand:15} : {count:4} DTCs")
