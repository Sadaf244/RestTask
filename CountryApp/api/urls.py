from CountryApp.api.views import (Table1List,Table1Create,Table1Retreive,
                         Table2List,Table2Create,Table5List,Table5Create,
                         Table6List,Table6Create,PopulationCreate,LanguageCreate)
from django.urls import path,include

urlpatterns = [
    path('list/', Table1List.as_view()),# API for getting list of Main Table and get data by Languagewise,Type Of Data,Location Name
    path('create/', Table1Create.as_view()), # Api for creating of Main Table
    path('retreive/<int:pk>/', Table1Retreive.as_view()), # Api for retreiving individual data of Main Table
    path('listcountry/', Table2List.as_view()),# Api for retreiving individual data of Country Table
    path('createcountry/', Table2Create.as_view()),# Api for creating of Country Table
    path('liststate/', Table5List.as_view()),# Api for retreiving individual data of State Table
    path('createstate/', Table5Create.as_view()),# Api for creating of State Table
    path('listcity/', Table6List.as_view()),# Api for retreiving individual data of City Table
    path('createcity/', Table6Create.as_view()),# Api for creating of City Table
    path('createlanguage/', LanguageCreate.as_view()),# Api for creating of Language Table
    path('createpopulation/', PopulationCreate.as_view()),# Api for creating of Population Table

    ]