from django.db import models
import uuid
from django_jalali.db import models as jmodels
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.conf import settings
# Create your models here.


class reshte(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	reshte_name = models.CharField(max_length=200)

	class Meta:
		verbose_name = 'رشته تحصیلی'
		verbose_name_plural = 'لیست رشته های تحصیلی'

	def __str__(self):
		return self.reshte_name


class project_cyrus(models.Model):
	name_project = models.CharField('نام پروژه', max_length=50)
	address_project = models.CharField('آدرس پروژه', max_length=300)
	units_project = models.CharField('تعداد واحد ها', max_length=2)
	desc_project = models.TextField('توضیحات تکمیلی')

	class Meta:
		verbose_name = 'پروژه'
		verbose_name_plural = 'لیست پروژه ها'

	def __str__(self):
		return '{} '.format(self.name_project)


class personel_cyrus(models.Model):

	SEMAT_CHOICES = (
		('modir_project', 'مدیر پروژه'),
		('mohandes', 'مهندس '),
		('ranande', 'راننده'),
		('modir_hesabdar', 'مدیر حسابداری'),
		('anbardar', 'انباردار'),
		('tarrah', 'معمار پروژه'),
		('monshi', 'منشی'),
		('vakil', 'وکیل'),
	)

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
	birth_day = jmodels.jDateField('تاریخ تولد', null=True, blank=True)
	meli_code = models.CharField('کد ملی', max_length=10)
	address = models.CharField('آدرس', max_length=300)
	celphone_one = models.CharField('شماره تلفن همراه', max_length=11,
									help_text='لطفا شماره تلفن همراه را در این حالت وارد کنید 09113910400',
									)
	tel_sabet =models.CharField('شماره تلفن ثابت', max_length=11)
	maghtae_tahsili = models.CharField('مقطع تحصیلی',
									max_length=2,
									choices=MAGHTAE_TAHSILI_CHOICES,
									default='dp',
									)
	reshte_tahsili = models.ForeignKey(reshte, 'رشته تحصیلی')
	semat = models.CharField('سمت در پروژه', choices=SEMAT_CHOICES, max_length=50,
							 null=True, blank=True,help_text='سمت را در این قسمت انتخاب کنید')


	class Meta:
		verbose_name = 'پرسنل'
		verbose_name_plural = 'لیست پرسنل'

	def __str__(self):
		return '{} {}, {}'.format(self.f_name, self.l_name, self.birth_day)


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
	meli_code = models.CharField('کد ملی', max_length=10, help_text='ورود کد ملی ۱۰ رقمی', null=True, blank=True)
	birthday = jmodels.jDateField('تاریخ تولد', help_text='تاریخ تولد را وارد کنید', null=True, blank=True)
	meliyat = models.CharField('ملیت', max_length=2, choices=MELIYAT_CHOICES)
	vaziyet_kari = models.CharField('وضعیت کاری', max_length=3, choices=VAZIYAT_KARI_CHOICES)
	moaref_kargar = models.ForeignKey(personel_cyrus, 'معرف', null=True)
	address = models.CharField('آدرس', max_length=300, help_text='آدرس را در این قسمت وارد کنید')
	tel_cellphone = models.CharField('شماره تلفن همراه', max_length=11,
									help_text='لطفا شماره تلفن همراه را در این حالت وارد کنید 09113910400',
									)
	tel_sabet = models.CharField('شماره تلفن ثابت', max_length=11,
									help_text='لطفا شماره تلفن همراه را در این حالت وارد کنید 01154633340',
									)
	created = models.DateField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	class Meta:
		verbose_name = 'کارگرها'
		verbose_name_plural = 'لیست کارگرها'

	def __str__(self):
		return 'کد کارگر :{} ,  نام : {} {} , {} , {}'.format(self.id, self.f_name, self.l_name, self.vaziyet_kari, self.meliyat)


class sabteruz(models.Model):
	current_user = get_user_model()
	tarikh = jmodels.jDateField('تاریخ', help_text='تاریخ روز کاری مورد نظر را مشخص کنید')
	project = models.ForeignKey(project_cyrus, on_delete=models.DO_NOTHING, help_text='پروژه مورد نظر را انتخاب کنید')
	user = models.ForeignKey(get_user_model(), on_delete=models.DO_NOTHING,null=True)
	dsc = models.CharField('توضیحات', max_length=200, null=True, blank=True)

	class Meta:
		verbose_name = 'ثبت روز کاری'
		verbose_name_plural = 'لیست روزهای کاری'

	def __str__(self):
		return 'تاریخ: {}/{}/{} پروژه: {} کاربر: {}'.format(self.tarikh.year, self.tarikh.month, self.tarikh.day,
															self.project, self.user)


class karkard(models.Model):

	VAZIYAT_KARI_CHOICES = (
		('krg', 'کارگر'),
		('ost', 'استادکار'),
	)

	ruze_kari = models.ForeignKey(sabteruz, on_delete=models.DO_NOTHING, help_text='روز کاری را با دقت انتخاب کنید')
	kargar = models.ForeignKey(kagar_cyrus, on_delete=models.DO_NOTHING, help_text='کارگر را از لیست انتخاب کنید')
	vaziyat = models.CharField('وضعیت کاری در روز', max_length=3, choices=VAZIYAT_KARI_CHOICES, help_text='مشخص کنید که کارگر در امروز چه وضعیتی داشته')
	desc = models.CharField('شرح کار', max_length=500)

	class Meta:
		verbose_name = 'ثبت کارکرد'
		verbose_name_plural = 'لیست کارکرد ها'

	def __str__(self):
		return '{} , {}, {}'.format(self.ruze_kari, self.kargar, self.vaziyat)




