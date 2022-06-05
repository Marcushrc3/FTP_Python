from Controllers.ConfigController import ConfigController
from Controllers.FTPController import FTPController

Paths = ConfigController.LoadPaths()
Config = ConfigController.LoadConfig()

for path in Paths:
    FTPController.RunBySettings()