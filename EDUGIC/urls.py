"""EDUGIC URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from . import views
#import settings allow the access of 
from django.conf import settings
#import static 
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/',views.index, name="home"),
    path('sign_in/',views.sign_in, name="sign_in"),
    #path('',views.sign_up, name="sign_up"),
    path('sign_up/',views.sign_up, name="sign_up"),
    path('users/',views.users,name="users"),
    path('add_question/',views.add_question, name="add_question"),
    path('add_job/',views.add_job, name="add_job"),
    path('job/',views.job, name="job"),
    path('add_packages/',views.add_packages, name='add_packages'),
    path('packages/', views.packages, name ='packages'),
    path('add_user/', views.add_user, name="add_user"),
    path('chat/', views.chat, name ='chat'),
    path('add_new_pdf/', views.add_new_pdf, name ='add_new_pdf'),
    path('video_tutorial/',views.video_tutorial, name="video_tutorial"),
    path('video_post/', views.video_post, name ='video_post'),
    path('file-images/', views.file_images, name ='file-images'),
    path('file-media/', views.file_media, name ='file-media'),
    path('mail-compose/', views.mail_compose, name ='mail-compose'),
    path('subjects/', views.subjects, name='subjects'),
    path('add_subject/',views.add_subject, name="add_subject"),
    path('mail-single/', views.mail_single, name='mail-single'),
    path('pdf_tutorial/', views.pdf_tutorial, name ='pdf_tutorial'),
    path('profile/', views.profile, name='profile'),
    path('addsub_toexam', views.addsub_toexam, name="addsub_toexam"),

    path('sub_topics/', views.sub_topics, name='sub_topics'),
    path('add_sub_topic/', views.add_sub_topic, name='add_sub_topic'),
    path('topics/', views.topics, name="topics"),
    path('add_topics/', views.add_topics, name="add_topics"),

    path('exam_center/', views.exam_center, name='exam_center'),
    path('add_center/', views.add_center, name='add_center'),

    path('result/', views.result, name='result'),
    path('file-dashboard/', views.file_dashboard, name ='file-dashboard'),
    path('file-documents/', views.file_documents, name ='file-documents'),
    path('questions/',views.qestions, name="questions"),

    path('exam',views.exam,name="exam"),
    path('add_exam/', views.add_exam, name="add_exam"),

    path('student/',views.student, name="student"),
    path('add_student/',views.add_student, name="add_student"),
    path('use_coupons/',views.used_coupons, name="used_coupons"),
    path('coupons/',views.coupons, name="coupons"),
    path('add_coupons/', views.add_coupons, name='add_coupons'),
    path('add_group/',views.add_group, name="add_group"),
    path('add_grouptable/',views.add_grouptable, name="add_grouptable"),



    # path('edit_package/',views.edit_package, name="edit_package"),

    #single  delete views url here....
    path('delete_packages/', views.delete_packages, name="delete_packages"),
    path('delete_job',views.delete_job, name="delete_job"),
    path('pdf_delete/',views.dpf_delete, name="pdf_delete"),
    path('delete_subject/',views.delete_subject, name='delete_subject'),
    path('delete_videotutorial/', views.delete_videotutorial, name='delete_videotutorial'),
    path('delete_subtopic/',views.delete_subtopic, name='delete_subtopic'),
    path('delete_questions/',views.detele_questions, name="delete_questions"),
    path('subject_chk_delete/',views.subject_chk_delete,name="subject_chk_delete"),
    path('delete_topics/',views.delete_topics,name="delete_topics"),
    path('delete_Excenter/',views.delete_Excenter, name="delete_Excenter"),
    path('del_exam/',views.delete_exam, name="delete_exam"),
    path('delete_coupons/',views.delete_coupons, name="delete_coupons"),
    path('delete_student/',views.detele_student, name="delete_student"),
    path('delete_user/', views.delete_user, name="delete_user"),
    path('delete_group/', views.delete_group, name="delete_group"),
    # path('edit_group/', views.edit_group, name="edit_group"),


    #urls for multiple delete recordes for.....
    path('multi_del_group',views.multiple_delete_group, name = "multiple_delete_group"),
    path('multi_del_sub/', views.multiple_delete_subject, name='multiple_delete_subject'),
    path('multi_del_packages/',views.multiple_delete_packages, name="multiple_delete_packages"),
    path('multi_del_video/', views.multiple_delete_video,name="multiple_delete_video"),
    path('multi_del_pdftuto/',views.multiple_delete_pdftutorial, name="multiple_delete_pdftutorial"),
    path('multi_del_topics/', views.multiple_delete_topics,name="multiple_delete_topics"),
    path('multi_del_subtopic/',views.multiple_delete_subtopic, name="multiple_delete_subtopic"),
    path('multi_del_question/',views.multiple_delete_question, name="multiple_delete_question"),
    path('multi_del_examcenter/', views.multiple_delete_examcenter, name="multiple_delete_examcenter"),
    path('multi_del_users/', views.multiple_delete_users, name="multiple_delete_users"),
    path('multi_del_sub/',views.multiple_delete_exam, name="multiple_delete_exam"),
    path('multi_del_coupons/',views.multiple_delete_coupons, name="multiple_delete_coupons"),
    path('multi_del_student/', views.multiple_delete_student, name="multiple_delete_student"),
    path('multi_del_job/', views.multiple_delete_job, name="multiple_delete_job"),



#All update or edit
    path('edit_student/', views.edit_student, name="edit_student"),
    path('update_student/',views.update_student, name="update_student"),
    path('edit_center/',views.edit_center, name="edit_center"),
    path('update_center/',views.update_center, name="update_center"),
    path('edit_coupons/',views.edit_coupons, name="edit_coupons"),
    path('update_coupons/',views.update_coupons, name="update_coupons"),
    path('edit_exam/',views.edit_exam, name="edit_exam"),
    path('update_exam/',views.update_exam, name="update_exam"),
    path('edit_group/', views.edit_group, name="edit_group"),
    path('update_group/', views.update_group, name="update_group"),
    path('edit_job/', views.edit_job, name="edit_job"),
    path('update_job/', views.update_job, name="update_job"),
    path('edit_packages/', views.edit_packages, name="edit_packages"),
    path('update_packages/', views.update_packages, name="update_packages"),
    path('edit_question/', views.edit_question, name="edit_question"),
    path('update_question/', views.update_question, name="update_question"),
    path('edit_subject/', views.edit_subject, name="edit_subject"),
    path('update_subject/', views.update_subject, name="update_subject"),
    path('edit_sub_topics/', views.edit_sub_topics, name="edit_sub_topics"),
    path('update_sub_topics/', views.update_sub_topics, name="update_sub_topics"),
    path('edit_topics/', views.edit_topics, name="edit_topics"),
    path('update_topics/', views.update_topics, name="update_topics"),
    path('edit_user/', views.edit_user, name="edit_user"),
    path('update_user/', views.update_user, name="update_user"),
    path('edit_videotutorial/',views.edit_videotutorial, name="edit_videotutorial"),
    path('update_videotutorial/',views.update_videotutorial, name="update_videotutorial"),
    path('edit_pdf',views.edit_pdf, name="edit_pdf"),
    path('update_pdf',views.update_pdf, name="update_pdf"),
    path('edit_exam', views.edit_exam, name="edit_exam"),
    path('update_exam', views.update_exam, name="update_exam"),

#view

    path('user_view', views.user_view, name="user_view"),
    path('view_package', views.view_package, name="view_package"),
    path('view_subject', views.view_subject, name="view_subject"),
    path('view_video', views.view_video, name="view_video"),
    path('view_pdf', views.view_pdf, name="view_pdf"),
    path('view_sub_topic', views.view_sub_topic, name="view_sub_topic"),
    path('view_question', views.view_question, name="view_question"),
    path('view_center', views.view_center, name="view_center"),
    path('view_topic', views.view_topic, name="view_topic"),
    path('view_student', views.view_student, name="view_student"),
    path('view_group', views.view_group, name="view_group"),
    path('view_job', views.view_job, name="view_job"),
    path('view_coupons', views.view_coupons, name="view_coupons"),
    path('view_exam', views.view_exam, name="view_exam"),
    path('job_details', views.job_details, name="job_details"),




]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #to provide the linking of static files and media files in the project

