import logging
class Logclass:
    @staticmethod
    def getthelog():
        logger=logging.getLogger()
        filehandler=logging.FileHandler("shubham.log")
        formatter=logging.Formatter('%(asctime)s: %(levelname)s: %(message)s',datefmt='%m/%d/%Y %I:%M:%S %p')
        filehandler.setFormatter(formatter)
        logger.setLevel(logging.DEBUG)


        return logger

