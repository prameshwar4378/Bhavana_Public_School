# Generated by Django 4.1.1 on 2022-10-12 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BPSApp', '0009_remove_db_alumni_bussiness_photo_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='db_alumni',
            name='bussiness_photo',
            field=models.ImageField(blank=True, null=True, upload_to='alumni_application'),
        ),
        migrations.AddField(
            model_name='db_alumni',
            name='company_or_bussiness_name',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='db_alumni',
            name='full_name',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='db_alumni',
            name='gender',
            field=models.CharField(choices=[('MALE', 'MALE'), ('FEMALE', 'FEMALE')], max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='db_alumni',
            name='last_standerd_in_bps',
            field=models.CharField(choices=[('JR.KG', 'JR.KG'), ('1st Standerd', '1st Standerd'), ('2nd Standerd', '2nd Standerd'), ('3rd Standerd', '3rd Standerd'), ('4th Standerd', '4th Standerd'), ('5th Standerd', '5th Standerd'), ('6th Standerd', '6th Standerd'), ('7th Standerd', '7th Standerd'), ('8th Standerd', '8th Standerd'), ('9th Standerd', '9th Standerd'), ('10th Standerd', '10th Standerd'), ('11th Standerd', '11th Standerd'), ('12th Standerd', '12th Standerd')], max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='db_alumni',
            name='last_year_in_bps',
            field=models.CharField(choices=[('2000', '2000'), ('2001', '2001'), ('2002', '2002'), ('2003', '2003'), ('2004', '2004'), ('2005', '2005'), ('2006', '2006'), ('2007', '2007'), ('2008', '2008'), ('2009', '2009'), ('2011', '2011'), ('2012', '2012'), ('2013', '2013'), ('2014', '2014'), ('2015', '2015'), ('2016', '2016'), ('2017', '2017'), ('2018', '2018'), ('2019', '2019'), ('2020', '2020'), ('2021', '2021'), ('2022', '2022')], max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='db_alumni',
            name='mobile',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='db_alumni',
            name='present_role',
            field=models.CharField(choices=[('EMPLOYEE', 'EMPLOYEE'), ('OWNNER', 'OWNNER')], max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='db_alumni',
            name='profile_photo',
            field=models.ImageField(blank=True, null=True, upload_to='alumni_application'),
        ),
        migrations.AddField(
            model_name='db_alumni',
            name='sallary_or_turnover_LPA',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
