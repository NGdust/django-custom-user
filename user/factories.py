import factory

from faker import Factory as FakerFactory
faker = FakerFactory.create()
from user import models


class UserFactory(factory.DjangoModelFactory):
    email = factory.LazyAttribute(lambda x: faker.email())
    name = factory.LazyAttribute(lambda x: faker.name())
    password = factory.LazyAttribute(lambda x: faker.password())

    class Meta:
        model = models.User