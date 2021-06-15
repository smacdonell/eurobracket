from functools import reduce

from django.conf import settings
import json

"""
 For reading JSON properties.
"""


class JsonPropertyReader:
    """
     Domain is the filename, key is the JSON key.
     Ex: read_value('form', ('a', 'b')) will read key json['a', 'b'] from file form.json
    """

    @staticmethod
    def read_value(domain, key):
        file = settings.PROPS_DIR + domain + '.json'

        try:
            with open(file) as json_file:
                data = json.load(json_file)
                return reduce(dict.get, key, data)
        except OSError as e:
            return None

        return None
