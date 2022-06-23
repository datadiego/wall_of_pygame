# wall_of_pygame

Este mural es un proyecto organizado por los alumnos del bootcamp realizado en Keepcoding.

La idea del repo es hacer un collage digital animado utilizando Python y pygame como base y la libertad de importar y usar las que queramos.

El proyecto sirve como espacio libre en el que practicar a crear diferentes clases, experimentar con las herramientas que nos da pygame para crear y usar gráficos, y empezar a utilizar github en grupo sin pensar en algo más que mover cosas en pantalla y practicar a interactuar entre ellas.
Hay total libertad para poner y dar el comportamiento que uno quiera a las imagenes y gráficos creados asi que go wild! 

No deberías preocuparte demasiado en que añadir o que hacer, asi que empieza simple, añade una imagen al mural! Las ideas empezarán a salir, las clases creadas las podremos compartir, heredar y ver como las ha creado cada uno de nuestros compañeros.

Por ultimo, aprenderemos a trabajar en equipo utilizando ramas y pull requests en github, y aunque es un proyecto con una escala pequeña, a plantear cambios de estructura en el codigo entre todos.

## Si quieres colaborar:
-   Crea una nueva rama en el repositorio:

![alt](/other/tutorial_0.png)
-   Clona este repositorio a tu PC:
```
git clone https://github.com/datadiego/wall_of_pygame
```

-   Crea un entorno virtual para instalar las dependencias:
```
python venv env
```
-   Activa el entorno virtual:

En PC:
```
.\env\Scripts\activate
```
Mac:
```
source ./env/bin/activate
```

-   Instala las dependencias necesarias:
```
pip install -r requirements-dev.txt
```
-   Abre el proyecto en vscode y situate en tu rama:

![alt](/other/tutorial_1.png)

![alt](/other/tutorial_2.png)

-    Desde terminal:
```
git checkout mi_rama
code .
```

Ya estas listo para empezar a editar tu rama del proyecto!
-   Realiza los commits que necesites, una vez lo tengas listo y hagas tu ultimo commit, ve al repo y haz click en "Compare & pull request":

![alt](/other/tutorial_3.png)

En la siguiente pagina puedes dejar un comentario sobre que has añadido en tu rama y tambien indica si tu rama sobreescribe algo que ya estaba antes escrito.

Una vez envies tu pull request entre todos podemos ver que los cambios que hace tu rama no rompen nada en el codigo y que todo esta correcto y hacer merge con la rama main.

## Estructura del proyecto

-   El archivo main.py es el que lanza el proyecto principal, aqui podremos importar nuestras clases, crear objetos con ellas y mostrarlos en el bucle principal
-   La carpeta resources contiene nuestros archivos .py con nuestras clases, ademas de una carpeta para almacenar las imagenes que queramos