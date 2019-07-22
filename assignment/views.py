from django.db.models import Count
from rest_framework import viewsets
from rest_framework.response import Response
from .models import Adult
from .serializers import AdultSerializer
from .resources import AdultResource
from tablib import Dataset


class AdultViewSet(viewsets.ViewSet):

    model = Adult
    queryset = model.objects.filter(active=True)
    serializer_class = AdultSerializer

    def list(self, request):
        """
           To list the all adult data set
           URL Structure: /assignment/api/
           Required Fields: None
        """
        result = {}
        result['data'] = self.serializer_class(self.queryset, many=True).data

        result['sex'] = self.queryset.values('sex').annotate(count=Count('sex'))
        result['relationship'] = self.queryset.values('relationship').annotate(count=Count('relationship'))
        return Response(result)

    def create(self, request):
        """
            To import CSV file to DB
            URL Structure: /assignment/api/
            Required Fields: myfile
        """

        adult_resource = AdultResource()
        dataset = Dataset()
        myfile = request.FILES['myfile']

        file_data = dataset.load(myfile.read().decode('utf-8'), format='csv')
        data = Dataset()
        data.headers = ('id', 'age', 'work', 'fnlwgt', 'education', 'education_num', 'marital_status', 'occupation', 'relationship',
                        'race', 'sex', 'capital_gain', 'capital_loss', 'hours_per_week', 'native_country', 'salary')

        for i in range(0, len(file_data)-1):
            l = list(file_data[i])
            l.insert(0, i+1)
            data.append(tuple(l))

        result = adult_resource.import_data(data, dry_run=True)  # Test the data import
        if not result.has_errors():
            adult_resource.import_data(data, dry_run=False)  # Actually import now
        pass

        return Response('Success')