from rest_framework_json_api import serializers
from .models import Lender


class LenderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lender
        fields = ('name', 'code', 'upfront_com',
                'trial_com', 'active')
