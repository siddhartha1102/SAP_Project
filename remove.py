from pathlib import Path
import os, shutil
def remove(path):
    path = Path(path)
    for file in path.glob("*_final*"):
        if file.is_file() and file.name.endswith("_final") or file.stem.endswith("_final"):
            file.unlink()
            print(f"Removed: {file}")

    if os.path.exists("extracted_images"):
        shutil.rmtree("extracted_images")
        print("Folder removed")

