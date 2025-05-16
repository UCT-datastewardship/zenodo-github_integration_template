import os
import re

data_dir = 'data'
project_prefix = 'EXAMPLE'  # Set your project prefix zde
pattern = re.compile(rf'^{project_prefix}_\d{{8}}_.+_v\d+\..+$')

print("Checking file naming convention EXAMPLE_YYYYMMDD_filename_version.ext in the 'data/' directory...")
invalid_files = []
if os.path.exists(data_dir):
    for filename in os.listdir(data_dir):
        if not pattern.match(filename):
            invalid_files.append(filename)
if invalid_files:
    print("Error: The following files do not follow the naming convention (EXAMPLE_YYYYMMDD_filename_version.ext):")
    for f in invalid_files:
        print(f"- {f}")
    exit(1)
else:
    print("All files in the 'data/' directory follow the naming convention.")
