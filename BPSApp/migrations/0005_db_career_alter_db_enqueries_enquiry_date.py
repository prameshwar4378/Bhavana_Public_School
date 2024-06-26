# Generated by Django 4.1.1 on 2022-10-12 01:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BPSApp', '0004_remove_db_enqueries_adress_remove_db_enqueries_date_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='DB_Career',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('mobile', models.BigIntegerField()),
                ('resume', models.FileField(upload_to='Resume')),
            ],
        ),
        migrations.AlterField(
            model_name='db_enqueries',
            name='enquiry_date',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
