from django.urls import path
from . import views

appapp_name = 'posty'

urlpatterns = [
    path('posty', views.list_of_post, name='posty'),
    path('posty/<slug:slug>', views.post_detail, name='post_detail'),
]