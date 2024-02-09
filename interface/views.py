from django.shortcuts import render
from django.http import HttpResponse
import math
from interface.models import Dados, Pi, LogPi, MultLogPi

# Create your views here.

def indice_calculator(request):
    return render(request,'interface/indice_calculator.html')

def digite_especies(request):
    numero = request.GET.get('numeros')
    numeros = [individual + 1 for individual in range(int(numero))]
    

    return render(request,'interface/digite_especies.html',context={'numeros':numeros})


def processamento(request):
    numeros = request.GET.getlist('resultados')
    dados = Dados(
        usuario = request.user
    )
    dados.save()
    # Laço entre os numeros das espécies de uma comunidade
    lista_numeros = [int(especie) for especie in numeros]
    #Sómatoria da lista dos resultados
    somatoria = sum(lista_numeros)
    
    #Proporção do Pi(frequência relativa) - Divisão de cada espécie pelo número da somatória. Obs: O Pi não é o pi de 3,14
    numeros_pi = [int(especie)/somatoria for especie in numeros]
    #Adicionando o Pi no banco de dados
    for numero in numeros_pi:
        pi = Pi.objects.create(
        usuario = request.user,
        numero_pi = numero
    )
        dados.pi.add(pi)
        dados.save()
    #-------------------------------------------------------------------------------------------
    #Log de Pi(logaritimo natural) 
    logaritimo_pi = [math.log(especie,2.71) for especie in numeros_pi]
    
    for numero in logaritimo_pi:
        log_pi = LogPi.objects.create(
            usuario = request.user,
            numero_pi = numero
        )
        dados.logpi.add(log_pi)
        dados.save()
    
    #-------------------------------------------------------------------------------------------
    
    
    #Lista para somatoria de (Pi)xlog(Pi)
    somatoria_pixlogpi = []
    #Multiplicação de (Pi)xlog(Pi) 
    for numero_pi, log_pi in zip(numeros_pi,logaritimo_pi):
        somatoria_pixlogpi.append(numero_pi *log_pi)
        
    for numero in somatoria_pixlogpi:
        mult_log = MultLogPi.objects.create(
            usuario = request.user,
            numero_pi = numero
        )
        dados.multipi.add(mult_log)
        dados.save()
    #-------------------------------------------------------------------------------------------
   
    #Somatoria de (Pi)xlog(Pi) Lembrar de por o sinal de subtração (-)
    somatoria_resultado = (-sum(somatoria_pixlogpi))
    dados.resultado = somatoria_resultado
    dados.save()
    

    
    return HttpResponse('Teste')
    
def detalhes(request):
    comunidades = Dados.objects.filter(usuario = request.user)
    numeros = request.GET.get('numeros')
    dados = Dados.objects.filter(id = numeros)
    return render(request,'interface/detalhes.html',context={'comunidades':comunidades,'dados':dados})
    
    

def serve(request):
    return render(request,'interface/paraqueserve.html')

