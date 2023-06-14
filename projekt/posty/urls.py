from django.urls import path
from . import views
from .views import PostCreateView

appapp_name = 'posty'

urlpatterns = [
    path('posty', views.list_of_post, name='posty'),
    path('posty/create', PostCreateView.as_view(), name='post_create'),
    path('wyszukaj/', views.BlogSearchView.as_view(), name='wyszukaj'),
    path('posty/<slug:slug>', views.post_detail, name='post_detail'),
]