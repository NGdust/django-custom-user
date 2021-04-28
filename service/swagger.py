from django.utils.decorators import method_decorator
from drf_yasg.utils import swagger_auto_schema


def swagger_decorator(tags, methods=None):
    if methods is None:
        methods = ['list', 'create', 'update', 'destroy', 'retrieve', 'partial_update']

    def deco(f):
        decs = [
            method_decorator(name=method, decorator=swagger_auto_schema(tags=[tags])) for method in methods
        ]
        for dec in decs:
            f = dec(f)
        return f
    return deco