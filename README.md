# Morse for Coders

En simples palabras es un traductor amigable de código morse a carácteres alfanuméricos

## Ejecución

Para comenzar la ejecución del proyecto se debe iniciar el documento main por medio de:

##### El terminal (recomendado):
[Imgur](https://i.imgur.com/areKglA.png)

## Primer Lanzamiento
Al iniciar el documento main este va a generar una ventana:
[Imagen]

Lo primero que salta a la vista es el primer campo, donde se puede escribir lo que se desea traducir:
[otra Imagen]

Es importante saber qué se está traduciendo y qué resultado se obtendrá, esto se puede visualizar en la parte superior del cuadro de entrada y el cuadro de salida.
[img]

Esto se puede cambiar usando el botón de cambio que como describe su nombre, cambia la modalidad entre alfanumerico-morse a morse-alfanumerico y viceversa.
[img]

Si se quiere limpiar rápidamente la entrada y la salida se puede usar el botón de LIMPIAR que limpiará la ventana en fracción de segundos.
[img]

Por último el botón ? genera una ventana que mostrará información de los creadores del proyecto además de un botón que te llevará al repositorio de GitHub, donde el proyecto se aloja.
[ultima imagen]



# Metodología

**“main.py”**: Este archivo es el principal como indica su nombre y es el encargada de iniciar y mostrar la ventana principal por medio de la creación de un "mainWindow".
**Clase "mainWindow"**: Esta clase es la clase "núcleo" ya que la gran parte de los métodos ocurren en esta clase, esta clase incorpora los siguientes métodos:
 + ***"switchFunction"*** la que es accionada por el botón marcado con "<--->". Al ser activado cambia la modalidad de traducción entre Alfanumérico-MORSE a MORSE-Alfanumérico.

 + ***"clearAll"*** simplemente limpia todo, la entrada y el resultado, por medio de definir el texto en cada uno de los contenedores como un string vacío ("").
 
 + ***"about"*** Es el método encargado de generar y mostrar la ventana de información básica del proyecto.

 + ***"entryInput"*** Este método es activado cuando la entrada de texto cambia, esto para actualizar la traducción de manera automática. Además esta detecta, por medio del label del título que se encuentra arriba de la misma, en qué modo se encuentra el proyecto, en el caso de que el modo sea morse y la entrada detecte un carácter que no pertenezca a los símbolos usados en el morse ".-/" mostrará un mensaje de recordatorio.

 + ***"Decodificadores"*** Hay en total 4 decodificadores trabajando para desempeñar la función de traducción bidireccional entre Morse y Alfanumérico, en esencia estos trabajan comparando los datos ingresados con un diccionario que alberga las traducciones de Morse.

**Clase "about"**: En esta clase se desempeña la generación y gestión de una ventana que despliega información sobre el proyecto, además de incluir un botón que muestra el repositorio donde se aloja el proyecto por medio del navegador de preferencia.

**"alfanumerico_morse.py"** Es un archivo que contiene un diccionario con el que se hace el trabajo de traducción.


## Desarrollado por:
- Angel Guerrero
- Yostin Sepulveda

