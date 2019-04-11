# Generated by Django 2.2 on 2019-04-11 07:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0018_sabteruz_dsc'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='sabteruz',
            options={'verbose_name': 'ثبت روز کاری', 'verbose_name_plural': 'لیست روزهای کاری'},
        ),
        migrations.AlterField(
            model_name='sabteruz',
            name='dsc',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='توضیحات'),
        ),
        migrations.CreateModel(
            name='karkard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vaziyat', models.CharField(choices=[('krg', 'کارگر'), ('ost', 'استادکار')], help_text='مشخص کنید که کارگر در امروز چه وضعیتی داشته', max_length=3, verbose_name='وضعیت کاری در روز')),
                ('desc', models.CharField(max_length=500, verbose_name='شرح کار')),
                ('kargar', models.ForeignKey(help_text='کارگر را از لیست انتخاب کنید', on_delete=django.db.models.deletion.DO_NOTHING, to='web.kagar_cyrus')),
                ('ruze_kari', models.ForeignKey(help_text='روز کاری را با دقت انتخاب کنید', on_delete=django.db.models.deletion.DO_NOTHING, to='web.sabteruz')),
            ],
        ),
    ]