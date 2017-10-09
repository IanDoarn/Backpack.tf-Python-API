from bptf.settings import WEBSITE, USER_INFO
from bptf.utils import build_steam_ids, check_status_code, \
    check_permissions
from requests import get as _get


class UserInfo:

    def __init__(self, key, steamids):
        if check_permissions(_get("{}{}?key={}".format(WEBSITE, USER_INFO, key)).json()):
            pass
        self.key = '&key=' + key
        self.steamids = '?steamids={}'.format(build_steam_ids(steamids))
        self.url = '{}{}{}{}'.format(WEBSITE, USER_INFO, self.steamids, self.key)
        self.data = self.__get()

    def __get(self):
        response = _get(self.url)
        check, _ = check_status_code(response.status_code)
        if check:
            return response.json()
