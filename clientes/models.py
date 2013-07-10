# -*- coding: utf-8 -*-
from django.db import models
from smart_selects.db_fields import ChainedForeignKey

# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField('Nombre',blank=False, max_length=50, unique=True)

    def __unicode__(self):
   		return self.nombre

class Pais(models.Model):
    nombre = models.CharField('País',blank=False, max_length=50, unique=True)

    def __unicode__(self):
   		return self.nombre

    class Meta:
		verbose_name_plural = u'Paises'
		ordering =['nombre']

class Estado(models.Model):
    nombre = models.CharField('Estado', blank=False, max_length=50, unique=True)
    pais = models.ForeignKey(Pais)

    def __unicode__(self):
   		return '%s - %s' % (self.nombre, self.pais)
   		

class Ciudad(models.Model):
	

    nombre = models.CharField('Ciudad',blank=False, max_length=50, unique=True)
    estado = models.ForeignKey(Estado)

    class Meta:
		verbose_name_plural = u'Ciudades'
		ordering =['nombre']

    def __unicode__(self):
   		return '%s - %s' % (self.nombre, self.estado)
   		

    

class Cliente(models.Model):
	nombre = models.CharField('Nombre', blank=False, max_length=200, unique=True)
	direccion = models.TextField('Dirección')
	telefonos = models.CharField('Telefonos', max_length=50,blank=True)
	pais = models.ForeignKey(Pais)
	estado = ChainedForeignKey(
        Estado, 
        chained_field="pais",
        chained_model_field="pais", 
        show_all=False, 
        auto_choose=True
    )
	ciudad = ChainedForeignKey(Ciudad,chained_field='estado',chained_model_field='estado')
	ingreso = models.DateTimeField('Fecha de Ingreso', auto_now_add=True)
	modificado = models.DateTimeField('Fecha de Modificación',auto_now=True)
	geo = models.CharField('Geolocalización', max_length=50,blank=True)
	categoria = models.ManyToManyField(Categoria)

	def __unicode__(self):
   		return self.nombre


	

