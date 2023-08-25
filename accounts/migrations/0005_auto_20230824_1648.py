# Generated by Django 3.2.20 on 2023-08-24 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20230810_1726'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='is_owner',
        ),
        migrations.AlterField(
            model_name='company',
            name='card_logo',
            field=models.ImageField(blank=True, null=True, upload_to='Card_logo/', verbose_name='Card_Logo'),
        ),
        migrations.AlterField(
            model_name='company',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to='Logo/', verbose_name='Logo'),
        ),
    ]
