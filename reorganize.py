import os
import shutil
import pywintypes
import win32file
import time
from PIL import Image
from datetime import datetime
import sys

parent = "D:/Fotos-Mediathek.photoslibrary/Masters" #path of Masters or Originals folder here 
output_folder = "D:/photos/" #path of the output folder here
paths = []
titles = []
files = {}

#make sure the paths are correct
if output_folder[-1]!="/":
    output_folder=output_folder+"/"
if not os.path.isdir(parent):
    print("Folder not found:",parent)
    sys.exit()
if not os.path.isdir(output_folder):
    print("Folder not found:", output_folder)
    sys.exit()

#scan photo library
def searchdir(dir):
    for file in os.listdir(dir):
        if file[:2]!="._":
            path = str(dir+"/"+file)
            if os.path.isdir(path):
                searchdir(path)
            else:
                if not path in paths:
                    paths.append(path)
                    while file in titles:
                        file = "c"+file #put a C in front of the filename until it's unique
                    titles.append(file)
                    files.update({path:file})

searchdir(parent)
print(len(files),"files scanned")


#copy files
i=0
failed=[]

def set_creation_date(file_path, creation_time):
    win_time=pywintypes.Time(creation_time)

    handle = win32file.CreateFile(
        file_path,
        win32file.GENERIC_WRITE,
        win32file.FILE_SHARE_READ,
        None,
        win32file.OPEN_EXISTING,
        win32file.FILE_ATTRIBUTE_NORMAL,
        None
    )
    win32file.SetFileTime(handle, win_time, None, None)
    handle.close()

for path,title in files.items():
    mdate = os.path.getmtime(path)
    try:
        with Image.open(path) as img:
            exif_data = img._getexif()
            if exif_data: #get creation date from photo metadata if available
                cdate = exif_data[36867]
                cdate = datetime.strptime(cdate, "%Y:%m:%d %H:%M:%S")
                date = time.mktime(cdate.timetuple())
            else:
                date = mdate
    except:
        date = mdate
        
    target = str(output_folder+title)
    try:
        shutil.copyfile(path, target)
        os.utime((target), (mdate, mdate))
        set_creation_date(target, date)
        i+=1
        print(i,"/",len(files))
    except:
        print("Could not copy",path,"as",title)
        failed.append(path)

print("failed to move:",str(failed))