import configparser
config=configparser.RawConfigParser()
config.read(".\\configuration\\config.ini")


class Readconfig():
    @staticmethod
    def getapplicationURL():
        url=config.get('common info','geturl')
        return url

    @staticmethod
    def getusername():
        username=config.get('common info','username')
        return username

    @staticmethod
    def getpassword():
        password=config.get('common info','password')
        return password

    @staticmethod
    def get_box_value():
        box1=config.get('next page','box1')
        return box1

    @staticmethod
    def get_next_pageURL():
        url=config.get('next page','mycoll')
        return url




