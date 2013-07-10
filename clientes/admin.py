from clientes.models import *
from django.contrib import admin

class ClienteAdmin(admin.ModelAdmin):
	list_filter = ['categoria']
	search_fields = ['nombre','telefonos']
	list_display = ['nombre','telefonos','ingreso','modificado']

class CiudadAdmin(admin.ModelAdmin):
	list_filter = ['estado']
	search_fields = ['nombre']
		

admin.site.register(Categoria)
admin.site.register(Ciudad,CiudadAdmin)
admin.site.register(Pais)
admin.site.register(Estado)
admin.site.register(Cliente, ClienteAdmin)