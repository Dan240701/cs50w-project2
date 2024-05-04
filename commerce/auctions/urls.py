
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("crear", views.crear_lista, name="crear"),
    path('vista_categoria/<int:id>/', views.vista_categoria, name='vista_categoria'),
    path("listado/<int:id>", views.listado, name="listado"),
    path("ver_watchlist", views.ver_watchlist, name="ver_watchlist"),
    path("agregar_watchlist/<int:id>", views.agregar_watchlist, name="agregar_watchlist"),
    path("eliminar_watchlist/<int:id>", views.eliminar_watchlist, name="eliminar_watchlist"),
    path("agregar_comentario/<int:id>", views.agregar_comentario, name="agregar_comentario"),
    path("pujar/<int:id>", views.agregar_oferta, name="agregar_oferta"),
    path("cerrar/<int:id>", views.cerrar_subasta, name="cerrar_subasta"),
]
