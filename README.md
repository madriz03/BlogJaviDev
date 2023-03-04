# BLOG JAVIDEV

Este blog inicialmente lo hice como proyecto final del bootcamp de Backend con Python en Codigo Facilito pero seguire trabajando en el ya que sera usado para compartir mis experiencias como programador, compartir conocimiento y otras temas de interes del mundo IT.

## Tecnologias Usadas
- **Python** como lenguaje de programacion
- **Django** como Framework para Backend
- **Postgresql** como motor de base de datos
- **Pincelada** de Html, Css y Js, recuerden son Backend :tw-1f602:

## Arquitectura del Proyecto
Nuestro proyecto esta construido bajo la arquitectura Model Template View **MTV** de Django, asi que la base fundamenta de nuestro proyecto esta definida en los archivos models.py, views.py y directorio de templates.

## Aplicaciones
Nuestro blog esta compuesto por dos aplicaciones:

### Usuarios
Aqui esta definido todo lo relacionado a registro y autenticacion, 

## Post
Aqui esta definido la gran parte de la logita de nuestro blog, donde construimos nuestros post y comentarios.

## Model Template View
### Modelos:
Para la aplicacion usuarios utilizamos el modelo users predefinido de Djando.

En la aplicacion Post tenemos los siguientes modelos:
**Post** Relacionado con el modelo Users
**Comment **Relacionado con el modelo Post y Users.

## Vistas
El views.py de nuestra aplicacion  Users esta compuesta por la vista register que se encarga de los datos de un nuevo registro de usuario el cual se le pasa al modelo user para la creacion de un nuevo usuario.

Las vistas Login y Logout no estan definidas en el views.py debido a que estamos usando la LoginViews y LogoutViews de Django y solo hacemos uso de ellas en la URLs, puedes revisar el archivo urls.py o la documentacion de Django.
[Using the Django authentication system](http://https://docs.djangoproject.com/en/4.1/topics/auth/default/#django.contrib.auth.views.LoginView "Using the Django authentication system")

## Templates
Cada aplicacion tiene su propio directorio para templates dentro del directorio principal de **templates** asi como tambien su directorio para archivos estaticos dentro del directorio static.

Existe un directorio **layout** donde se encuentra el codigo que comparte todas las rutas contempladas en nuestro proyecto y asi hacemos uso del principio **No repeat Yoursel** como buena practica de programacion.

Existe el directorio **partials** que esta destinado para francciones de codigo que cumplen con una tarea en especifico en nuestro proyecto como por ejemplo la fraccion de codigo JS que usamos para contar los caracteres restantes que el usuario podra ver al momento de comenzar a escribir un comentario el cual colocamos en partial e hicimos uso de el en nuestro template detail con la funcionalidad include Django.

## Deploy
Este proyecto estara desplegado en Digital Ocean, sin embargo compartire con ustedes como se ve hasta el momento la interfaz del Blog.

## Home

La vista Home lista todos los post con una fraccion de su contenido, puede darle ver mas para ver el contenido completo en la vista detail.

![Home](https://live.staticflickr.com/65535/52725539887_ddb7cec071_c.jpg "Home")

## Detail
Esta vista muestra el detalle el post completo y ademas los comentarios asociados a ese post.

![Detail](https://live.staticflickr.com/65535/52726325234_3211451272_z.jpg "Detail")

## Registro
Esta vista muestra el formulario para registro de usuarios

![Registro](https://live.staticflickr.com/65535/52726557218_358d2f089e_w.jpg "Registro")

## Login
Esta vista muestra el formulario de inicio de sesion.

![Login](https://live.staticflickr.com/65535/52725559807_ba321aa9a9_n.jpg "Login")


## Invitacion
Si llegaste hasta aca muchas gracias, cualquier duda sobre el proyecto o colaboracion que quieras hacer no dudes en dejarme un mensaje, cuando el proyecto este en priduccion espero puedas interactuar con el y hacerte un usuario.

## Mis Redes Sociales
[Linkedin](http://https://www.linkedin.com/in/javiermadriz3/ "Linkedin")
[Twitter](https://twitter.com/madriz03 "Twitter")
