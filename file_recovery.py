import os

def recover_files(image_file, found_files, output_dir="recovered_files"):
    """Extracts and saves recoverable files."""
    os.makedirs(output_dir, exist_ok=True)

    if not found_files:
        print("No recoverable files found.")
        return

    with open(image_file, "rb") as disk:
        for index, (file_type, position) in enumerate(found_files):
            disk.seek(position)
            recovered_data = disk.read(1024 * 1024)  # Read 1 MB

            file_path = os.path.join(output_dir, f"recovered_{index}.{file_type}")
            with open(file_path, "wb") as f:
                f.write(recovered_data)

            print(f"Recovered {file_type.upper()} file saved as {file_path}")

# Make sure to define found_files
try:
    from file_scanner import find_files, read_raw_data

    raw_data = read_raw_data("/dev/disk4", size=100*1024*1024)
    found_files = find_files(raw_data)

    recover_files("/dev/disk4", found_files)
except ImportError:
    print("Error: Could not import file_scanner.py")
except NameError:
    print("Error: No files were found to recover.")
