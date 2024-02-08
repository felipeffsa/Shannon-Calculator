from django.shortcuts import render
from django.http import HttpResponse
import math

# Create your views here.

def indice_calculator(request):
    return render(request,'interface/indice_calculator.html')

def digite_especies(request):
    numero = request.GET.get('numeros')
    numeros = [individual + 1 for individual in range(int(numero))]
    

    return render(request,'interface/digite_especies.html',context={'numeros':numeros})


def processamento(request):
    numeros = request.GET.getlist('resultados')
    # Laço entre os numeros das espécies de uma comunidade
    lista_numeros = [int(especie) for especie in numeros]
    #Sómatoria da lista dos resultados
    somatoria = sum(lista_numeros)
    #Proporção do Pi(frequência relativa) - Divisão de cada espécie pelo número da somatória. Obs: O Pi não é o pi de 3,14
    numeros_pi = [int(especie)/somatoria for especie in numeros]
    #Log de Pi(logaritimo natural) -- Falta arredondar os números
    logaritimo_pi = [round(math.log10(especie),2) for especie in numeros_pi]
    
    #Lista para somatoria de (Pi)xlog(Pi)
    somatoria_pixlogpi = []
    #Multiplicação de (Pi)xlog(Pi) -- Falta arredondar os números
    for numero_pi, log_pi in zip(numeros_pi,logaritimo_pi):
        somatoria_pixlogpi.append(round(numero_pi *log_pi,2))
    #Somatoria de (Pi)xlog(Pi) Lembrar de por o sinal de subtração (-)
    
    return HttpResponse( "H' " + str(-sum(somatoria_pixlogpi)))
    
    
    
    

def serve(request):
    return render(request,'interface/paraqueserve.html')

