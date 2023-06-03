from . import views
from django.urls import path

app_name = 'cwierkacz'

urlpatterns = [
    # path('', views.HelloView.as_view(), name='hello'),
    path('', views.home, name='index'),
    path('rejestracja', views.signup, name='rejestracja'),
    path('logowanie', views.signin, name='logowanie'),
    path('wylogowanie', views.signout, name='wylogowanie'),

]
