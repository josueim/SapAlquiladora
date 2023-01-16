from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from .models import GestionMobiliaria, Personal, MenusComida

# Login function.
def signin(request):
    if request.method == 'GET':
        return render(request, 'home.html', {
            'form': AuthenticationForm
        })
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'home.html', {
                'form': AuthenticationForm,
                'error': 'El usuario o la contraseña son incorrectos'
            })
        else:
            login(request, user)
            return redirect('menu')


#Register function
def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html', {
            'form': UserCreationForm
        })
    else:
        #validates that the password is the same in both fields
        if request.POST['password1'] == request.POST['password2']:
            try:
                #register user
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('menu')
            except IntegrityError:
                return render(request, 'signup.html', {
                    'form': UserCreationForm,
                    'error': 'El usuario ya existe'
                })
        return render(request, 'signup.html', {
                    'form': UserCreationForm,
                    'error': 'Las contraseñas no coinciden'
                })


# logout the session
def signout(request):
    logout(request)
    return redirect('signin')


def menu(request):
    return render(request, 'menu.html')


def mobiliario(request):
    mobiliario = GestionMobiliaria.objects.all()

    return render(request, 'Mobiliario/mobiliario.html', {
        'mobiliario' : mobiliario,
    })


def mobiliario_p(request):
    context = {}
    #table gestion mobiliaria inside a list
    mobiliario = GestionMobiliaria.objects.all()
    #getting inputs inside a list
    mobiliario_calcular = request.POST.getlist('calcular[]')
    
    for i in range(len(mobiliario_calcular)):
        if mobiliario_calcular[i] == "":
            mobiliario_calcular[i] = 0

    multiplicacion = zip(mobiliario, mobiliario_calcular)
    subtotal = []
    for i,j in multiplicacion:
        subtotal.append(i.precio_renta * int(j))    

    my_list = zip(mobiliario, mobiliario_calcular, subtotal)
    context = {
        'my_list' : my_list
    }

    return render(request, 'Mobiliario/mobiliario_p.html', context)


def personal(request):
    personal = Personal.objects.all()
    
    return render(request, 'Personal/personal.html', {
        'personal': personal
    })


def personal_p(request):
    context = {}
    #table personal inside a list
    personal = Personal.objects.all()
    #getting inputs inside a list
    calcular_personal = request.POST.getlist('calcular_personal[]')
    
    for i in range(len(calcular_personal)):
        if calcular_personal[i] == "":
            calcular_personal[i] = 0

    multiplicacion = zip(personal, calcular_personal)
    subtotal = []
    for i,j in multiplicacion:
        subtotal.append(i.precio_evento * int(j))    

    my_list = zip(personal, calcular_personal, subtotal)
    context = {
        'my_list' : my_list
    }

    return render(request, 'Personal/personal_p.html', context)


def platillos(request):
    platillos = MenusComida.objects.all()
    
    return render(request, 'Platillos/platillos.html', {
        'platillos': platillos
    })


def platillos_p(request):
    context = {}
    #table platillos inside a list
    platillos = MenusComida.objects.all()
    #getting inputs inside a list
    calcular_platillos = request.POST.getlist('calcular_platillos[]')
    
    for i in range(len(calcular_platillos)):
        if calcular_platillos[i] == "":
            calcular_platillos[i] = 0

    multiplicacion = zip(platillos, calcular_platillos)
    subtotal = []
    for i,j in multiplicacion:
        subtotal.append(i.precio_persona * int(j))    

    my_list = zip(platillos, calcular_platillos, subtotal)
    context = {
        'my_list' : my_list
    }

    return render(request, 'Platillos/platillos_p.html', context)


def presupuesto(request):
    #mobiliario
    mobiliario_elegido = request.POST.getlist('mobiliario_elegido[]')
    subtotal_mobiliario = request.POST.getlist('subtotal_mobiliario[]')

    #personal
    personal_elegido = request.POST.getlist('personal_elegido[]')
    subtotal_personal = request.POST.getlist('subtotal_personal[]')

    #platillos
    platillos_elegido = request.POST.getlist('platillos_elegido[]')
    subtotal_platillos = request.POST.getlist('subtotal_platillos[]')

    print(platillos_elegido)
    print(subtotal_platillos)

    return render(request, 'Presupuesto/presupuesto.html')
