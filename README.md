# 🛠️ FileFixer

**FileFixer** is a Python-based utility that attempts to repair corrupted files by restoring or replacing their **magic bytes** (file headers). You can let the program make an **educated guess** based on file content or **manually specify** the file type to fix.

---

## 🚀 Features
- ✅ Auto Mode: Scans and detects the closest matching file type by analyzing magic bytes.
- ✅ Manual Mode: Manually select a file type to repair.
- ✅ Backs up the original file before making changes.
- ✅ Supports a wide range of file formats: images, documents, archives, executables, videos, audio, and disk images.
- ✅ User-friendly CLI interface.

---

## 📂 Supported File Types
- **Images**: PNG, JPEG, GIF (87a/89a), BMP
- **Documents**: PDF, MS Office (Old), DOCX/PPTX/XLSX
- **Archives**: ZIP, GZIP, 7-Zip, RAR
- **Executables**: ELF, Windows EXE/DLL
- **Video & Audio**: AVI/WAV (RIFF), MPEG, MKV, MP4, OGG
- **Disk Images**: ISO, FAT16, FAT32

Use the `List Supported Types` option in the program for the full list.

---

## 📥 Installation

### Prerequisites
- Python 3.x installed on your system.

### Clone the Repository
```bash
git clone https://github.com/ezpz44/FileFixer.git
cd FileFixer


⚙️ How to Use
Run FileFixer
~ python filefixer.py

# Menu Options
-Auto Mode:
Detects the closest file type and repairs the file header.

-Manual Mode:
You specify the file type, and it applies the correct header.

-List Supported Types:
Displays all recognized file formats.

-Exit:
Exits the program.

🛡️ Safety & Backup
Before applying any changes, FileFixer creates a backup of the original file with a .bak extension, ensuring your data is safe.

🏗️ How It Works
FileFixer compares a file's magic bytes against a list of known signatures. In Auto Mode, it uses similarity scoring (difflib) to detect the closest match. In Manual Mode, you select the type, and it applies the appropriate magic bytes.

🔧 Example Usage
Start the program:
~ python filefixer.py

Choose Auto Mode to let FileFixer detect the file type.

Provide the full file path when prompted.

The program:
Backs up the original file (e.g., file.jpg.bak)

Fixes the magic bytes

Notifies you when the process is complete.

⚠️ Disclaimer
FileFixer only fixes file headers (magic bytes). It does not repair damaged file content or structure.
Use at your own risk, and always test repaired files.

📜 License
MIT License.

✨ Contributing
Pull requests are welcome! If you'd like to contribute, please fork the repository and submit a PR.

👨‍💻 Author
Created by ezpz44