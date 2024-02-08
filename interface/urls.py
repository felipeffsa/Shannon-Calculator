from django.urls import path
from interface import views

urlpatterns = [
    path('',views.indice_calculator, name ='indice_calculator'),
    path('digite/',views.digite_especies, name ='digite'),
    path('processamento',views.processamento, name ='processamento'),
    path('paraqueserve/',views.serve, name ='serve'),
]
