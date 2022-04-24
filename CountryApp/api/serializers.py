from rest_framework import serializers
from CountryApp.models import MainTable,Country,State,City,Population,Language

class Table1Serializer(serializers.ModelSerializer):
    class Meta:
        model=MainTable
        fields="__all__"

class Table2Serializer(serializers.ModelSerializer):
    class Meta:
        model=Country
        fields="__all__"

class Table5Serializer(serializers.ModelSerializer):
    class Meta:
        model=State
        fields="__all__"

class Table6Serializer(serializers.ModelSerializer):
    class Meta:
        model=City
        fields="__all__"
class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model=Language
        fields="__all__"
class PopulationSerializer(serializers.ModelSerializer):
    class Meta:
        model=Population
        fields="__all__"