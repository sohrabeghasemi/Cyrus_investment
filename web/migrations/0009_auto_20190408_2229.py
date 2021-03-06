# Generated by Django 2.2 on 2019-04-09 05:29

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0008_kagar_cyrus_moaref_kargar'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='kagar_cyrus',
            options={'verbose_name': 'کارگرها', 'verbose_name_plural': 'لیست کارگرها'},
        ),
        migrations.AlterModelOptions(
            name='personel_cyrus',
            options={'verbose_name': 'پرسنل', 'verbose_name_plural': 'لیست پرسنل'},
        ),
        migrations.AlterModelOptions(
            name='project_cyrus',
            options={'verbose_name': 'پروژه', 'verbose_name_plural': 'لیست پروژه ها'},
        ),
        migrations.AlterModelOptions(
            name='reshte',
            options={'verbose_name': 'رشته تحصیلی', 'verbose_name_plural': 'لیست رشته های تحصیلی'},
        ),
        migrations.RemoveField(
            model_name='kagar_cyrus',
            name='vorud_date',
        ),
        migrations.AddField(
            model_name='kagar_cyrus',
            name='created',
            field=models.DateField(default=django.utils.timezone.now, editable=False),
        ),
        migrations.AddField(
            model_name='kagar_cyrus',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
