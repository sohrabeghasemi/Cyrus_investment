from django.urls import path
from . import views

app_name = 'web'


urlpatterns = [
	path('', views.index, name='index'),
	path('web/', views.web, name='web'),
	path('web/<int:kargar_id>', views.kargar_detail, name='kargar_detail'),
	path('web/plist/', views.project_list, name='p_list'),
	path('web/kargar_input/', views.kargar_input_form, name='kargar_input_form')
]