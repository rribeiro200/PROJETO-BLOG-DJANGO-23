# Generated by Django 5.0 on 2023-12-12 00:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_setup', '0004_sitesetup_favicon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sitesetup',
            name='favicon',
            field=models.ImageField(blank=True, default='', upload_to='assets/favicon/%Y/%m/'),
        ),
    ]