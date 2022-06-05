import json 

class ConfigController:

    def LoadPaths():
        JsonPath = open('Config/Paths.json')
        listPaths = json.load(JsonPath)   
        return listPaths
    

    def LoadConfig():
        JsonConfig = open('Config/Config.json')
        configString = json.load(JsonConfig)
        return configString
    
