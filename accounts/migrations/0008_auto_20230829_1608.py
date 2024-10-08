# Generated by Django 3.2.20 on 2023-08-29 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_member_salesrepresentative_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='member_of',
            field=models.CharField(choices=[('admin', 'Admin'), ('dealer', 'Dealer'), ('repair_facility', 'Repair Facility'), ('sales_representative', 'Sales Representative'), ('agency', 'Agency')], default=[('admin', 'Admin'), ('dealer', 'Dealer'), ('repair_facility', 'Repair Facility'), ('sales_representative', 'Sales Representative'), ('agency', 'Agency')], max_length=50),
        ),
        migrations.DeleteModel(
            name='OtpVerify',
        ),
    ]
