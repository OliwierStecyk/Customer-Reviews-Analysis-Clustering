import kagglehub
import os
import zipfile
import shutil

target_dir = "../data/raw"
os.makedirs(target_dir, exist_ok=True)

path = kagglehub.dataset_download("snap/amazon-fine-food-reviews")
print("Pobrany plik/folder:", path)

if zipfile.is_zipfile(path):
    with zipfile.ZipFile(path, 'r') as zip_ref:
        zip_ref.extractall(target_dir)
    os.remove(path)
    print("Dataset rozpakowany do folderu:", target_dir)
else:
    shutil.move(path, target_dir)
    print("Dataset przeniesiony do folderu:", target_dir)
