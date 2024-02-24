import os
import configparser

def get_config():
    script_dir = os.path.dirname(os.path.realpath(__file__))
    config_path = os.path.join(script_dir, 'properties.ini')
    config = configparser.ConfigParser()
    config.read(config_path)
    return config
