from factory import Faker
from factory.django import DjangoModelFactory
from ..models import Lender


class LenderFactory(DjangoModelFactory):
    name = Faker('name')
    code = Faker('abbreviated name')
    upfront_com = Faker('percentage')
    trial_com = Faker('percentage')
    active = Faker('boolean')

    class Meta:
        model = Lender