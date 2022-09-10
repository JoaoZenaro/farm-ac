from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.calendario_form,name='calendario_insert'),
    path('<int:id>/', views.calendario_form,name='calendario_update'),
    path('delete/<int:id>/',views.calendario_delete,name='calendario_delete'),
    path('list/',views.calendario_list,name='calendario_list')
]