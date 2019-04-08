from django.contrib import admin
from . import models

# Register your models here.


@admin.register(models.kagar_cyrus)
class PersonelAdmin(admin.ModelAdmin):
	list_display = ('l_name', 'f_name')
	fields = (('f_name','l_name'), ('meliyat', 'vaziyet_kari'), 'vorud_date')


