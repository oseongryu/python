#!usr/bin/env python3
from logging import handlers
import logging

#log settings
carLogFormatter = logging.Formatter('%(asctime)s,%(message)s')

#handler settings
carLogHandler = handlers.TimedRotatingFileHandler(filename='car.log', when='midnight', interval=1, encoding='utf-8')
carLogHandler.setFormatter(carLogFormatter)
carLogHandler.suffix = "%Y%m%d"

#logger set
carLogger = logging.getLogger()
carLogger.setLevel(logging.INFO)
carLogger.addHandler(carLogHandler)

#use logger
carLogger.info("car is coming")
carLogger.info("car is coming")