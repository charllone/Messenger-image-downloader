import os
import shutil

# 🔧 Path to your folder
SOURCE_FOLDER = r"C:\Users\arsol\Downloads\Messenger"

# Create target folders for GIFs and videos
GIF_FOLDER = os.path.join(SOURCE_FOLDER, "GIFs")
VIDEO_FOLDER = os.path.join(SOURCE_FOLDER, "Videos")

os.makedirs(GIF_FOLDER, exist_ok=True)
os.makedirs(VIDEO_FOLDER, exist_ok=True)

# Supported video extensions
VIDEO_EXTENSIONS = (".mp4", ".mov", ".avi", ".mkv", ".wmv", ".flv")

# Loop through files in the source folder
for filename in os.listdir(SOURCE_FOLDER):
    file_path = os.path.join(SOURCE_FOLDER, filename)

    # Skip directories
    if os.path.isdir(file_path):
        continue

    # Move GIFs
    if filename.lower().endswith(".gif"):
        shutil.move(file_path, os.path.join(GIF_FOLDER, filename))
        print(f"Moved GIF: {filename}")

    # Move Videos
    elif filename.lower().endswith(VIDEO_EXTENSIONS):
        shutil.move(file_path, os.path.join(VIDEO_FOLDER, filename))
        print(f"Moved Video: {filename}")

print("Sorting complete!")
