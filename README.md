# Apple Photos Exporter
This is for when you have a bunch of photos stored in the MacOS built in Photos app and you want to export them to an external SSD

Use this to export your own photos or do it for your parents who don't understand how to

# How to export photos from the Photos app to an external SSD
## Requirements
* Any device running MacOS with the Photos app
* Any device running Windows 10 or higher with python 3.0 or higher
* An SSD/USB drive or another way to transfer large files from a Mac to a Windows device

Note: The script can't be ran on a Mac because it uses a Windows-specific library to change the creation date of the files after copying them

## Instructions
1. Locate the Photos-Library file on your mac.

   It is usually located inside of ``` Macintosh HD/Users/Username/Pictures ```

2. Copy the entire Photos-Library file from your mac to the SSD or USB drive

   This can be done by right-clicking and copying the file, then going to the drive and pasting it there
   The copying might take a very long time or not depending on the size of your photo library and the transfer speeds of your device

3. Download the [reorganize.py](https://github.com/Blue-Sea2/Apple-Photos-Exporter/blob/main/reorganize.py) file from this repository and put it on the SSD or USB
4. Eject the drive and plug it into your windows device
5. On your windows device, open the script you downloaded in an editor
6. In file explorer, navigate into the ``` Photos-Library.photoslibrary/Masters ``` or ``` Photos-Library.photoslibrary/Originals ``` folder and copy the path

   Put that path into the ``` parent ``` variable in the top of the script

7. Create a folder that you would like the photos to end up in and copy the path to that folder as well

   Put the path you copied into the ``` output_folder ``` variable in the script

8. Run the script

   It should scan your photo library, say how many files it found and then start copying them to the folder you specified as the ``` output_folder ```
   
   If there are photos with the same name it will just put a c in front of the filename to make it unique
   
   At the end it will list any files that it failed to copy that you can manually drag into the output folder when done

10. Check that all your photos have been moved to the output folder and that their date information has been preserved
11. Delete the Photos-Library.photoslibrary folder and the reorganize.py script

## Problems?
* ### I don't have a windows device
  The script uses a library that only works on windows to set the creation date of the files
  If a friend has a windows computer you might be able to borrow it?
  I have not found a way to make it also work on MacOS
* ### How do I install python?
  Follow the instructions on [python.org](https://www.python.org/) to install Python
* ### I don't know how to edit the script
  Just open it in Notepad or VS Code whichever you prefer
* ### Folder not found
  This means that the folder you put into the variables in the top of the script do not exist or are not a folder
* ### I have another problem
  Ask ChatGPT for help
  
  If it doesn't feel free to contact me at maxkoene0@gmail.com
