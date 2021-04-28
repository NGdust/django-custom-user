from rest_framework import serializers
from enum import Enum


class ChoiceEnum(Enum):
    @classmethod
    def choices(cls):
        return tuple((item.value, item.name) for item in cls)

    def __str__(self):
        return self.name

    def __int__(self):
        return self.value


class ChoicesField(serializers.Field):
    default_error_messages = {
        'invalid_choice': '"{input}" is not a valid choice.'
    }

    def __init__(self, choices, **kwargs):
        self.choices = dict(choices)
        self.values = dict((v, k) for k,v in choices)
        self.allow_blank = kwargs.pop('allow_blank', False)
        super(ChoicesField, self).__init__(**kwargs)

    def to_internal_value(self, data):
        if data == '' and self.allow_blank:
            return None
        if data is None and self.allow_null:
            return None

        try:
            return self.values[data]
        except KeyError:
            self.fail('invalid_choice', input=data)

    def to_representation(self, value):
        if value in ('', None):
            return None
        return self.choices[value]


class CommonField(serializers.Field):
    default_error_messages = {
        'not_found': 'Channel not found',
        'invalid': 'Invalid json'
    }

    def to_internal_value(self, data):
        try:
            model = self.model.objects.get(id=int(data['id']))
        except (ValueError, KeyError):
            self.fail('invalid')
        except self.model.DoesNotExist:
            self.fail('not_found')
        return model

    def to_representation(self, model):
        data = self.serializer(model).data
        return data
