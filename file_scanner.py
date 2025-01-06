import re

FILE_SIGNATURES = {
    "jpg": b"\xFF\xD8\xFF\xE0",
    "png": b"\x89\x50\x4E\x47",
    "pdf": b"%PDF-",
    "mp4": b"\x00\x00\x00\x18\x66\x74\x79\x70\x6D\x70\x34\x32"
}

def find_files(raw_data):
    """Searches for known file signatures in raw disk data."""
    recoverable_files = []

    for file_type, signature in FILE_SIGNATURES.items():
        matches = re.finditer(signature, raw_data)
        for match in matches:
            recoverable_files.append((file_type, match.start()))

    return recoverable_files

def read_raw_data(image_file, size=50*1024*1024):
    """Reads raw binary data from disk image."""
    with open(image_file, "rb") as disk:
        return disk.read(size)

raw_data = read_raw_data("/dev/disk4")
found_files = find_files(raw_data)

print("\nRecoverable Files:")
for file_type, position in found_files:
    print(f"- {file_type.upper()} file found at byte {position}")
