from django.contrib import admin
from . import models
from django_jalali.admin.filters import JDateFieldListFilter

# Register your models here.


@admin.register(models.reshte)
class Reshte_name_Admin(admin.ModelAdmin):
	pass


class kargar_inline(admin.TabularInline):
	model = models.kagar_cyrus


@admin.register(models.personel_cyrus)
class Personel_cyrus_Admin(admin.ModelAdmin):
	inlines = [kargar_inline]

	list_filter = (
		('birth_day', JDateFieldListFilter),
	)

	list_display = ('l_name', 'birth_day')

	fields = (
		('f_name', 'l_name'),
		('meli_code', 'birth_day', 'address'),
		('celphone_one', 'tel_sabet'),
		('maghtae_tahsili', 'reshte_tahsili', 'semat')
	)


@admin.register(models.kagar_cyrus)
class PersonelAdmin(admin.ModelAdmin):
	#list_display = ('l_name', 'f_name')
	list_display = ( 'l_name', 'f_name', 'id', 'meliyat','birthday', 'tel_cellphone', 'address', 'vaziyet_kari')
	fields = (
		('f_name', 'l_name'),
		('meliyat', 'vaziyet_kari', 'meli_code', 'birthday'),
		'address',
		('tel_cellphone', 'tel_sabet'),
		'moaref_kargar',
	)
	list_filter = ('meliyat', 'vaziyet_kari')


@admin.register(models.project_cyrus)
class projectAdmin(admin.ModelAdmin):
	pass

class karkardinline(admin.TabularInline):
	model = models.karkard
	extra = 1
	max_num = 25

@admin.register(models.sabteruz)
class sabteruzAdmin(admin.ModelAdmin):
	inlines = [karkardinline]
	fields = (('tarikh', 'project', 'user'), 'dsc')
	list_filter = ('tarikh', 'project', 'user')



