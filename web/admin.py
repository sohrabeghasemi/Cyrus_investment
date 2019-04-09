from django.contrib import admin
from . import models

# Register your models here.


@admin.register(models.reshte)
class Reshte_name_Admin(admin.ModelAdmin):
	pass


@admin.register(models.personel_cyrus)
class Personel_cyrus_Admin(admin.ModelAdmin):
	fields = (('f_name', 'l_name'),
			  'meli_code', 'address',
			  ('celphone_one', 'tel_sabet'),
			  ('maghtae_tahsili', 'reshte_tahsili'))


@admin.register(models.kagar_cyrus)
class PersonelAdmin(admin.ModelAdmin):
	#list_display = ('l_name', 'f_name')
	fields = (('f_name', 'l_name'), ('meliyat', 'vaziyet_kari'),'address', ('tel_cellphone','tel_sabet'),'moaref_kargar')


@admin.register(models.project_cyrus)
class projectAdmin(admin.ModelAdmin):
	pass


