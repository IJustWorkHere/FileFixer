import difflib
import shutil
import os

# Dictionary of known magic bytes (File Signatures)
known_magic_bytes = {
    # Image Formats
    b'\x89\x50\x4E\x47\x0D\x0A\x1A\x0A': 'PNG',
    b'\xFF\xD8\xFF': 'JPEG',
    b'\x47\x49\x46\x38\x37\x61': 'GIF (87a)',
    b'\x47\x49\x46\x38\x39\x61': 'GIF (89a)',
    b'\x42\x4D': 'BMP',

    # Document Formats
    b'\x25\x50\x44\x46': 'PDF',
    b'\xD0\xCF\x11\xE0\xA1\xB1\x1A\xE1': 'MS Office (Old, pre-2007)',
    b'\x50\x4B\x03\x04': 'DOCX, PPTX, XLSX (Office Open XML)',

    # Archive Formats
    b'\x50\x4B\x03\x04': 'ZIP',
    b'\x1F\x8B\x08': 'GZIP',
    b'\x37\x7A\xBC\xAF\x27\x1C': '7-Zip Archive',
    b'\x52\x61\x72\x21\x1A\x07\x00': 'RAR Archive',

    # Executable Formats
    b'\x7F\x45\x4C\x46': 'ELF Executable',  # Linux Executable
    b'\x4D\x5A': 'Windows Executable (EXE/DLL)',
    
    # Video & Audio Formats
    b'\x52\x49\x46\x46': 'RIFF (AVI/WAV)',
    b'\x00\x00\x01\xBA': 'MPEG Video',
    b'\x00\x00\x01\xB3': 'MPEG Video',
    b'\x1A\x45\xDF\xA3': 'MKV Video',
    b'\x66\x74\x79\x70': 'MP4 Video',
    b'\x4F\x67\x67\x53': 'OGG Audio',

    # Disk Images
    b'\x43\x44\x30\x30\x31': 'ISO Disk Image',
    b'\xEB\x3C\x90': 'FAT16 Boot Sector',
    b'\x33\xC0\x8E\xD0\xBC\x00\x7C': 'FAT32 Boot Sector',
}

def title():
    print("\n===== Welcome to FileFixer =====")
    print("This program attempts to fix corrupted files by restoring their magic bytes.")
    print("You can let the program make an educated guess (Auto Mode) or manually specify the file type.")
    
    while True:
        user_selection = input("1 for Auto Mode \n 2 for Manual Mode \n 3 to List Supported Types \n 0 to Exit \n Enter the number of your choice: ").strip()
        if user_selection == "1":
            autoFix()
            break
        elif user_selection == "2":
            manualFix()
            break
        elif user_selection == "3":
            list_file_types()
        elif user_selection == "0":
            print("Exiting program.")
            return
        else:
            print("Invalid input, try again.")

def list_file_types():
    """ Displays all supported file types. """
    print("\nSupported File Types:")
    for magic, file_type in known_magic_bytes.items():
        print(f" - {file_type}")
    print()

def manualFix():
    """ Allows user to manually choose a file type and apply the correct magic bytes. """
    target_path = input("\nEnter the full path of the file to fix: ").strip()
    
    if not os.path.exists(target_path):
        print("❌ Error: File not found.")
        return title()
    
    list_file_types()
    user_type_request = input("Enter the desired file type (case sensitive): ").strip().lower()

    # Find matching magic bytes
    new_magic_bytes = None
    for magic, file_type in known_magic_bytes.items():
        if file_type.lower() == user_type_request:
            new_magic_bytes = magic
            break

    if not new_magic_bytes:
        print("❌ Unknown file type. Try again.")
        return title()

    apply_fix(target_path, new_magic_bytes, user_type_request)

def autoFix():
    """ Automatically detects the closest matching file type and applies the fix. """
    target_path = input("\nEnter the full path of the file to fix: ").strip()

    if not os.path.exists(target_path):
        print("❌ Error: File not found.")
        return title()

    # Read first 16 bytes
    with open(target_path, "rb") as f:
        file_bytes = f.read(16)

    # Find exact match first
    for magic, file_type in known_magic_bytes.items():
        if file_bytes.startswith(magic):
            print(f"✔ Exact match found: {file_type}")
            apply_fix(target_path, magic, file_type)
            return title()

    # If no exact match, find the closest match
    best_match = None
    best_score = 0

    for magic, file_type in known_magic_bytes.items():
        similarity = difflib.SequenceMatcher(None, file_bytes[:len(magic)], magic).ratio()
        if similarity > best_score:
            best_match = (magic, file_type)
            best_score = similarity

    if best_match:
        new_magic_bytes, matched_type = best_match
        print(f"🔍 Closest match found: {matched_type}")
        apply_fix(target_path, new_magic_bytes, matched_type)
    else:
        print("❌ No close match found.")

def apply_fix(target_path, new_magic_bytes, file_type):
    """ Applies new magic bytes to a file and saves a backup """
    backup_path = target_path + ".bak"
    shutil.copy2(target_path, backup_path)  # Preserve original

    with open(target_path, "r+b") as f:
        f.seek(0)
        f.write(new_magic_bytes)

    print(f"✔ Magic bytes updated to match {file_type}.")
    print(f"✔ Original file backed up as {backup_path}.")
    return title()

# Run the program
title()
