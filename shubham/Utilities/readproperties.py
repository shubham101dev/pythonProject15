import configparser

config=configparser.RawConfigParser()
config.read(".\\configurations\\config.ini")

class Readconfig:
    @staticmethod
    def application_url():
        url=config.get('common info','geturl' )
        return url

    @staticmethod
    def get_username():
        username=config.get('common info','username')
        return username

    @staticmethod
    def get_surname():
        surname=config.get('common info','surname')
        return surname

    @staticmethod
    def get_email():
        email=config.get('common info','email')
        return email

    @staticmethod
    def get_phone():
        phone=config.get('common info','number')
        return phone




