# file_organiser
A python based mini project to organised files and folders .
# 📂 Python File Organizer

A simple Python automation project that organizes files into different folders based on their file extensions. It automatically creates categorized folders and moves files into their respective directories, helping keep your workspace clean and organized.

## 🚀 Features

- **Automatic Folder Creation:** Creates folders if they don't already exist.
- **File Classification:** Identifies files based on their extensions.
- **Automatic File Movement:** Moves files into their respective folders.
- **Multiple File Categories:** Supports images, documents, audio, videos, archives, and scripts.
- **Duplicate Folder Handling:** Reuses existing folders instead of creating duplicates.

## 📁 Supported File Types

| Category | Extensions |
|---|---|
| Images | `.jpg`, `.jpeg`, `.png`, `.gif`, `.bmp`, `.tiff` |
| Documents | `.pdf`, `.docx`, `.txt`, `.xlsx`, `.pptx` |
| Audio | `.mp3`, `.wav`, `.aac`, `.flac` |
| Videos | `.mp4`, `.avi`, `.mkv`, `.mov` |
| Archives | `.zip`, `.rar`, `.tar`, `.gz` |
| Scripts | `.py`, `.js`, `.html`, `.css` |

## 🛠️ Technologies Used

- **Python 3**
- `os` module
- `shutil` module

## ⚙️ How It Works

1. Gets the current working directory.
2. Defines categories and their supported file extensions.
3. Creates folders for each category.
4. Scans files in the current directory.
5. Checks each file's extension.
6. Moves files into their corresponding folders.

## 💻 Installation & Usage

**1. Clone the repository**

```bash
git clone https://github.com/koushikk2005/file_organiser.git
```

**2. Navigate to the project directory**

```bash
cd python-file-organizer
```

**3. Run the Python script**

```bash
python main.py
```

No external libraries are required because the project uses Python's built-in modules.

## 📂 Example Folder Structure

**Before Execution:**

```text
FileOrganizer/
│
├── main.py
├── photo.jpg
├── document.pdf
├── song.mp3
├── video.mp4
├── project.zip
└── script.py
```

**After Execution:**

```text
FileOrganizer/
│
├── main.py
│
├── Images/
│   └── photo.jpg
│
├── Documents/
│   └── document.pdf
│
├── Audio/
│   └── song.mp3
│
├── Videos/
│   └── video.mp4
│
├── Archives/
│   └── project.zip
│
└── Scripts/
    └── script.py
```

## 🎯 Learning Outcomes

- Understanding Python file handling.
- Working with directories and file paths.
- Using the `os` and `shutil` modules.
- Automating repetitive tasks.
- Implementing conditional logic and loops.

## 🔮 Future Improvements

- Add support for more file formats.
- Create a graphical user interface (GUI).
- Add duplicate filename handling.
- Allow users to select a custom directory.
- Generate a report of organized files.
- Add logging and error handling.

## 👨‍💻 Author

**Koushik Khan**

Computer Science Engineering Student | Cyber Security

---

⭐ If you find this project useful, consider giving it a star!
