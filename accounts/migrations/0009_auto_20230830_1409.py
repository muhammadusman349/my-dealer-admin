# Generated by Django 3.2.20 on 2023-08-30 09:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_auto_20230829_1608'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='SalesRepresentative_role',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.salesrepresentativerole'),
        ),
        migrations.AlterField(
            model_name='member',
            name='company_role',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.companyrole'),
        ),
        migrations.CreateModel(
            name='Dealer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=120)),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('country', models.CharField(max_length=220)),
                ('city', models.CharField(max_length=220)),
                ('state', models.CharField(max_length=220)),
                ('zip_code', models.CharField(max_length=120)),
                ('address', models.CharField(max_length=256)),
                ('phone', models.CharField(max_length=120, null=True)),
                ('fax', models.CharField(max_length=120)),
                ('dealer_prefix', models.CharField(max_length=120)),
                ('billing_cycle', models.IntegerField()),
                ('ach_fee', models.IntegerField()),
                ('logo', models.ImageField(blank=True, null=True, upload_to='Logo/', verbose_name='Logo')),
                ('max_claim_for_auto_approval', models.IntegerField()),
                ('cpi_max_claim_for_auto_approval', models.IntegerField()),
                ('approved_labor_rate', models.IntegerField()),
                ('max_loss_ratio_for_auto_approval', models.IntegerField()),
                ('is_part_of_agency', models.BooleanField(default=False)),
                ('producer_type', models.CharField(choices=[('franchise', 'Franchise'), ('independent', 'Independent'), ('bank', 'Bank'), ('credit union', 'Credit Union')], default=[('franchise', 'Franchise'), ('independent', 'Independent'), ('bank', 'Bank'), ('credit union', 'Credit Union')], max_length=50)),
                ('agent_code', models.CharField(max_length=120)),
                ('agent_name', models.CharField(max_length=120)),
                ('producer_start_date', models.DateField()),
                ('terminated', models.BooleanField(default=False)),
                ('sale_tax_on_part', models.BooleanField(default=False)),
                ('tax_on_parts', models.IntegerField()),
                ('sale_tax_on_labor', models.BooleanField(default=False)),
                ('tax_on_labor', models.IntegerField()),
                ('sale_tax_on_total', models.BooleanField(default=False)),
                ('tax_on_total', models.IntegerField()),
                ('part_number_used_for_claim_review', models.CharField(choices=[('oem', 'OEM'), ('after market', 'After Market')], default=[('oem', 'OEM'), ('after market', 'After Market')], max_length=50)),
                ('payment_method', models.CharField(choices=[('stripe', 'Stripe'), ('dwolla', 'Dwolla')], default=[('stripe', 'Stripe'), ('dwolla', 'Dwolla')], max_length=50)),
                ('stripe_customer_id', models.CharField(max_length=156)),
                ('automated_approval', models.BooleanField(default=False)),
                ('requires_customer_approval', models.BooleanField(default=False)),
                ('pay_by_card_only', models.BooleanField(default=False)),
                ('enable_lightspeed', models.BooleanField(default=False)),
                ('lightspeed_username', models.CharField(max_length=156)),
                ('lightspeed_password', models.CharField(max_length=128)),
                ('lightspeed_cmf', models.CharField(max_length=120)),
                ('has_service_department', models.BooleanField(default=False)),
                ('repair_order', models.BooleanField(default=False)),
                ('heading_1', models.CharField(max_length=120)),
                ('heading_2', models.CharField(max_length=120)),
                ('message', models.TextField()),
                ('dealer_note', models.TextField()),
                ('sale_representative', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.member')),
            ],
        ),
    ]
