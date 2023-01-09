from django.db import models

# Create your models here.
class Vehiculos(models.Model):
    id_vehiculos = models.SmallAutoField(primary_key=True)
    descripcion = models.CharField(max_length=80)
    marca = models.CharField(max_length=80)
    estatus = models.BooleanField()
    combustible = models.SmallIntegerField()

    def __str__(self):
        return self.descripcion + (', ') + self.marca


class PersonalVehiculos(models.Model):
    id_personalv = models.SmallAutoField(primary_key=True)
    nombre_puesto = models.CharField(max_length=80)
    nombre = models.CharField(max_length=80)
    edad = models.SmallIntegerField()
    estatus = models.BooleanField()

    def __str__(self):
        return self.nombre


class GestionMobiliaria(models.Model):
    id_gestionm = models.SmallAutoField(primary_key=True)
    producto = models.CharField(max_length=80)
    reposicion = models.SmallIntegerField()
    precio_renta = models.SmallIntegerField()
    cantidad = models.SmallIntegerField()
    #cantidad_elegida = models.SmallIntegerField()
    #total = models.IntegerField()

    def __str__(self):
        return self.producto


class Personal(models.Model):
    id_personal = models.SmallAutoField(primary_key=True)
    descripcion = models.CharField(max_length=80)
    precio_evento = models.SmallIntegerField()
    cantidad = models.SmallIntegerField()
    #cantidad_elegida = models.SmallIntegerField()
    #total = models.IntegerField()

    def __str__(self):
        return self.descripcion


class MenusComida(models.Model):
    id_menusc = models.SmallAutoField(primary_key=True)
    producto = models.CharField(max_length=80)
    descripcion = models.TextField(max_length=600)
    precio_persona = models.SmallIntegerField()
    #cantidad_elegida = models.SmallIntegerField()
    #total = models.IntegerField()

    def __str__(self):
        return self.producto


class Clientes(models.Model):
    id_cliente = models.SmallAutoField(primary_key=True)
    nombre = models.CharField(max_length=80)
    direccion = models.CharField(max_length=150)
    telefono = models.IntegerField()
    rfc = models.CharField(max_length=13)

    def __str__(self):
        return self.nombre


class Historial(models.Model):
    id_historial = models.SmallAutoField(primary_key=True)
    cliente = models.ForeignKey(Clientes, on_delete=models.CASCADE)
    mobiliario = models.ManyToManyField(GestionMobiliaria)
    menusc = models.ManyToManyField(MenusComida)
    personal = models.ManyToManyField(Personal)
    total = models.IntegerField()
    a_cuenta = models.IntegerField()
    fecha_entrega = models.DateTimeField()
    estatus = models.SmallIntegerField()

    def __str__(self):
        return self.id_historial + (', ') + self.cliente


class Presupuesto(models.Model):
    id_presupuesto = models.SmallAutoField(primary_key=True)
    cliente = models.ForeignKey(Clientes, on_delete=models.CASCADE)
    mobiliario = models.ManyToManyField(GestionMobiliaria)
    menusc = models.ManyToManyField(MenusComida)
    personal = models.ManyToManyField(Personal)
    precio_unitario = models.SmallIntegerField()
    subtotal = models.IntegerField()
    descuento = models.IntegerField()
    total = models.IntegerField()
    a_cuenta = models.IntegerField()

    def __str__(self):
        return self.id_presupuesto + (', ') + self.cliente