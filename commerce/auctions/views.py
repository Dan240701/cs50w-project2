from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import User, Categoria, Lista, Comentario, Oferta


def index(request):
    categorias = Categoria.objects.all()
    listado_activo = Lista.objects.filter(es_activo=True)
    return render(request, "auctions/index.html",{
        "listado": listado_activo,
        "categorias": categorias
    })

def vista_categoria(request, id):
    categoria_seleccionada = Categoria.objects.get(id=id)
    listado_activo = Lista.objects.filter(es_activo=True, categoria=categoria_seleccionada)
    return render(request, "auctions/index.html",{
        "listado": listado_activo,
        "categorias": Categoria.objects.all()
    })

def listado(request, id):
    loguser= request.user
    listaProductos = Lista.objects.get(pk=id)
    WatchlistActivo = listaProductos.watchlist.filter(pk=loguser.id).exists()
    Comentarios = Comentario.objects.filter(lista=listaProductos)
    Ofertas = Oferta.objects.filter(oferta_lista=listaProductos)
    
    Ganador = listaProductos.seller.username

    return render(request, "auctions/listado.html",{
        "listado": listaProductos,
        "WatchlistActivo": WatchlistActivo,
        "Comentarios": Comentarios,
        "Oferta": Ofertas,
        "Ganador": Ganador,
        "loguser": loguser,
    }) 
  
def agregar_oferta(request, id):
    loguser= request.user
    Producto = Lista.objects.get(pk=id)
    Puja = request.POST['puja']
    WatchlistActivo = Producto.watchlist.filter(pk=loguser.id).exists()
    Comentarios = Comentario.objects.filter(lista=Producto)
    Ganador = loguser.username = Producto.seller.username

    if float(Puja) > Producto.precio.oferta:
        nuevoPrecio = Oferta(user = loguser, oferta=Puja)
        nuevoPrecio.save()
        Producto.precio = nuevoPrecio
        Producto.save()
        return render(request, "auctions/listado.html",{
            "listado": Producto,
            "WatchlistActivo": WatchlistActivo,
            "Comentarios": Comentarios,
            "Estado": True,
            "mensaje": "Oferta realizada con exito",
            "Ganador": Ganador,
        })
    else:
        return render(request, "auctions/listado.html",{
            "listado": Producto,
            "Estado": False,
            "mensaje": "La oferta debe ser mayor a la actual",
            "WatchlistActivo": WatchlistActivo,
            "Comentarios": Comentarios,
            "Ganador": Ganador,
        })


def agregar_watchlist(request, id):
    loguser= request.user
    listaProductos = Lista.objects.get(pk=id)
    listaProductos.watchlist.add(loguser)
    return HttpResponseRedirect(reverse('listado', args=(id,)))

def eliminar_watchlist(request, id):
    loguser= request.user
    listaProductos = Lista.objects.get(pk=id)
    listaProductos.watchlist.remove(loguser)
    return HttpResponseRedirect(reverse('listado', args=(id,)))

def ver_watchlist(request):

    loguser = request.user
    watchView = Lista.objects.filter(watchlist=loguser)
    return render(request, "auctions/watchlist.html",{
        "watchlist": watchView
    })

def agregar_comentario(request, id):
    LogUser = request.user
    ListaProducto = Lista.objects.get(pk=id)
    nota = request.POST["comentario"]
    comentario = Comentario(comentario=nota, user=LogUser, lista=ListaProducto)
    comentario.save()

    return HttpResponseRedirect(reverse('listado', args=(id,)))


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))

def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")
        
def crear_lista(request):
    categorias = Categoria.objects.all()

    if request.method != "POST":
        return render(request, "auctions/agregar.html",{
            "categorias": categorias
        })
    else:
        titulo = request.POST["titulo"]
        descripcion = request.POST["descripcion"]
        precio = request.POST["precio"]
        image_url = request.POST["image_url"]
        seller = request.user
        #Agregamos una oferta en base al precio que enviamos desde el formulario
        oferta = Oferta(oferta = float(precio), user=seller)
        oferta.save()
        #creamos un objeto categoria con la llave primaria que enviamos desde el formulario
        categoria = Categoria.objects.get(pk=request.POST["categoria"])
        #creamos un objeto lista con los datos que enviamos desde el formulario
        lista = Lista(titulo=titulo, descripcion=descripcion, precio=oferta, image_url=image_url, categoria=categoria, seller=seller)
        lista.save()
        #retornamos a la pagina principal
        return HttpResponseRedirect(reverse("index"))

def cerrar_subasta(request, id):
    loguser= request.user
    ListaProducto = Lista.objects.get(pk=id)
    ListaProducto.es_activo = False
    ListaProducto.save()
    Ganador = loguser.username = ListaProducto.seller.username
    WatchlistActivo = ListaProducto.watchlist.filter(pk=loguser.id).exists()
    Comentarios = Comentario.objects.filter(lista=ListaProducto)

    return render(request, "auctions/listado.html",{
        "listado": ListaProducto,
        "Estado": True,
        "mensaje": "Felicidades, la subasta ha sido cerrada con exito",
        "Ganador": Ganador,
        "WatchlistActivo": WatchlistActivo,
        "Comentarios": Comentarios,
    })

    