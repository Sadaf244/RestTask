from django.db import models

# Create your models here.
class MainTable(models.Model):
    DataType=models.CharField(max_length=30)
    MainLocation=models.CharField(max_length=30)
    Capital = models.CharField(max_length=30)
    Population = models.FloatField(default=0)
    Language = models.CharField(max_length=150)

    def __str__(self):
        return self.DataType

class Population(models.Model):
    Population=models.FloatField(default=0)
    def __str__(self):
        return str(self.Population)

class Language(models.Model):
    Language=models.CharField(max_length=30)
    def __str__(self):
        return self.Language

class Country(models.Model):
    Country=models.CharField(max_length=30)
    Capital=models.CharField(max_length=30)
    foreign_id1=models.ForeignKey(Population, on_delete=models.CASCADE)
    foreign_id2 = models.ForeignKey(Language, on_delete=models.CASCADE)
    def __str__(self):
        return self.Country
class State(models.Model):
    State=models.CharField(max_length=30)
    Capital=models.CharField(max_length=30)
    foreign_id1 = models.ForeignKey(Population, on_delete=models.CASCADE)
    foreign_id2 = models.ForeignKey(Language, on_delete=models.CASCADE)
    def __str__(self):
        return self.State
class City(models.Model):
    City=models.CharField(max_length=30)
    Capital=models.CharField(max_length=30)
    foreign_id1 = models.ForeignKey(Population, on_delete=models.CASCADE)
    foreign_id2 = models.ForeignKey(Language, on_delete=models.CASCADE)
    def __str__(self):
        return self.City