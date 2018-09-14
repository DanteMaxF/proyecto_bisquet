from django.db import models
from django.urls import reverse #Used to generate URLs by reversing the URL patterns

class Category(models.Model):
    """
    Modelo que representa una categoría de un producto
    """
    name = models.CharField(max_length=200, help_text="Ingresa el nombre de la categoría")
    description = models.CharField(max_length=200, help_text="Ingresa la descripción de la categoría")


    def __str__(self):
        """
        Cadena que representa a la instancia particular del modelo (p. ej en el sitio de Administración)
        """
        return self.name

class Unit(models.Model):
    """
    Modelo que representa a una unidad de medida
    """
    name = models.CharField(max_length=200)

    syntax = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Product(models.Model):
    """
    Modelo que representa un producto
    """

    name = models.CharField(max_length=200)

    description = models.TextField(max_length=1000, help_text="Ingresa una breve descripción del producto")

    category = models.ForeignKey(Category, help_text="Selecciona una categoría para este producto", on_delete=models.DO_NOTHING)

    unit = models.ForeignKey(Unit, help_text="Selecciona la unidad de medida del producto", on_delete=models.DO_NOTHING)


    LOAN_STATUS = (
        ('a', 'Activo'),
        ('i', 'Inactivo'),
    )

    status = models.CharField(max_length=1, choices=LOAN_STATUS, blank=True, default='a', help_text='Disponibilidad del producto')

    class Meta:
        ordering = ["name"]

    def __str__(self):
        """
        String que representa al objeto
        """
        return self.title
