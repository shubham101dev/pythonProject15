import configparser
config=configparser.RawConfigParser()
config.read("configuration/config.ini")

class Readconfig:
    @staticmethod
    def getapplicationURL():
        url=config.get('common info','geturl')
        return url

    @staticmethod
    def get_username():
        username=config.get('common info','username')
        return username

    @staticmethod
    def get_password():
        password=config.get('common info','password')
        return password


