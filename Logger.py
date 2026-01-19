import logging


logger = logging.getLogger('logger')
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler('logs.txt', encoding='utf-8')
file_handler.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s - %(filename)s - %(levelname)s - %(message)s')

file_handler.setFormatter(formatter)

logger.addHandler(file_handler)