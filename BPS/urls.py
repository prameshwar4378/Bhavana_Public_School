"""BPS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import path
from BPSApp import views
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index,name="index"),
    path('enquiry_form/', views.enquiry_form, name="enquiry_form"), 

    # About Links
    path('alumni/', views.alumni,name="alumni"),
    path('principal_message/', views.principal_message,name="principal_message"),
    path('founder_message/', views.founder_message,name="founder_message"),
    path('school_info/', views.school_info,name="school_info"),
    path('vision_and_mission/', views.vision_and_mission,name="vision_and_mission"),
    path('school_location/', views.school_location,name="school_location"),
    path('phylosophy/', views.phylosophy,name="phylosophy"),
    path('risod_city/', views.risod_city,name="risod_city"),

    # General Informations Links
    path('teaching_staff/', views.teaching_staff,name="teaching_staff"),
    path('School Times/', views.school_times,name="school_times"),
    path('Important Days/', views.important_days,name="important_days"),
    path('Calender/', views.calender,name="calender"),
    path('Uniforms/', views.uniform,name="uniform"),
    path('Rules/', views.rules,name="rules"),
    path('Parent Meets/', views.parents_meet,name="parents_meet"),
    path('Parents Consent Form/', views.parents_consent_form,name="parents_consent_form"),

    # Admission Links
    path('age_criteria/', views.age_criteria,name="age_criteria"),
    path('guidlines/', views.guidlines,name="guidlines"),
    path('withdrawal/', views.withdrawal,name="withdrawal"),

    # Academics Links
    path('crriculum/', views.crriculum,name="crriculum"),
    path('co_crriculum/', views.co_crriculum,name="co-crriculum"),

    # Facilities Links
    path('infrastucture/', views.infrastructure,name="infrastructure"),
    path('hostel/', views.hostel,name="hostel"),
    path('library/', views.library,name="library"),
    path('computer_lab/', views.computer_lab,name="computer_lab"),
    path('smart_classes/', views.smart_classes,name="smart_classes"),
    path('news_papper/', views.news_papper,name="news_papper"),
    path('transportations/', views.transportation,name="transportations"),

    # Gallary Links
    path('photos/', views.photos,name="photos"),
    path('videos/', views.videos,name="videos"),

    #admin login links
    path('login/', views.admin_login, name="login"),
    path('logout/', views.admin_logout, name="logout"),
    path('admin_home/', views.admin_home, name="admin_home"),

    # Export Links
    path('export_enquiry/', views.export_excel_enquiries, name="export_enquiry"),

    # Other links
    path('enquiry_list/', views.enquiry_list, name="enquiry_list"),
    path('delete_enquiry/<int:id>/',views.delete_enquiry, name='delete_enquiry'),
    path('resolve_enquiry/<int:id>/',views.resolve_enquiry, name='resolve_enquiry'),

    path('career_form/',views.career_form, name='career_form'),
    path('career_list/',views.career_list, name='career_list'), 
    path('delete_career/<int:id>/',views.delete_career, name='delete_career'),

    path('alumni_form/',views.alumni_form, name='alumni_form'),
    path('alumni_list/',views.alumni_list, name='alumni_list'), 
    path('delete_alumni/<int:id>/',views.delete_alumni, name='delete_alumni'),

]
if settings.DEBUG:
    urlpatterns +=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
    