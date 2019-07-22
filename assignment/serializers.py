from rest_framework import serializers

from .models import Adult


class AdultSerializer(serializers.ModelSerializer):

    class Meta:
        model = Adult
        fields = ('id', 'age', 'work', 'fnlwgt', 'education', 'education_num', 'marital_status', 'occupation', 'relationship',
                'race', 'sex', 'capital_gain', 'capital_loss', 'hours_per_week', 'native_country', 'salary')