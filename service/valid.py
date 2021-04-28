import re


def is_valid_email(email):
    return re.match(r'(^|\s)[-a-zA-Z0-9_.]+@([-a-z0-9]+\.)+[a-z]{2,6}(\s|$)', email)

def is_valid_phone(phone):
    return re.match(r'^((\+7|7|8)+([0-9]){10})$', phone)