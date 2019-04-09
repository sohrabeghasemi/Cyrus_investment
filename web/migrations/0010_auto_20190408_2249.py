# Generated by Django 2.2 on 2019-04-09 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0009_auto_20190408_2229'),
    ]

    operations = [
        migrations.AddField(
            model_name='kagar_cyrus',
            name='address',
            field=models.CharField(help_text='آدرس را در این قسمت وارد کنید', max_length=300, null=True, verbose_name='آدرس'),
        ),
        migrations.AddField(
            model_name='kagar_cyrus',
            name='tel_cellphone',
            field=models.CharField(help_text='لطفا شماره تلفن همراه را در این حالت وارد کنید 09113910400', max_length=11, null=True, verbose_name='شماره تلفن همراه'),
        ),
        migrations.AddField(
            model_name='kagar_cyrus',
            name='tel_sabet',
            field=models.CharField(help_text='لطفا شماره تلفن همراه را در این حالت وارد کنید 01154633340', max_length=11, null=True, verbose_name='شماره تلفن ثابت'),
        ),
        migrations.AlterField(
            model_name='kagar_cyrus',
            name='created',
            field=models.DateField(auto_now_add=True),
        ),
    ]