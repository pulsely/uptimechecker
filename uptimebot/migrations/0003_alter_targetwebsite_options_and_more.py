# Generated by Django 4.1.1 on 2022-09-22 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uptimebot', '0002_alter_targetwebsite_flag_cdn_random_key_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='targetwebsite',
            options={'managed': True, 'ordering': ('url',), 'verbose_name': 'Target Website', 'verbose_name_plural': 'Target Websites'},
        ),
        migrations.AlterModelOptions(
            name='uptimecheck',
            options={'managed': True, 'ordering': ('-start_time',), 'verbose_name': 'Uptime Check', 'verbose_name_plural': 'Uptime Checks'},
        ),
        migrations.AddField(
            model_name='targetwebsite',
            name='title',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
