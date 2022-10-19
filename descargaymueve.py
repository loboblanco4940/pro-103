# time es un modulo proporciona las funciones para trabajar con el tiempo.
import time
#proporciona funciones para interactuar con el sistema operativo.
import os
import shutil
import random
import sys
from watchdog.observers import Observer 
from watchdog.events import FileSystemEventHandler

#https://pythonhosted.org/watchdog/
from_dir="C:\Users\edgar\Documents"
to_dir="C:\Riot Games"

dir_tree = {
    "Image_Files": ['.jpg', '.jpeg', '.png', '.gif', '.jfif'],
    "Video_Files": ['.mpg', '.mp2', '.mpeg', '.mpe', '.mpv', '.mp4', '.m4p', '.m4v', '.avi', '.mov'],
    "Document_Files": ['.ppt', '.xls', '.xlsx' '.csv', '.pdf', '.txt'],
    "Setup_Files": ['.exe', '.bin', '.cmd', '.msi', '.dmg']
}

class FileMovmentHandler(FileSystemEventHandler):
    def on_created(self,event):
        name,extension=os.path.splitext(event.src_path)
        time.sleep(1)

        if extension in value:
            file_name=os.path.basename(event.src_path)
            print  ("Descargando"+file_name)
            path1 = from_dir + '/' + file_name
            path2 = to_dir + '/' + key
            path3 = to_dir + '/' + key + '/' + file_name

            if os.path.exists(path2):
                print("La carpeta"+ file_name +" ya existe")
                shutil.move(path1,path3)
                time.sleep(1)
            else : 
                print("Se esta creando la carpeta")
                os.makedirs(path2)
                shutil.move(path1,path3)
                time.sleep(1)

event_handler=FileMovmentHandler()
observer=Observer()

observer.schedule(event_handler, from_dir, recursive=True)
observer.start()
try:
    while True:
        time.sleep(2)
        print("ejecutando...")
except KeyboardInterrupt:
    print("¡detenido!")
    observer.stop()


