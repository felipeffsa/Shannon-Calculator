from django.urls import path
from interface import views

urlpatterns = [
    path('',views.indice_calculator, name ='indice_calculator'),
    path('digite/',views.digite_especies, name ='digite'),
    path('processamento',views.processamento, name ='processamento'),
    path('paraqueserve/',views.serve, name ='serve'),
    path('detalhes/',views.detalhes, name ='detalhes'),
    path('comparacao_comunidades_processamento/', views.comparacao_comunidades_processamento, name ='comparacao_comunidades_processamento'),
    path('comparar_comunidades/', views.comparacao_comunidades, name='comparar_comunidades')
]
