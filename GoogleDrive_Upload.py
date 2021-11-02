from pydrive.drive import GoogleDrive
from pydrive.auth import GoogleAuth
import os

gauth = GoogleAuth()
gauth.LocalWebserverAuth()

drive = GoogleDrive(gauth)
path = r"LOCAL DE UPLOAD" #lembre-se do limite de upload do GoogleDrive

for x in os.listdir(path):

    f = drive.CreateFile({'title':x})
    f.SetContentFile(os.path.join(path, x))
    f.upload()
    f = none