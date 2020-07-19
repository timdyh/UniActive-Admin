from django.urls import path, re_path
from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('show_reviewedActivities/', views.show_reviewedActivities, name='show_reviewedActivities'),
    path('show_passedActivities/', views.show_passedActivities, name='show_passedActivities'),
    path('show_denyedActivities/', views.show_denyedActivities, name='show_denyedActivities'),
    path('show_users/', views.show_users, name='show_users'),
    path('pass_activity/', views.pass_activity, name='pass_activity'),
    path('deny_activity/', views.deny_activity, name='deny_activity'),
    path('change_user_status/', views.change_user_status, name='change_user_status'),
    path('upload_file/', views.upload_file, name='upload_file'),
    path('download_file/', views.download_file, name='download_file'),
    path('minidouyin_post_video/', views.minidouyin_post_video, name='minidouyin_post_video'),
    path('minidouyin_get_feed/', views.minidouyin_get_feed, name='minidouyin_get_feed'),
    path('minidouyin_get_file/', views.minidouyin_get_file, name='minidouyin_get_file'),
    path('post_picture/', views.post_picture, name='post_picture'),
    path('get_picture/', views.get_picture, name='get_picture'),
    path('get_feedback/', views.get_feedback, name='get_feedback'),
    # path('get_actDetail/', views.get_actDetail, name='get_actDetail'),
    # path('get_actDiscuss/', views.get_actDiscuss, name='get_actDiscuss'),
    path('discuss/', views.discuss, name='discuss'),
    path('delete_discuss/', views.delete_discuss, name='delete_discuss'),
    path('download/', views.download, name='download'),
    path('check_new/', views.check_new, name='check_new'),
    path('changepsw/', views.changepsw, name='changepsw'),
]
