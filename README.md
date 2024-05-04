# Commerce Project 2

## Descripción del proyecto

### Modelos
La aplicación se constituye de un modelo que cuenta con 5 clase en total (Incluyendo la clase User)

La logica general de estos modelos nos permitira, crear listas, realizar ofertas, comentar en la pagina de la listas y visitar las diferentes categorias de los productos, permitiendonos filtrarlos en base a nuestras necesidades.

### Views
La aplicación se compone de varias vistas que permiten interactuar con los modelos y presentar la información al usuario.

La lógica general de estas vistas nos permitirá, por ejemplo, ver listas de productos, realizar ofertas en productos, dejar comentarios en las páginas de los productos y navegar por las diferentes categorías de productos. Cada vista está diseñada para presentar la información de una manera fácil de entender y permitir al usuario interactuar con la aplicación de manera intuitiva.

### URLS.PY

El archivo `urls.py` en nuestro proyecto de subastas en línea define las rutas para todas las operaciones que los usuarios pueden realizar.

- `/` o `/home`: Esta es la ruta para la página de inicio, donde se muestran todos los listados activos.
- `/listado/<int:id>`: Esta ruta muestra los detalles de un listado específico, donde `<int:id>` es el ID del listado. Los usuarios pueden hacer ofertas en este listado o agregarlo a su lista de seguimiento.
- `/crear`: Esta ruta lleva a un formulario donde los usuarios pueden crear un nuevo listado.
- `/watchlist`: Esta ruta muestra todos los listados que el usuario ha agregado a su lista de seguimiento.
- `/categorias`: Esta ruta muestra todas las categorías disponibles y permite al usuario ver listados por categoría.
- `/cerrar/<int:id>`: Esta ruta permite al propietario de un listado cerrar la subasta, donde `<int:id>` es el ID del listado.

Cada una de estas rutas está asociada con una vista que maneja la lógica correspondiente y devuelve una respuesta al usuario.

### Templates
- `index.html`: Este template sera el Home de nuestro sitio y mostrara todos los listados activos en la página de inicio.
- `listado.html`: Este template muestra los detalles de un listado específico, incluyendo la imagen del producto, la descripción, las ofertas actuales y los comentarios.
- `crear.html`: Este template contiene un formulario que permite a los usuarios crear un nuevo listado.
- `watchlist.html`: Este template muestra todos los listados que el usuario ha agregado a su lista de seguimiento.
- `cerrar.html`: Este template permite al propietario de un listado cerrar la subasta y muestra el ganador y la oferta ganadora.

Cada uno de estos templates se renderiza en respuesta a una solicitud a la ruta correspondiente, y se le pasan los datos necesarios desde la vista asociada.
