import logging, os
import logging.handlers
import datetime,time

logger = logging.getLogger("basic_logger")
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler(os.path.join(os.path.abspath(os.path.dirname(__file__)), "logs", "log_{}.txt".format(time.strftime("%d_%m_%Y"))))
file_handler.setFormatter(logging.Formatter('[%(asctime)s] - [%(filename)s file line:%(lineno)d] - %(levelname)s: %(message)s'))
file_handler.setLevel(logging.DEBUG)

console_handler = logging.StreamHandler()
console_handler.setFormatter(logging.Formatter('%(levelname)s: %(message)s'))
console_handler.setLevel(logging.DEBUG)

logger.addHandler(file_handler)
logger.addHandler(console_handler)
