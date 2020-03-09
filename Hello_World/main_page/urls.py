from django.urls import path
from . import views

app_name = 'main_page'
urlpatterns = [
    # /welcome/
    path('', views.HomePageView.as_view(), name='index'),
    path('crud/', views.PhpPageView.as_view(), name='crud'),

]
