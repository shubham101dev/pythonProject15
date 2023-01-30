import configparser
config=configparser.RawConfigParser()
config.read(".\\configuration\\config.ini")

class Readconfig:
    @staticmethod
    def getapplicationURL():
        url=config.get('common info','geturl')
        return url

    @staticmethod
    def get_username_xpath():
        username_xpath=config.get('login xpath','username_xpath')
        return username_xpath

    @staticmethod
    def get_password_xpath():
        password_xpath=config.get('login xpath','password_xpath')
        return password_xpath

    @staticmethod
    def get_box_xpath():
        box=config.get('login xpath','box_xpath')
        return box

    @staticmethod
    def get_signin_xpath():
        signin_xpath=config.get('login xpath','signin_xpath')
        return signin_xpath

    @staticmethod
    def get_username():
        username=config.get('value','username')
        return username

    @staticmethod
    def get_password():
        password=config.get('value','password')
        return password


