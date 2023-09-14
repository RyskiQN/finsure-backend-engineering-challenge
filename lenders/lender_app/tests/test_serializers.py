from django.test import TestCase

from ..serializers import LenderSerializer
from .factories import LenderFactory


class LenderSerializerTest(TestCase):
    def test_model_fields(self):
        """Serializer data matches the Company object for each field."""
        lender = LenderFactory()
        serializer = LenderSerializer(lender)
        for field_name in [
            'id', 'name', 'description', 'website', 'street_line_1', 'street_line_2',
            'city', 'state', 'zipcode'
        ]:
            self.assertEqual(
                serializer.data[field_name],
                getattr(lender, field_name)
            )