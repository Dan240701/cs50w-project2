from django.contrib import admin
from .models import User, Categoria, Lista, Comentario, Oferta
# Register your models here.
# Primer paso para poder registrar datos desde nuestra vista admin
admin.site.register(User)
admin.site.register(Categoria)
admin.site.register(Lista)
admin.site.register(Comentario)
admin.site.register(Oferta)

