from django.urls import path
from . import views

urlpatterns = [
    path('', views.cliente),
    path('Empresa/<str:nameEmpresa>/', views.viewEmpresa, name='empresa'),
    path('nosotros/', views.nostros, name = 'Sobre nosotros')
]