import os
import shutil
path = "C:/Users/prave/Downloads/BYJU'S/C102_assets-main/Badminton.gif"
destination = "downloads"
root,extension = os.path.splitext(path)
print("root of the Path",root)
print("extension of the Path", extension)
shutil.copy(path,destination)
print(os.listdir(path))