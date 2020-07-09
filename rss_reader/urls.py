from django.urls import path

from . import views

app_name = 'rss_reader'
urlpatterns = [
    path('', views.index, name='index'),
    path('show/', views.show, name='show')
]