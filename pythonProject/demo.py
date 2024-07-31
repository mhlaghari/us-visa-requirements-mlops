from us_visa.logger import logging
from us_visa.exception import USVisaException


logging.info("Welcome to our custom logging")

try:
    2/0
except Exception as e:
    raise USVisaException
