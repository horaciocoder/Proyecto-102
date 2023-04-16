import os
import shutil

startDir = "C:/Users/hrugg/OneDrive/Escritorio/C1"
destDir = "C:/Users/hrugg/OneDrive/Escritorio/C2"


files = os.listdir(startDir)

for i in files:
    name,extension = os.path.splitext(i)

    if len(extension) == 0:
        continue
    else:
        path1 = startDir + "/" + i
        path2 = destDir + "/" + "files"
        path3 = destDir + "/" + "files" + "/" + i

        if os.path.exists(path2):
            shutil.move(path1, path3)
        else:
            os.mkdir(path2)
            shutil.move(path1, path3)