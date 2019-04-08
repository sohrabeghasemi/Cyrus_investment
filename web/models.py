from django.db import models
import uuid
# Create your models here.


class reshte(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	reshte_name = models.CharField(max_length=200)

	def __str__(self):
		return self.reshte_name


class project_cyrus(models.Model):
	name_project = models.CharField('نام پروژه', max_length=50)
	address_project = models.CharField('آدرس پروژه', max_length=300)
	units_project = models.CharField('تعداد واحد ها', max_length=2)
	desc_project = models.TextField('توضیحات تکمیلی')

	def __str__(self):
		return self.name_project


class personel_cyrus(models.Model):

	MAGHTAE_TAHSILI_CHOICES = (
		('ci', 'سیکل'),
		('dp', 'دیپلم'),
		('fd', 'فوق دیپلم'),
		('li', 'لیسانس'),
		('fl', 'فوف لیسانس'),
		('dr', 'دکترا'),
	)

	f_name = models.CharField('نام', max_length=200)
	l_name = models.CharField('نام خانوادگی', max_length=250)
	meli_code = models.CharField('کد ملی', max_length=10)
	address = models.CharField('آدرس', max_length=300)
	celphone_one = models.CharField('شماره تلفن همراه', max_length=11, help_text='لطفا شماره تلفن همراه را در این حالت وارد کنید 09113910400')
	tel_sabet =models.CharField('شماره تلفن ثابت', max_length=11)
	maghtae_tahsili = models.CharField('مقطع تحصیلی',
									   max_length=2,
									   choices=MAGHTAE_TAHSILI_CHOICES,
									   default='dp',
									   )
	reshte_tahsili = models.ForeignKey(reshte, 'رشته تحصیلی')

	def __str__(self):
		return '{} {}'.format(self.f_name, self.l_name)


class kagar_cyrus(models.Model):

	MELIYAT_CHOICES = (
		('IR', 'ایرانی'),
		('AF', 'افغانی'),
	)

	VAZIYAT_KARI_CHOICES = (
		('krg', 'کارگر'),
		('ost', 'استادکار'),
	)
	f_name = models.CharField('نام', max_length=200)
	l_name = models.CharField('نام خانوادگی', max_length=250)
	meliyat = models.CharField('ملیت', max_length=2, choices=MELIYAT_CHOICES)
	vaziyet_kari = models.CharField('وضعیت کاری', max_length=3, choices=VAZIYAT_KARI_CHOICES)
	vorud_date = models.DateField('تاریخ ورود به پروژه')
	moaref_kargar = models.ForeignKey(personel_cyrus,'معرف', null=True)

	def __str__(self):
		return '{} , {} {} , {} , {}'.format(self.id, self.f_name, self.l_name, self.vaziyet_kari, self.meliyat)

