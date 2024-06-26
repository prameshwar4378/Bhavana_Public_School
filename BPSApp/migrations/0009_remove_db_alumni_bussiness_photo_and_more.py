# Generated by Django 4.1.1 on 2022-10-12 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BPSApp', '0008_alter_db_alumni_bussiness_photo_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='db_alumni',
            name='bussiness_photo',
        ),
        migrations.RemoveField(
            model_name='db_alumni',
            name='company_or_bussiness_name',
        ),
        migrations.RemoveField(
            model_name='db_alumni',
            name='full_name',
        ),
        migrations.RemoveField(
            model_name='db_alumni',
            name='gender',
        ),
        migrations.RemoveField(
            model_name='db_alumni',
            name='last_standerd_in_bps',
        ),
        migrations.RemoveField(
            model_name='db_alumni',
            name='last_year_in_bps',
        ),
        migrations.RemoveField(
            model_name='db_alumni',
            name='present_role',
        ),
        migrations.RemoveField(
            model_name='db_alumni',
            name='profile_photo',
        ),
        migrations.RemoveField(
            model_name='db_alumni',
            name='sallary_or_turnover_LPA',
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
        migrations.AlterField(
            model_name='db_career',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='db_career',
            name='full_name',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='db_career',
            name='mobile',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='db_career',
            name='resume',
            field=models.FileField(null=True, upload_to='Resume'),
        ),
    ]
