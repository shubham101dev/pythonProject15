import logging

class LogGen:
    @staticmethod
    def log_gen():
        logging.basicConfig(filename=".\\Logs\\automation.log",
                        format='%(asctime)s: %(levelname)s: %(name)s %(threadName)s: %(message)',datefmt='%m%d%Y %I:%M:%s %p')
        logger=logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger





