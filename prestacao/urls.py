from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.lancamento_form,name='lancamento_insert'),
    path('<int:id>/', views.lancamento_form,name='lancamento_update'),
    path('delete/<int:id>/',views.lancamento_delete,name='lancamento_delete'),
    path('list/',views.lancamento_list,name='lancamento_list')
]