from rest_framework.viewsets import ModelViewSet

from factory_app.models import Table, Leg, Feet
from factory_app.serializers import TableSerializer, LegSerializer, FeetSerializer, GETTableSerializer


# Create your views here.
# Upon visiting the home page the the default basic urls for corresponding views via DefaultRouter will be presented.

class TableModelViewSet(ModelViewSet):
    queryset = Table.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return GETTableSerializer
        return TableSerializer


class LegModelViewSet(ModelViewSet):
    queryset = Leg.objects.all()
    serializer_class = LegSerializer


class FeetModelViewSet(ModelViewSet):
    queryset = Feet.objects.all()
    serializer_class = FeetSerializer
