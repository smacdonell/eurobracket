from django.conf import settings
import configparser

"""
 For reading string properties.
"""


class PropertyReader:
    config = configparser.ConfigParser()

    @staticmethod
    def read_string(domain, section, key):
        PropertyReader.config.read(settings.PROPS_DIR + domain + '.ini')
        return str(PropertyReader.config[section][key])

    @staticmethod
    def read_int(domain, section, key):
        PropertyReader.config.read(settings.PROPS_DIR + domain + '.ini')
        return int(PropertyReader.config[section][key])

    @staticmethod
    def read_bool(domain, section, key):
        PropertyReader.config.read(settings.PROPS_DIR + domain + '.ini')
        return bool(PropertyReader.config[section][key])