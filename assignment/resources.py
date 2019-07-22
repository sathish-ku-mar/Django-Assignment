from import_export import resources
from .models import Adult


class AdultResource(resources.ModelResource):

    class Meta:
        model = Adult
        fields = ('id', 'age', 'work', 'fnlwgt', 'education', 'education_num', 'marital_status', 'occupation', 'relationship',
                        'race', 'sex', 'capital_gain', 'capital_loss', 'hours_per_week', 'native_country', 'salary')