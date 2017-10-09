from bptf.settings import WEBSITE, SPECIAL_ITEMS, APPID_TF2
from bptf.utils import verify_format_type, check_status_code, \
    check_permissions
from requests import get as _get


class SpecialItems:

    def __init__(self, key, _format='json', appid=APPID_TF2):
        if check_permissions(_get("{}{}?key={}".format(WEBSITE, SPECIAL_ITEMS, key)).json()):
            pass
        if not verify_format_type(_format):
            raise ValueError('{} is not a valid format type'.format(_format))
        self.key = '?key=' + key
        self.format = '&format=' + _format
        # self.appid = '&appid=' + str(appid)
        self.url = r'{}{}{}{}'.format(
            WEBSITE, SPECIAL_ITEMS,
            self.key, self.format
        )
        self.data = self.__get()

    def __get(self):
        response = _get(self.url)
        check, _ = check_status_code(response.status_code)
        if check:
            return response.json()
