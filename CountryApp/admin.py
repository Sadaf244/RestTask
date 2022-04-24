from django.contrib import admin

from .models import MainTable,Country,State,City,Population,Language

admin.site.register(MainTable)
admin.site.register(Country)
admin.site.register(State)
admin.site.register(City)
admin.site.register(Population)
admin.site.register(Language)

