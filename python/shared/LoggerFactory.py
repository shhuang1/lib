import os
import logging
import socket

from shared.Constants import *

def get_logger(log_file='',logger_name=None,file_level=LOGGER_LEVEL,file_format=LOGGER_FORMAT,file_mode='w',console_level=LOGGER_LEVEL,console_format=LOGGER_FORMAT):
    if (logger_name==None):
        logger = logging.getLogger()
    else:
        logger = logging.getLogger(logger_name)
    if (log_file!=''):
        file = logging.FileHandler(log_file,mode=file_mode)
        formatter1 = logging.Formatter(file_format)
        file.setFormatter(formatter1)
        logger.addHandler(file)
    
    console = logging.StreamHandler()
    formatter2 = logging.Formatter(console_format)
    console.setFormatter(formatter2)
    logger.addHandler(console)
    #print 'Logger factory LOGGER:',logger.name,logger_name
    logger.setLevel(file_level)
    return logger

def log_command(logger,cmd_array):
    logger.info('host: '+socket.getfqdn())
    logger.info('cwd: '+os.getcwd())
    cmd = 'command: '+' '.join(cmd_array)
    logger.info(cmd)

