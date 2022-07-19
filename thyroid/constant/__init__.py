import os
from datetime import datetime
from tkinter import CURRENT

from thyroid.config.configuration import ROOT_DIR

ROOT_DIR = os.getcwd()  # to get current working directory

CONFIG_DIR = "config"
CONFIG_FILE_NAME = "config.yaml"
CONFIG_FILE_PATH = os.path.join(ROOT_DIR, CONFIG_DIR, CONFIG_FILE_NAME)


CURRENT_TIME_STAMP = f"{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}"