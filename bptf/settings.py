# Constants used in the program
WEBSITE = r'http://backpack.tf'

# Web APIs
COMMUNITY_PRICES = r'/api/IGetPrices/v4'
CURRENCIES = r'/api/IGetCurrencies/v1'
USER_INFO = r'/api/users/info/v1'
COMMUNITY_PRICE_HISTORY = r'/api/IGetPriceHistory/v1'
SEARCH_CLASSIFIED_LISTINGS = r'/api/classifieds/search/v1'
SPECIAL_ITEMS = r'/api/IGetSpecialItems/v1'
MARKET_IMAGES = r'/api/market/images/v1'

# Access Message
PARTNER_ACCESS_MESSAGE = r"This web API requires partner access. " \
                         r"Please visit https://backpack.tf/developer for more information."

# App Ids
APPID_TF2 = 440
APPID_DOTA_2 = 570
APPID_CSGO = 730

# Status codes
STATUS_CODE = [
    {'code': 200, 'response_name': 'OK', 'message': 'A standard error-free response type for most methods.'},
    {'code': 201, 'response_name': 'Accepted',
     'message': 'Used in place of 200 OK if the request resulted in the creation of a resource, such as in POST methods'},
    {'code': 204, 'response_name': 'No_Content',
     'message': 'Used in place of 200 OK if the response is never expected to return a body, '
                'such as in DELETE methods.'},
    {'code': 400, 'response_name': 'Bad_Request',
     'message': 'Indicates an error with the supplied request body.'},
    {'code': 401, 'response_name': 'Unauthorized',
     'message': 'Indicates an error with user authorization. This will only be returned if the API key or '
                'OAuth user session is invalid.'},
    {'code': 403, 'response_name': 'Forbidden',
     'message': 'Implies an error with user access control for a resource. The user may not own the resource, '
                'or could perhaps be banned from interacting with the resource.'},
    {'code': 404, 'response_name': 'Not_Found', 'message': 'Returned if a resource cannot be found.'},
    {'code': 422, 'response_name': 'Unprocessable_Entity',
     'message': 'Indicates a validation error on the request body.'},
    {'code': 429, 'response_name': 'Too_Many_Requests',
     'message': 'Returned if the client is being throttled.'},
    {'code': 500, 'response_name': 'Internal_Server_Error',
     'message': 'Indicates a fatal error on the server.'},
    {'code': 501, 'response_name': 'Not_Implemented',
     'message': 'On resource APIs, will be returned if a request attempt is made to a resource that does not support that request method.'}
]
