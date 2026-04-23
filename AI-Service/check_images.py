from PIL import Image, ImageFile
import os

ImageFile.LOAD_TRUNCATED_IMAGES = False
dataset_dir = "Dataset"
removed = 0
skipped = 0

for folder in os.listdir(dataset_dir):
    folder_path = os.path.join(dataset_dir, folder)
    if not os.path.isdir(folder_path):
        continue
    for filename in os.listdir(folder_path):
        filepath = os.path.join(folder_path, filename)
        try:
            img = Image.open(filepath)
            img.convert("RGB")
            img.close()
        except Exception as e:
            try:
                os.remove(filepath)
                print(f"Removed: {filepath}")
                removed += 1
            except PermissionError:
                print(f"Skipped (in use): {filepath}")
                skipped += 1

print(f"Done — removed {removed}, skipped {skipped}")