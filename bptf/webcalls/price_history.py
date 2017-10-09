from bptf.settings import WEBSITE, COMMUNITY_PRICE_HISTORY, APPID_TF2
from bptf.utils import verify_format_type, check_status_code, \
    check_permissions
from requests import get as _get


class PriceHistory:

    def __init__(self, key, item, quality, tradable, craftable, _format='json', appid=APPID_TF2):
        if not verify_format_type(_format):
            raise ValueError('{} is not a valid format type'.format(_format))

        if tradable not in [1, 0]:
            raise ValueError('tradable must be 0 (False) or 1 (True)')

        if craftable not in [1, 0]:
            raise ValueError('craftable must be 0 (False) or 1 (True)')

        self.key = '?key=' + key
        self.format = '&format=' + _format
        self.item = '&item={}'.format(item.replace(' ', '+'))
        self.quality = '&quality=' + str(quality)
        self.tradable = '&tradable=' + str(tradable)
        self.craftable = '&craftable=' + str(craftable)

        self.url = r'{}{}{}{}{}{}{}{}'.format(
            WEBSITE, COMMUNITY_PRICE_HISTORY,
            self.key, self.format, self.item,
            self.quality, self.tradable,
            self.craftable
        )

        if check_permissions(_get(self.url).json()):
            pass

        self.data = self.__get()

    def __get(self):
        response = _get(self.url)

        check, _ = check_status_code(response.status_code)
        if check:
            return response.json()
