# Generated by Django 2.2 on 2019-04-11 07:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0015_sabteruz'),
    ]

    operations = [
        migrations.AlterField(
            model_name='karkard_cyrus',
            name='tarikh',
            field=models.ForeignKey(help_text='تاریخ روز کاری مورد نظر را مشخص کنید', on_delete=django.db.models.deletion.DO_NOTHING, to='web.sabteruz'),
        ),
    ]