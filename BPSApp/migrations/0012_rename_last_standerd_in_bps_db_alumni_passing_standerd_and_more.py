# Generated by Django 4.1.1 on 2022-10-12 13:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BPSApp', '0011_db_enqueries_email_db_enqueries_enquiry_date_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='db_alumni',
            old_name='last_standerd_in_bps',
            new_name='passing_standerd',
        ),
        migrations.RenameField(
            model_name='db_alumni',
            old_name='last_year_in_bps',
            new_name='passing_year',
        ),
    ]