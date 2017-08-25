from django.conf.urls import include, url
from . import views

urlpatterns = [
url(r'^$', views.post_list),
url(r'^register/', views.registrar, name='registrar'), 
url(r'^login/', views.logear, name='logear'), 
url(r'^postear/', views.postear, name='postear'), 
url(r'^calendario/', views.calendario),
]