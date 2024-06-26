# Generated by Django 4.1.1 on 2022-10-11 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BPSApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DB_Enquiry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=200)),
                ('mobile', models.BigIntegerField()),
                ('adress', models.TextField()),
                ('message', models.TextField()),
                ('date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='db_enqueries',
            name='email',
        ),
        migrations.RemoveField(
            model_name='db_enqueries',
            name='enquiry_date',
        ),
        migrations.RemoveField(
            model_name='db_enqueries',
            name='full_name',
        ),
        migrations.RemoveField(
            model_name='db_enqueries',
            name='message',
        ),
        migrations.RemoveField(
            model_name='db_enqueries',
            name='mobile',
        ),
        migrations.RemoveField(
            model_name='db_enqueries',
            name='solution_date',
        ),
        migrations.RemoveField(
            model_name='db_enqueries',
            name='solution_description',
        ),
        migrations.RemoveField(
            model_name='db_enqueries',
            name='solved_or_not',
        ),
        migrations.RemoveField(
            model_name='db_enqueries',
            name='subject',
        ),
    ]
