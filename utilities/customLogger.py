import logging

class LogGen():
    @staticmethod
    def loggen():
        # Remove all handlers associated with the root logger object.
        for handler in logging.root.handlers[:]:
            logging.root.removeHandler(handler)
        logging.basicConfig(filename=".\\Logs\\automation.log",
                           format='%(asctime)s: %(levelname)s: %(message)s:',
                           datefmt='%m/%d/%Y %I:%M:%S %p'
                            )
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger
