from django.conf.urls import url
from registration import views

urlpatterns = [
        url(r'^register/$',views.register,name='register'), # New pattern!
        url(r'^login/$', views.user_login, name='login'),
        url(r'^logout/$', views.user_logout, name='logout'),
        url(r'^restricted/', views.restricted, name='restricted'),        
]
