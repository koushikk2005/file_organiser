import os
import shutil

folder_path=os.getcwd()
file_types = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff'],
    'Documents': ['.pdf', '.docx', '.txt', '.xlsx', '.pptx'],
    'Audio': ['.mp3', '.wav', '.aac', '.flac'],
    'Videos': ['.mp4', '.avi', '.mkv', '.mov'],
    'Archives': ['.zip', '.rar', '.tar', '.gz'],
    'Scripts': ['.py', '.js', '.html', '.css'],
}
for folder in file_types.keys():
    if not os.path.exists( folder):
        os.makedirs(folder)

for filename in os.listdir(folder_path):
    if os.path.isdir(filename):
        continue

extension=os.path.splitext(filename)[1].lower
for folder, extensions in file_types.items():
    if extension in extensions:
        shutil.move(filename, os.path.join(folder, filename))
        break