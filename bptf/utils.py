from bptf.exceptions import HTTPError, AccessError, SteamIdError
from bptf.settings import STATUS_CODE, PARTNER_ACCESS_MESSAGE
import re


def verify_format_type(t):
    if t not in ['json', 'jsonp', 'vdf', 'pretty']:
        return False
    return True


def check_status_code(status_code):
    msg = '[{}]: {}'.format(
        str(status_code),
        ['{}! {}'.format(x['response_name'], x['message']) for x in STATUS_CODE]
    )
    if status_code not in [200, 201]:
        raise HTTPError(status_code, msg=msg)
    return True, msg


def check_permissions(response):
    if response["response"]["success"] == 0:
        raise AccessError(PARTNER_ACCESS_MESSAGE)
    return True


def build_steam_ids(ids):
    if re.match(r'[\d]|,', ids):
        return ids.replace(',', '%2C')
    raise SteamIdError("Given steam id(s) are not valid. [{}]".format(ids))
