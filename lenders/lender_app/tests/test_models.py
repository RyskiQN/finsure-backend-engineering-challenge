from django.test import TestCase

from ..models import Lender
from .factories import LenderFactory


class LenderTestCase(TestCase):
    def test_str(self):
        """Test for string representation."""
        lender = LenderFactory()
        self.assertEqual(str(lender), lender.name)