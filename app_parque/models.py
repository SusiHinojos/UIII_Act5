from django.db import models

# NOTA: Atraccion y Empleado se definen con ForeignKey circular (ambos se referencian). 
# Para evitar errores de referencia, Atraccion debe definirse primero, o usar cadena. 
# Aquí usaremos la cadena 'Atraccion' en Empleado para asegurar la funcionalidad.

# =================
# MODELO: ATRACCIÓN
# =================
class Atraccion(models.Model):
    # Clave Primaria (PK)
    id_atr = models.AutoField(primary_key=True, unique=True) # [cite: 53]

    # Campos
    nombre = models.CharField(max_length=50) # [cite: 54]
    tipo = models.CharField(max_length=50) # [cite: 55]
    capacidad = models.IntegerField() # [cite: 56]
    estado = models.CharField(max_length=100) # [cite: 57]
    altura_min = models.DecimalField(max_digits=3, decimal_places=2) # [cite: 58]

    # Clave Foránea (FK) a Empleado (Empleado encargado de la Atracción)
    # Se usa SET_NULL para que si se borra el Empleado, la Atracción no se borre.
    id_emp = models.ForeignKey('Empleado', on_delete=models.SET_NULL, null=True, blank=True) # [cite: 59]

    def __str__(self):
        return self.nombre # [cite: 61]
    
# =================
# MODELO: EMPLEADO (Trabajaremos con este primero, como se indica en el paso 13)
# =================
class Empleado(models.Model):
    # Clave Primaria (PK)
    id_emp = models.AutoField(primary_key=True, unique=True) # [cite: 28]

    # Campos
    nombre = models.CharField(max_length=50) # [cite: 29]
    apellido = models.CharField(max_length=50) # [cite: 30]
    puesto = models.CharField(max_length=40) # 
    telefono = models.CharField(max_length=15) # [cite: 32]
    salario = models.DecimalField(max_digits=8, decimal_places=2) # [cite: 33]
    
    # Clave Foránea (FK) a Atraccion (Atracción asignada al Empleado)
    # id_atr: La FK se define en el modelo Empleado.
    id_atr = models.ForeignKey(Atraccion, on_delete=models.SET_NULL, null=True, blank=True) # [cite: 34]
    
    def __str__(self):
        return self.nombre # [cite: 35, 36]

# =================
# MODELO: CLIENTE
# =================
class Cliente(models.Model):
    # Clave Primaria (PK)
    id_cli = models.AutoField(primary_key=True, unique=True) # [cite: 41]

    # Campos
    nombre = models.CharField(max_length=50) # [cite: 42]
    apellido = models.CharField(max_length=50) # [cite: 43]
    telefono = models.CharField(max_length=15) #
    correo = models.CharField(max_length=50) #
    fecha_reg = models.DateField(auto_now_add=True) # [cite: 44]

    # Clave Foránea (FK) a Atraccion (Atracción a la que se registra el cliente)
    # Se usa CASCADE para que si se borra la Atracción, el registro del Cliente también.
    id_atr = models.ForeignKey(Atraccion, on_delete=models.CASCADE) # [cite: 45]

    def __str__(self):
        return self.nombre # [cite: 47, 48]