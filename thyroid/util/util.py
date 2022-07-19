import yaml
from thyroid.exception import ThyroidException
import os,sys

def read_yaml_file(file_path:str) ->dict:
    """
    Reads a yaml file and returns a dictionary
    """
    try:
        with open(file_path, 'rb') as yaml_file:
            return yaml.safe_load(yaml_file)
    except Exception as e:
        raise ThyroidException(e,sys) from e