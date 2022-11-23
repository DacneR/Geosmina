from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.http import HttpResponse

# Create your views here.

def Index(request):
    
    if request.method == 'GET':
        return render(request, 'index.html',{
        'form': UserCreationForm
    })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                #register user
                Usuario = User.objects.create_user(username=request.POST['username'],
                password=request.POST['password1'])
                #Save user
                Usuario.save()
                login(request, Usuario)
                return redirect('iniciar')
            except:
                return render(request, 'index.html',{
                    'form': UserCreationForm,
                    'error': 'Usuario ya existe'
                })
        return render(request, 'index.html',{
            'form': UserCreationForm,
            'error': 'Usuario ya existe'
        }) 



def acerca(request):
    return render(request, 'acerca.html')

    

def iniciar(request):
    return render(request, 'iniciar.html')

def productos(request):
    return render(request, 'productos.html')

def sigin(request):
    if request.method == "GET":
        return render(request, 'sigin.html',{
            'form': AuthenticationForm
        })
    else: 
        Usuario = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])

        if Usuario is None:
            return render(request, 'sigin.html',{
                'form': AuthenticationForm,
                'error': 'Usuario o contraseña incorrecta'
            })
        else:
            login(request, Usuario)
            return redirect('iniciar')

        

        
        
