import logging
import os

DEBUG = os.getenv("ENVIRONEMENT") == "DEV"

APPLICATION_ROOT = os.getenv("APPLICATION_ROOT", "/")
HOST = os.getenv("APPLICATION_HOST")
PORT = os.getenv("APPLICATION_PORT", "3001")
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = os.getenv("APPLICATION_SECRET_KEY")
IMAGE_URL = '/mnt/static/image/'

EXCEL_FOLDER_PATH = os.getenv("EXCEL_FOLDER_PATH", "/Users/user/programming/digital-twin/ExcelRetriver/dummy_data")

VARIABLES_CELL = os.getenv("VARIABLES_ROWS", "B7")
UNIT_CELL = os.getenv("VARIABLES_ROWS", "C7")
VALUE_CELL = os.getenv("VARIABLES_ROWS", "D7")

logging.basicConfig(
    filename=os.getenv("SERVICE_LOG", "server.log"),
    level=logging.DEBUG,
    format="%(levelname)s: %(asctime)s \
        pid:%(process)s module:%(module)s %(message)s",
    datefmt="%d/%m/%y %H:%M:%S",
)
