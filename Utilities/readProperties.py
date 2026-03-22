import configparser
import os

config = configparser.RawConfigParser()
config.read(os.path.abspath(os.curdir)+"//Configurations//"+"config.ini")

class ReadConfig:

    @staticmethod
    def getApplicationUrl():
        url = config.get('CommonInfo', 'baseUrl')
        return url

    @staticmethod
    def getEmail():
        user = config.get('CommonInfo', 'username')
        return user

    @staticmethod
    def getPassword():
        password = config.get("CommonInfo", 'password')
        return password