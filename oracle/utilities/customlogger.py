import logging
import pytest
class Logclass:
    def getthelog(self):
        logger=logging.getLogger()
        filehandler=logging.FileHandler("mylogfile.log",mode="w")
        formatter=logging.Formatter('%(asctime)s: %(levelname)s: %(message)s',datefmt='%m/%d/%Y %I:%M:%S %p')
        filehandler.setFormatter(formatter)
        logger.addHandler(filehandler)
        logger.setLevel(logging.DEBUG)
        return logger



# class LogGen:
#     @staticmethod
#     def loggen():
#         logging.basicConfig(
#             filename=".\\Logs\\automation.log",
#             format='%(asctime)s: %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
#         logger = logging.getLogger()
#         logger.setLevel(logging.INFO)
#         return logger




