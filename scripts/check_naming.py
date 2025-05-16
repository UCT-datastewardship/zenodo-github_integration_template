import os
import re

data_dir = 'data'
project_prefix = 'EXAMPLE'  # Set your project prefix zde

# Definice povolených hodnot pro poslední část názvu
allowed_suffixes = [
    'raw', 'final', 'clean'
] + [f'v{i}' for i in range(0, 101)]

# Sestavení regulárního výrazu pro povolené přípony (case-insensitive)
suffix_pattern = '|'.join(allowed_suffixes)
pattern = re.compile(rf'^{project_prefix}_(\d{{4}})(0[1-9]|1[0-2])(0[1-9]|[12][0-9]|3[01])_.*_({suffix_pattern})\.[^.]+$', re.IGNORECASE)

print("Checking file naming convention EXAMPLE_YYYYMMDD_filename_suffix.ext in the 'data/' directory...")
invalid_files = []
if os.path.exists(data_dir):
    for filename in os.listdir(data_dir):
        if not pattern.match(filename):
            invalid_files.append(filename)
if invalid_files:
    print("Error: The following files do not follow the naming convention (EXAMPLE_YYYYMMDD_filename_suffix.ext):")
    for f in invalid_files:
        print(f"- {f}")
    exit(1)
else:
    print("All files in the 'data/' directory follow the naming convention.")
