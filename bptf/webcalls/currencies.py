from bptf.settings import WEBSITE, CURRENCIES
from bptf.utils import verify_format_type, check_status_code, \
    check_permissions
from requests import get as _get


class Currencies:

    def __init__(self, key, _format='json', raw=0):
        if check_permissions(_get("{}{}?key={}".format(WEBSITE, CURRENCIES, key)).json()):
            pass
        if not verify_format_type(_format):
            raise ValueError('{} is not a valid format type'.format(_format))
        self.key = '?key=' + key
        self.format = '&format=' + _format
        self.raw = '&raw=' + str(raw)
        self.url = r'{}{}{}{}{}'.format(
            WEBSITE, CURRENCIES,
            self.key, self.format, self.raw
        )
        self.data = self.__get()

    def __get(self):
        response = _get(self.url)
        check, _ = check_status_code(response.status_code)
        if check:
            return response.json()
