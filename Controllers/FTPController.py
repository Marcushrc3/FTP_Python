import os
import ftplib
from pathlib import Path
from ConfigController import ConfigController


class FTPController():




    def RunBySettings():
        config = ConfigController.LoadConfig()
        PathList = ConfigController.LoadPaths()       
        FTP_USER = config["User"]
        FTP_PASS = config["Pass"]

        for path in PathList:
            FTP_HOST = path["PathTo"]
            # connect to the FTP server
            ftp = ftplib.FTP(FTP_HOST, FTP_USER, FTP_PASS)
            # force UTF-8 encoding
            ftp.encoding = "utf-8"
            dirFiles = os.listdir(path["PathFrom"])
            for file in dirFiles:
                with open(file, "rb") as file:
                    # use FTP's STOR command to upload the file
                    ftp.storbinary(f"STOR {file}", file)
            ftp.quit()
