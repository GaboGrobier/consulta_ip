from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
import requests
from . import forms

# Create your views here.

def home(request):
    form = forms.ingresoIp
    return render (request, 'index.html',{'form':form})

def consultar(request):
    if request.method =='POST':
        ip = request.POST['ip']
        url = f'http://ipwho.is/{ip}'
        response = requests.get(url)
        data_response = response.json()
        country = data_response['country']
        region = data_response['region']
        flag = data_response['flag']['img']
        isp = data_response['connection']['isp']
        return render(request, 'resultado.html', {'bandera': flag, 'reg': region, 'ciudad': country, 'i': ip, 'prove':isp})

def informacion_json(request):
    if request.method == 'POST':
        ip = request.POST['ip']
        url = f'http://ipwho.is/{ip}'
        response = requests.get(url)
        data_response = response.json()
        return JsonResponse(data_response)
    
def ip_api(request, numip):
    url = f'http://ipwho.is/{numip}'
    response = requests.get(url)
    data_response = response.json()
    return JsonResponse(data_response)

    
    
