# Generated by Django 4.1.1 on 2022-09-22 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uptimebot', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='targetwebsite',
            name='flag_cdn_random_key',
            field=models.BooleanField(default=True, help_text='Add random GET parameter for proxy'),
        ),
        migrations.AlterField(
            model_name='targetwebsite',
            name='flag_check_ssl_expire_time',
            field=models.BooleanField(default=True, help_text='Check SSL expiration?', verbose_name='Check SSL Expire Time'),
        ),
        migrations.AlterField(
            model_name='targetwebsite',
            name='must_contain_keyword',
            field=models.CharField(blank=True, help_text='Keyword to check for successful', max_length=400, null=True),
        ),
        migrations.AlterField(
            model_name='targetwebsite',
            name='ssl_expire_time',
            field=models.DateTimeField(blank=True, help_text='Current SSL expiration time', null=True),
        ),
        migrations.AlterField(
            model_name='targetwebsite',
            name='url',
            field=models.CharField(help_text='URL of website to check', max_length=400),
        ),
    ]
