from rest_framework.generics import ListAPIView,CreateAPIView,RetrieveAPIView
from CountryApp.api.serializers import Table1Serializer,Table2Serializer,Table5Serializer,Table6Serializer,LanguageSerializer,PopulationSerializer
from CountryApp.models import MainTable,Country,State,City,Population,Language
from django_filters.rest_framework import DjangoFilterBackend

class Table1List(ListAPIView):
    serializer_class = Table1Serializer
    queryset=MainTable.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ('Language', 'DataType','MainLocation')

class Table1Create(CreateAPIView):
    serializer_class = Table1Serializer
    queryset=MainTable.objects.all()
class Table1Retreive(RetrieveAPIView):
    serializer_class = Table1Serializer
    queryset=MainTable.objects.all()
class PopulationCreate(CreateAPIView):
    serializer_class = PopulationSerializer
    queryset=Population.objects.all()
class LanguageCreate(CreateAPIView):
    serializer_class = LanguageSerializer
    queryset=Language.objects.all()
class Table2List(ListAPIView):
    serializer_class = Table2Serializer
    queryset=Country.objects.all()
class Table2Create(CreateAPIView):
    serializer_class = Table2Serializer
    queryset=Country.objects.all()

class Table5List(ListAPIView):
    serializer_class = Table5Serializer
    queryset=State.objects.all()
class Table5Create(CreateAPIView):
    serializer_class = Table5Serializer
    queryset=State.objects.all()

class Table6List(ListAPIView):
    serializer_class = Table6Serializer
    queryset=City.objects.all()
class Table6Create(CreateAPIView):
    serializer_class = Table6Serializer
    queryset=City.objects.all()
