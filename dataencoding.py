import os
import chardet

def check_encoding(file_path):
    with open(file_path, 'rb') as f:
        raw_data = f.read()
        result = chardet.detect(raw_data)
        return result['encoding']

directory = r'C:\engramar\projects\sydney-venues-for-hire'  # Your project path
exclude_path = os.path.join(directory, 'env', 'Lib', 'site-packages')

for root, dirs, files in os.walk(directory):
    for file in files:
        if file.endswith('.py'):
            file_path = os.path.join(root, file)
            # Skip files in the site-packages directory
            if exclude_path in file_path:
                continue
            encoding = check_encoding(file_path)
            if encoding is None or encoding.upper() != 'UTF-8':
                print(f"{file_path}: {encoding}")
