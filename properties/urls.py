from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.property_list, name='property_list'),
    re_path(r'^property/(?P<slug>[-\w\u0600-\u06FF]+)/$', views.property_detail, name='property_detail'),
    path('about_us/', views.about_us, name='about_us'),
    ]