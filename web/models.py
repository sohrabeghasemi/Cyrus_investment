from django.db import models
import uuid
# Create your models here.


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

