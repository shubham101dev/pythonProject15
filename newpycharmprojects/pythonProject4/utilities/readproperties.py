import configparser
config=configparser.RawConfigParser()
config.read(".\\configuration\\config.ini")

class Readconfig():
    @staticmethod
    def getapplicationURL():
        url=config.get('page info','myurl')
        return url

    @staticmethod
    def radiobutton1xpath():
        radio1=config.get('Radio Button Example','radio1')
        return radio1

    @staticmethod
    def radiobutton2xpath():
        radio2=config.get('Radio Button Example','radio2')
        return radio2

    @staticmethod
    def radiobutton3xpath():
        radio3=config.get('Radio Button Example','radio3')
        return radio3

    @staticmethod
    def checkbox1():
        option1=config.get('Checkbox Example','option1')
        return option1

    @staticmethod
    def checkbox2():
        option2=config.get('Checkbox Example','option2')
        return option2

    @staticmethod
    def checkbox3():
        option3=config.get('Checkbox Example','option3')
        return option3
