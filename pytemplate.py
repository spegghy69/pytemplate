#!/usr/bin/env python3.9
# -*- coding: utf-8 -*-
# pylint: disable=line-too-long
####################################################

import os
import sys
import argparse

import logging
import logging.config
import logging.handlers

from logging.handlers import RotatingFileHandler
from pathlib import Path

import configparser

from datetime import date, datetime


### MAIN ####
__version__ = '0.1.0'
__version_date__ = '2024-10-04'

# # # #  # # # # # # # # # # # # #
#  Global variables and setup    #
#  don't touch                   #
# # # #  # # # # # # # # # # # # #

LOGGERS_INI = 'loggers.ini'
CONFIG_INI = 'config.ini'
DATA_PATH="./data/"
LOG_PATH="./log/"
OK_CODE = 0
WARNING_CODE = 1
CRITICAL_CODE = 2
UNKNOWN_CODE = 3

path_current_directory = os.path.dirname(os.path.realpath(__file__))

# read config file
path_config_ini_file = os.path.join(path_current_directory,  CONFIG_INI)
if not os.path.isfile(path_config_ini_file):
    print("Missing configuration file %s" , path_config_ini_file )
    sys.exit(CRITICAL_CODE)
cfg = configparser.ConfigParser()
cfg.read(path_config_ini_file)

# Set logger  to script name + log extension
path_logger_ini_file = os.path.join(path_current_directory,  LOGGERS_INI)
if not os.path.isfile(path_logger_ini_file):
    print("Missing configuration file %s" , path_logger_ini_file )
    sys.exit(CRITICAL_CODE)

# create log dir
log_dir  = os.path.join(path_current_directory, LOG_PATH)
os.makedirs(log_dir, exist_ok=True)

log_name  = os.path.join(path_current_directory, LOG_PATH, Path(__file__).stem+".log")
logging.config.fileConfig(path_logger_ini_file,  defaults={'logfilename': log_name} )
logger = logging.getLogger(__name__)

# create data dir
data_dir  = os.path.join(path_current_directory, DATA_PATH)
os.makedirs(data_dir, exist_ok=True)

# # # # # # # # # # # # # # #
#  Script global variables  #
# # # # # # # # # # # # # # #

FAKEOPTION= False
# Set elaboration date
today = date.today().strftime("%Y-%m-%d")
dataelab  = datetime.today().strftime("%Y-%m-%d %H:%M:%S%z")

# # # # # # # # # # # #
#  Custom function    #
# # # # # # # # # # # #

def fake()
    ''' template for fake function '''

    try:

        exit_code = OK_CODE
        return exit_code

    except Exception as error:
        logger.error("CRITICAL - An unhandled exception occured during script execution.")
        logger.error("Exception (args): %s", str(error))
        logger.error("Exception (type): %s", str(type(error)))
        logger.error("Exception (line): %s", str(error.__traceback__.tb_lineno))
        sys.exit(CRITICAL_CODE)




def parse_args():
    ''' parse CLI arguments '''

    # Arguments definition
    parser = argparse.ArgumentParser(description="Description ")
    parser.add_argument("-v", "--version", help="show program version", action="store_true")
    parser.add_argument('-d', '--debug', help="enable debug mode", action='store_true')
    parser.add_argument('-f', '--fakeoption', help="fakeoption", action='store_true')

    # Read arguments from command line
    args = parser.parse_args()

    # version
    if args.version:
        print(__version__)
        sys.exit(0)

    # log verbosity
    if args.debug:
        logging.getLogger().setLevel(logging.DEBUG)
        logger.debug("Activate debug level")
    else:
        logging.getLogger().setLevel(logging.INFO)

    #
    global FAKEOPTION
    if args.fakeoption:
        FAKEOPTION = True

    return args



def main():
    ''' main part '''
    logger.info("Starting")

    args=parse_args()

    if FAKEOPTION:
        fake()

    logger.info("Ending")

    result = OK_CODE
    sys.exit(result)

if __name__=='__main__':
    main()
