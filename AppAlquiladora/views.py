from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from .models import GestionMobiliaria, Personal, MenusComida, Clientes

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


lista_mobiliario = []
id_mobiliarios = []
mobiliarios = []
subtotales_m = []

lista_personal = []
id_personal = []
personals = []
subtotales_p = []

lista_platillo = []
id_platillo = []
platilloss = []
subtotales_pl = []


def presupuesto(request):
    context = {}
    #data base tables into lists
    mobiliario = GestionMobiliaria.objects.all()
    personal = Personal.objects.all()
    platillos = MenusComida.objects.all()


    #mobiliario
    mobiliario_elegido = request.POST.getlist('mobiliario_elegido[]')
    subtotal_mobiliario = request.POST.getlist('subtotal_mobiliario[]')

    mobiliario_post = zip(mobiliario_elegido, subtotal_mobiliario)

    #lists mobiliario, id, elegidos, subrtotales without zeros
    counter_mobiliario = 1
    for i,j in mobiliario_post:
        if j != '0':
            id_mobiliarios.append(counter_mobiliario)
            mobiliarios.append(i)
            subtotales_m.append(j)
            counter_mobiliario += 1
        else:
            counter_mobiliario += 1

    for i in mobiliario:
        if i.id_gestionm in id_mobiliarios:
            lista_mobiliario.append(i)

    mobiliario_zip = zip(lista_mobiliario, id_mobiliarios, mobiliarios, subtotales_m)
    

    #personal
    personal_elegido = request.POST.getlist('personal_elegido[]')
    subtotal_personal = request.POST.getlist('subtotal_personal[]')

    personal_post = zip(personal_elegido, subtotal_personal)

    #lists personal, id, elegidos, subrtotales without zeros
    
    counter_personal = 1
    for i,j in personal_post:
        if j != '0':
            id_personal.append(counter_personal)
            personals.append(i)
            subtotales_p.append(j)
            counter_personal += 1
        else:
            counter_personal += 1

    for i in personal:
        if i.id_personal in id_personal:
            lista_personal.append(i)

    personal_zip = zip(lista_personal, id_personal, personals, subtotales_p)


    #platillos
    platillos_elegido = request.POST.getlist('platillos_elegido[]')
    subtotal_platillos = request.POST.getlist('subtotal_platillos[]')

    platillos_post = zip(platillos_elegido, subtotal_platillos)

    #lists platillos, id, elegidos, subrtotales without zeros
    counter_platillo = 1
    for i,j in platillos_post:
        if j != '0':
            id_platillo.append(counter_platillo)
            platilloss.append(i)
            subtotales_pl.append(j)
            counter_platillo += 1
        else:
            counter_platillo += 1

    for i in platillos:
        if i.id_menusc in id_platillo:
            lista_platillo.append(i)

    platillo_zip = zip(lista_platillo, id_platillo, platilloss, subtotales_pl)

    context = {
        'mobiliario_zip': mobiliario_zip,
        'personal_zip': personal_zip,
        'platillo_zip': platillo_zip
    }

    return render(request, 'Presupuesto/presupuesto.html', context)


def presupuesto_p(request):
    context = {}

    global lista_mobiliario, id_mobiliarios, mobiliarios, subtotales_m
    global lista_personal, id_personal, personals, subtotales_p
    global lista_platillo, id_platillo, platilloss, subtotales_pl

    mobiliario_zip = zip(lista_mobiliario, id_mobiliarios, mobiliarios, subtotales_m)
    personal_zip = zip(lista_personal, id_personal, personals, subtotales_p)
    platillo_zip = zip(lista_platillo, id_platillo, platilloss, subtotales_pl)

    nombre_cliente = request.POST.get("nombre_cliente")
    descuento_presupuesto = int(request.POST.get("p_descuento"))

    for i in range(len(subtotales_m)):
        subtotales_m[i] = int(subtotales_m[i])

    for i in range(len(subtotales_p)):
        subtotales_p[i] = int(subtotales_p[i])

    for i in range(len(subtotales_pl)):
        subtotales_pl[i] = int(subtotales_pl[i])

    descuento_porcentaje = ((descuento_presupuesto * ((sum(subtotales_m) + sum(subtotales_p) + sum(subtotales_pl))))/100)
    total = (sum(subtotales_m) + sum(subtotales_p) + sum(subtotales_pl)) - descuento_porcentaje

    context = {
        'mobiliario_zip': mobiliario_zip,
        'personal_zip': personal_zip,
        'platillo_zip': platillo_zip,
        'nombre_cliente': nombre_cliente,
        'descuento_presupuesto': descuento_presupuesto,
        'total': total
    }

    lista_vacia = []

    if 'Terminar' in request.POST:

        lista_mobiliario = lista_vacia
        id_mobiliarios = lista_vacia
        mobiliarios = lista_vacia
        subtotales_m = lista_vacia

        lista_personal = lista_vacia
        id_personal = lista_vacia
        personals = lista_vacia
        subtotales_p = lista_vacia

        lista_platillo = lista_vacia
        id_platillo = lista_vacia
        platilloss = lista_vacia
        subtotales_pl = lista_vacia

        nombre_cliente = 0
        descuento_presupuesto = 0


    return render(request, 'Presupuesto/presupuesto_p.html', context)


def vista_platillos(request):
    return render(request, 'vista_platillos.html')