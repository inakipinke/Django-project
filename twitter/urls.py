from django.conf.urls import include, url
from . import views

urlpatterns = [
url(r'^$', views.post_list),url(r'^register/', views.registrar), url(r'^postear/', views.postear), url(r'^calendario/', views.calendario),
]