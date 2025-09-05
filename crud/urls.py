from django.urls import path
from . import views 

#archivo para las urls de la app crud
app_nombre = 'crud'

#definicion de las urls
urlpatterns = [path('',views.task_list_and_create, name='crud_list')]