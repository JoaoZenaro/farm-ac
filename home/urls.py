from django.urls import path
from . import views
from .views import line_chart, line_chart_json

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name = "home"),
    path("signup/", views.signup_form, name="signup"),
    path('lancamentos_text', views.lancamentos_text, name='lancamentos_text'),
    path('chart', line_chart, name='line_chart'),
    path('chartJSON', line_chart_json, name='line_chart_json'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)