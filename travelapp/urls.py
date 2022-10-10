from django.urls import path
from . import views
urlpatterns = [
    path('',views.first_load,name='first_load'),
    path('add',views.add,name = 'addition')
]