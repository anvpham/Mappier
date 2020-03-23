from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    # Home page.
    path('', views.home, name='home'),
    path('search/<str:category>', views.search, name='search'),
]
