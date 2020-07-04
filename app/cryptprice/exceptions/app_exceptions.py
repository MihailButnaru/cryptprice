from rest_framework.exceptions import APIException

__author__ = "Mihail Butnaru"
__copyright__ = "Copyright 2020, All rights reserved."


class APPServerError(APIException):
    status_code = 500
    default_detail = "Service temporarily unavailable, contact the administrator"
    default_code = "internal_server_error"
