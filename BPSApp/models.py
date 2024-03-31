from datetime import datetime
import email
from random import choices
from django.db import models
from django.forms import DateField
# Create your models here.

ENQUIRY_SOLVED_OR_NOT=(
    ('YES','YES'),
    ('NO','NO'),
    ('NOT SURE','NOT SURE'),
)

GENDER=(
    ('MALE','MALE'),
    ('FEMALE','FEMALE'),
)

ROLE=(
    ('EMPLOYEE','EMPLOYEE'),
    ('OWNNER','OWNNER'),
)
STANDERDS=(
    ('JR.KG','JR.KG'),
    ('1st Standerd','1st Standerd'),
    ('2nd Standerd','2nd Standerd'),
    ('3rd Standerd','3rd Standerd'),
    ('4th Standerd','4th Standerd'),
    ('5th Standerd','5th Standerd'),
    ('6th Standerd','6th Standerd'),
    ('7th Standerd','7th Standerd'),
    ('8th Standerd','8th Standerd'),
    ('9th Standerd','9th Standerd'),
    ('10th Standerd','10th Standerd'),
    ('11th Standerd','11th Standerd'),
    ('12th Standerd','12th Standerd'),
)


YEAR=(
    ('2000','2000'),
    ('2001','2001'),
    ('2002','2002'),
    ('2003','2003'),
    ('2004','2004'),
    ('2005','2005'),
    ('2006','2006'),
    ('2007','2007'),
    ('2008','2008'),
    ('2009','2009'),
    ('2011','2011'),
    ('2012','2012'),
    ('2013','2013'),
    ('2014','2014'),
    ('2015','2015'),
    ('2016','2016'),
    ('2017','2017'),
    ('2018','2018'),
    ('2019','2019'),
    ('2020','2020'),
    ('2021','2021'),
    ('2022','2022'),
)


# class DB_Enqueries(models.Model):
#     pass
    # full_name=models.CharField(max_length=100)
    # email=models.EmailField(max_length=254)
    # mobile=models.BigIntegerField()
    # subject=models.CharField(max_length=500)
    # message=models.TextField()
    # enquiry_date=models.DateTimeField(auto_now=False, auto_now_add=False)

    # solved_or_not=models.CharField(max_length=100, null=True, blank=True, choices=ENQUIRY_SOLVED_OR_NOT)
    # solution_description=models.TextField(null=True, blank=True)
    # solution_date=models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True)
    
class DB_Enqueries(models.Model):
    full_name=models.CharField(max_length=100, null=True)
    email=models.EmailField(max_length=254, null=True)
    mobile=models.CharField( max_length=250, null=True)
    subject=models.CharField(max_length=500, null=True)
    message=models.TextField(null=True)
    enquiry_date=models.DateTimeField(auto_now=True, auto_now_add=False,null=True, blank=True )

    solved_or_not=models.CharField(max_length=100, null=True, blank=True, choices=ENQUIRY_SOLVED_OR_NOT)
    solution_description=models.TextField(null=True, blank=True)
    solution_date=models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True)
    
   
class DB_Career(models.Model):
    full_name=models.CharField(max_length=255,null=True)
    email=models.EmailField(max_length=254,null=True)
    mobile=models.CharField( max_length=250,null=True)
    resume=models.FileField( upload_to="Resume", max_length=100,null=True)
    date=models.DateTimeField(auto_now=True, auto_now_add=False, editable=True)

class DB_Alumni(models.Model):
    full_name=models.CharField(max_length=250, null=True)
    mobile=models.CharField(max_length=250, null=True)
    gender=models.CharField(max_length=50,choices=GENDER, null=True)
    passing_standerd=models.CharField( max_length=100,choices=STANDERDS, null=True)
    passing_year=models.CharField( max_length=100,choices=YEAR, null=True)
    present_role=models.CharField( max_length=100,choices=ROLE, null=True)
    company_or_bussiness_name=models.CharField(max_length=500,null=True)
    sallary_or_turnover_LPA=models.IntegerField(null=True, blank=True)
    profile_photo=models.ImageField(upload_to="alumni_application", height_field=None, width_field=None, max_length=None,null=True, blank=True)
    bussiness_photo=models.ImageField(upload_to="alumni_application", height_field=None, width_field=None, max_length=None,null=True, blank=True)