TEORÍA FUNDAMENTAL
""" Teoría general autodidáctica para el pensamiento informático: http://www.openbookproject.net/thinkcs/archive/python/spanish2e/index.html

NIVEL 1 CÓDIGO PYTHON
- Lenguaje de alto nivel (Python, C++, PHP, Java): programas escritos primero traducidos y después ejecutados por la computadora. Son más fáciles, rápidos, cortos, con mejor lecturabilidad, mejor corrección de errores y son portables a otras computadoras sin apenas modificaciones (no como los otros que deben ser reescritos para ser ejecutados en otro PC).
- Lenguaje de bajo nivel (lenguajes de máquina, lenguajes ensambladores): programas escritos ejecutados por la computadora. Se usan para ciertas aplicaciones especiales.
- Intérprete: lector y ejecutor de los comandos de un determinado programa de alto nivel.
- Compilador: lee y traduce el programa de alto nivel (código fuente) antes de su ejecución, el cual una vez traducido pasa a ser programa ejecutable (código objeto) compuesto por Bytecodes (códigos de bytes), llamados así porque cada código de operación tiene una longitud promedio de un byte (y suelen ser tratados como archivos binarios).
- Código: conjunto de líneas que indica los pasos a seguir por una computadora para ejecutar un software o programa.
- Programa: secuencia de instrucciones que especifican cómo ha de ejecutarse un cómputo.
- Instrucciones: comandos u órdenes con apariencia determinada (color, invocación particular) que suelen expresar: entrada, salida, condición, repetición, operaciones matemáticas, y un largo etcétera en los que se incluyen los algoritmos (procesos generales para resolver problemas completos).
- Cómputo: idea expresada mediante un lenguaje formal (lenguaje de programación). Puede ser matemático (sistemas de ecuaciones, raíces polinómicas...) o simbólico (buscar o reemplazar el texto de un documento, compilar un programa...).
- Depuración: ciencia experimental basada en la subsanación de errores de sintaxis, errores semánticos y errores en tiempo de ejecución. Los primeros refieren a estructuras y reglas internas de las mismas (qúe bièn leer). Los segundos dan resultados pero no los deseados por sentido o significado incorrecto (ingeniería inversa para identificarlos). Los terceros aparecen al ejecutar un programa (sucesos malos pero muy excepcionales).
- Lenguaje formal: lenguaje de programación diseñado para expresar cómputos mediante unidades léxicas y estructuras. Difieren de los lenguajes naturales (los idiomas humanos) por ser inequívocos, poco redundantes, muy concisos y literales (no metafórico).
- Unidad léxica: análogo a las palabras de un lenguaje natural (español, francés, italiano, inglés, chino, alemán, ruso, griego...).
- Sentencia: Instrucción que el intérprete del programa puede ejecutar. Una sentencia compuesta contiene como mínimo dos bloques: encabezado y cuerpo.
- Sentencia de asignación: crea nuevas variables y les otorga valores para que el intérprete de Python lo pueda ejecutar.
- Print: instrucción que muestra en pantalla un valor impreso entre paréntesis, resultado de una sentencia dada (las sentencias de asignación no producen un resultado per se). La sentencia print sin argumentos muestra una nueva línea.
- Variable: nombre al que se refiere a un valor concreto asignado (señalado, fijado, designado). Pueden ser largos y contener letras y números, pero han de empezar siempre con letra y a la izquierda. 
- Valor: tipo de código que manipula un programa informático.
- Expresión: combinación de valores, variables y operadores representado como un único valor siempre al lado derecho de una sentencia de asignación.
- Cadena: el string es una encadenación de caracteres (agrupaciones de letras, números, ambas...) encerrados en comillas (simples, dobles o triples).
- Cadena f: Las cadenas 'f' son una notación que contiene variables, valores, expresiones y operaciones matemáticas entre llaves {}, siendo lo de dentro sustituido por la asignación que incrustemos dentro (usualmente referido a una variable y/o sentencia previa). La doble llave siempre ha de ir precedida de comillas y a su vez de la letra f (representando 'literal').
- Integer: número entero (0-9), sea positivo o negativo.
- Float: número decimal (2.0).
- Operador: símbolo especial que representa cómputos (aritmética) cuyos valores que utilice serán denominados como "operandos".
- Operador de asignación: enlaza un nombre a la izquierda con un valor en el lado derecho mediante un '=' entre medias (numeroasdfg = 55).
- Mayúsculas: por convención no se usan.
- Letras ilegales: aquellas que dan error de sintaxis como $ (salvo que se emplee la función ascii).
- Palabras reservadas: excepciones que no pueden ser usadas como nombres de variables a la izquierda de una sentencia, oración o frase de asignación. Python tiene treinta y una reservadas:
    and, as, assert, break, class, continue, def, del, elif, else, except, exec, finally, for, from, global, if, import, in, is, lambda, not, or, pass, print, raise, return, try, while, with, yield
- Reglas de precedencia: operadores matemáticos según el orden de evaluación 'PPMDAS' (Paréntesis, Potenciación, Multiplicación-División, Adición-Substracción). Relacionado a su vez con los flujos de ejecución.
- Operaciones sobre cadenas: '+' representa la operación de concatenación, enlazando dos operandos. '*' hace una operación de repetición.
- Función: secuencia con nombre asignado de diversas sentencias compuestas que ejecutan una operación deseada (conjunto de instrucciones agrupadas bajo un nombre concreto). Permite recortar el código repetitivo al ser reutilizable. La sintaxis para su definición es:
    def NOMBRE_FUNCIÓN( LISTA DE PARÁMETROS ):
        BLOQUE DE SENTENCIAS / CONJUNTO DE INSTRUCCIONES
- definición: encabezado 'def' que define una función junto con una lista de parámetros encerrados entre paréntesis. Definir no conlleva a ejecución, para ello es necesario una llamada a función. Una definición puede aparecer dentro de otra, pero la def interna no se ejecutará hasta que se produzca la llamada de la función externa.
- Lista de parámetros: especifica la información que se debe proporcionar para usar una nueva función. Puede estar vacía. Suelen tener la forma de '()' y pueden estar vacíos.
- Llamada a función: contienen el nombre de la función a ejecutar seguido por la lista de valores asignados (argumentos) a los parámetros en la definición de la función. El tipo de archivo de los diferentes argumentos que se le coloquen al etiquetado definido posteriormente se verán reflejados si se posa el puntero del ratón encima.
- Argumentos: valores simples o expresiones, que además controlan la manera en que las funciones trabajan.
- Flujo de ejecución: orden de las sentencias de arriba (línea 1) a abajo (líneas posteriores). Las llamadas a función producen un desvío saltando a la primera línea de la función llamada, ejecutando todas las sentencias de dicha función, para retornar y continuar con la lectura del programa.
- Función llama a función: mientras se ejecuta una función, el programa puede ejecutar las sentencias de otra función, pudiendo para ello tener que ejecutar a su vez otra función. Este lío es el que hace que sea mejor leer el programa siguiendo el flujo de ejecución que no de arriba a abajo.
- Tipo de archivo: type muestra el valor de lo que se manipula entre paréntesis (cadena de caracteres, integers, floats, pi...).
- Variable local: valor asignado a una función que fuera de ella.
- Secuencia de escape: incrustación para saltar una línea, tabulación, espacio o carácter mediante la barra inversa \, y la adición de otro carácter concreto (\n, \', \\...).
- Anidamiento: estructura de un programa (sentencia condicional) dentro de otra rama (dentro de otra distinta sentencia condicional).
- Bucle: estructura iterativa/repetitiva/reiterativa que ejecuta un mismo bloque de código equis número de veces. Puede ser una lista, rango, datos de tipo almacenaje...
        - Bloque: conjunto de sentencias sangradas, estando este texto dentro de dos cuerpos de una sentencia como se ve en esas dos líneas verticales al comienzo de esta línea de código.
- def: sentencia que define a una función (con un nombre o un identificador, seguido de una lista opcional de parámetros entre paréntesis) que se va a usar para crear objetos (siendo necesario invocarlas en el momento oportuno de su desarrollo).
- variable local: variable definida dentro de la función única y exclusivamente. No servirá para otras funciones salvo que hagamos return.
- variable global: variables declaradas fuera de la función, pero disponibles dentro y fuera de la función.
- ruta absoluta: ubicación de un archivo o de un directorio comenzando desde el directorio raíz del sistema de archivos (desde el disco A:, C:, D:...).
- ruta relativa: ubicación de un archivo desde el directorio actual donde nos encontramos. Es lo que usamos en la cmd con '..', que ambas refieren simbólicamente al directorio actual y al directorio padre [el equivalente humano a los tres puntos suspensivos iniciales, desde donde lo dejamos].
- for: función bucle que implica acceder secuencialmente a cada uno de los elementos de una lista o realizar una acción concreta dentro de su composición/parámetros internos.

NIVEL 2 PROGRAMACIÓN ORIENTADA A OBJETOS EN PYTHON
-- Programación orientada a objetos: paradigma de programación que contiene propiedades, acciones, métodos y demás cosas que un objeto puede llegar a hacer. Organiza y escala mejor nuestro software. Lo hace más reusable.
-- Clase de objetos: las clases son los moldes que permiten crear infinidad de objetos con características parecidas entre ellos.
-- Atributos/propiedades: piezas o rasgos que formarán a una variable (marca, color, modelo, número de características concretas, tipo de cositas que lo componen...)
-- Métodos: acciones que puede realizar nuestro objeto. Van precedidos del nombre del objeto y un punto ('.').
-- Abstracción en POO: se puesen usar objetos sin necesidad de conocer su funcionamiento interno.
-- Herencia: las propiedades y métodos pueden tomarse de una clase a otra (las variables, características y acciones básicas).
-- Modularidad: división fractal en ramajes más completos de un objeto. Un módulo (o librería) es un fichero que contiene código donde se almacenan diferentes declaraciones, funciones y scripts fabricados.
-- Encapsulación: reunir los métodos que tienen relación con una entidad concreta.
-- Ocultación: cada objeto deben tener sus propios datos internos, solo modificables dentro de la clase a la que pertenecen.
-- Constructor: Método especial dentro de una 'clase' que se suele utilizar para darle un valor a los atributos del objeto al crearlo. Primer método que se ejecuta al crear el objeto y se llama automáticamente al crearlo. Puede recibir parámetros como cualquier otro método. Cuando invoquemos la 'clase', le pasamos entonces los parámetros.
-- Herencia: capacidad/posibilidad para compartir atributos y métodos entre clases (clase madre -> clases hijas).

NIVEL 3 BASES DE DATOS PARA PYTHON
- Una base de datos se compone de tablas, columnas (campos) y filas (registros).
- Los Sistemas Gestores de Base de Datos (SGBD) son un conjunto de programas que permiten el almacenamiento, la modificación y la extracción de la información dentro de una base de datos ya sea mediante informes, aplicaciones o herramientas específicas de consulta.
- El 'sqlite3' es un sistema gestor de base de datos ligero basado en SQL (Structured Query Language), ya instalado dentro del lenguaje Python en un módulo.
- Siempre se debe abrir y cerrar una conexión para guardar los cambios realizados en su interior.
- Antes de crear una tabla es necesario crear un cursor, aquello que te va a permitir ejecutar una consulta.
- Claúsula: palabras clave en mayúsculas (CREATE, TABLE, IF, NOT, EXISTS, INTEGER, PRIMARY, KEY, AUTOINCREMENT, INSERT, INTO, VALUES, DELETE, FROM, UPDATE, SET, WHERE, SELECT...) que afectan interactuando con los elementos de una tabla.
- Métodos más importantes: conexion.commit (guardar cambios, para cada instrucción o ejecución dentro del script), cursor.execute (para cada ejecución), .fetchall or .fetchone para cantidades de registros de una tabla a afectar...
- 

NIVEL 4 MySQL/MariaDB en PYTHON
-- Hypertext Preprocessor (PHP): lenguaje de programación adaptado al entorno y desarrollo web. Necesita de tres herramientas: navegador web, editor de código o entorno de desarrollo integrado y un servidor de aplicaciones web.
-- Editor de código vs Entorno de Desarrollo Integrado (IDE): una modifica código y la otra tiene más herramientas integradas aparte, como Reconocimiento Avanzado de clase, Sugerencias de código avanzada, un gestor de base de datos en su interior [María DB o MySQL que son lo mismo]...).
   IDE es una aplicación que integra en un espacio común todas las herramientas que el programador necesita en cada fase del desarrollo de sus programas, desde la edición del código, hasta la compilación, el depurado y la ejecución, así como un conjunto adicional de funciones que facilitan todas estas labores.
-- Netbeans: IDE o editor de código.
-- Servidor de aplicaciones web: conjunto de herramientas o servidores que permiten servir localmente una web, poner a disposición del usuario una web. En el entorno de PHP hay un servidor Apache (el servidor web que te permite tener tu local host, urls...), el lenguaje de programación (PHP) y la base de datos MySQL/MariaDB para almacenaje de los mismos.
-- Instalación e interfaz: ver vídeo "Instalar servidor de MySQL para trabajar con las BBDD en Python".
-- modelo: fuente única y definitiva de información sobre sus datos que se encarga de tratar directamente con la base de datos, permitiendo la creación de diversos objetos de ese tipo y manipularlo.
-- hash: cifrado de contraseña para que no se muestren como texto plano o vulnerabilidad similar.
-- rowcount: método que devuelve la cantidad de registros y filas que hayan sido afectadas.

NIVEL 5 TKINTER
- Tkinter: módulo para crear interfaces gráficas de usuario.
- Parámetro keyboard: DDD.
- Side: modifica la colocación de un elemento.
- Frames: cajas manipulables (ventanas dentro de una ventana).

NIVEL 6 DESARROLLO WEB HTML (en el entorno 'Sublime Text 3')
-- ver index.html - apuntes. Anotación de etiquetas que hay: [https://developer.mozilla.org/es/docs/HTML/HTML5/HTML5_lista_elementos] [107 para empezar].

NIVEL 7 INSTALACIÓN DE DJANGO
- Entrar en Símbolo del sistema (cmd) o Ctrl+Shift+C dentro de Python (en Visual Code Studio por ejemplo) para tener el directorio base.
- 'DIR pip install Django==3.0.5' o la última versión disponible.
- 'DIR\python .h' => Sacará la ayuda de python. Nos interesa -m mod, que hace correr al módulo de una librería como si fuera un guion de código (un script).
- 'DIRECTORIO\python -m django --version' para comprobar
- 'DIRECTORIO\django-admin startproyect AprendiendoDjango => [no se pueden poner guiones en los nombres de proyectos] para que genere una carpeta, con el archivo 'manage.py' y otra carpeta con diferentes archivos {__init__.py} {asgi.py}{settings.py} {urls.py} {wsgi.py}.
- Ahora deberemos migrar el proyecto antes que hacer nada: 'DIRECTORIO\AprendiendoDjango\python manage.py migrate => Generará una base de datos {db.sqlite3} con las funcionalidades de las aplicaciones que vienen por defecto dentro de Django.
- Ejecutar el run server: 'DIRECTORIO\AprendiendoDjango\python manage.py runserver => Así tenemos un servidor "http://127.0.0.1:8000/" hasta que cerremos el Símbolo del Sistema, pudiendo trabajar con código de django y con nuestras aplicaciones web
- 'DIRECTORIO\python manage.py help => ahí localizamos el comando startapp: 'DIRECTORIO\python manage.py startapp miapp' => generará una carpeta con diferentes archivos: {__init__.py} {admin.py} {apps.py} {models.py} {tests.py} {viewvs.py}.

- MVC y MVT: Modelo Vista-Controlador y Modelo Template Vista. La vista que se muestra al usuario funciona igual en ambos. El controlador básico dentro de Django se conoce como vista el fichero {views.py}. MVT es lo mismo que MVC pero al controlador se le llama Vista y a la vista se le llama Temple.

NIVEL 8 AUTODIDACTA
- Asyncio: módulo (de la librería Python) para aplicar la concurrencia asíncrona en una parte del código. # El problema de la cena de los filósofos [palillos chinos]
    Concurrencia: habilidad de un programa, algoritmo o problema para ser ejecutado desordenadamente sin afectar al resultado final, realizando dichos cálculos u operaciones en distintos hilos.
    # Miguel Grinberg's 2017 Chess master Judit Polgár example [https://realpython.com/async-io-python/]
- Referencia de atributo: 'primary' seguido de '.' y un 'nombre. The primary must evaluate to an object of a type that supports attribute references, which most objects do.
"""

FUNCIONES DE PYTHON (MANERA EN LA QUE SE ORGANIZARÁ LA INFORMACIÓN):
    # Definición completa en inglés y su traducción |CLASIFICACIÓN/PARÁMETRO (color) DE LA PALABRA CLAVE | Principales funciones. --> Otros datos de interés
    # el color blanco indica valor asignado a una sentencia, el verde indica función, azul objeto, rojo error, gris ni idea.
    # |CODE SNIPPET| = Parte o trozo reusable de código fuente, código máquina o texto.

    # respecto a los errores echarle un ojo al siguiente enlace: https://docs.python.org/3/library/exceptions.html

AAA A16 AAA

abs # absolute; absoluto |ENTRY VALUE| Nº entero (1), nº flotador o decimal (1.5) y nº complejo (3+10j).
all # all; todo |ITERABLE| Da True si se repiten todos sus ítems o False. De estar vacío da True.
and # Operador lógico.
any # any; alguno |ITERABLE| Da True si algún ítem se repite o False. De estar vacío da False.
ascii # American Standard Code for Information Exchange; Código Estándar Americano para el Intercambio de Información |OBJETO| manera de introducir caracteres no alfanuméricos en una terminal de consola (cmd).
assert # assert; sostener |CONDITION| Testea mediante comparación == si una condición previamente dada es True o es False.
async # asynchronous function; función asíncrona |COROUTINE| Realiza concurrencias en distintos hilos para ahorrar tiempo y recursos en sus cálculos u operaciones. --> Importar asyncio (PEP [Python Enhacement Proposal] nº 3156) desde las librerías de Python para funcionalidades mejor que loops con callbacks.
await # answer wait; esperar respuesta |CONDITION| Unido a la corutina async, mantiene una operación hasta recibir cierta respuesta. --> Funciona parecido a la función yield.

1] "add/new/cell" # add new cell; añadir nueva celda |CODE SNIPPET| Implementa variables almacenadas localmente en celdas por múltiples campos, de manera que cuando se accede al valor de una variable, se usa el valor que está contenido en la celda en lugar del objeto celdado.
# %%

2] "async/def" # asynchronous definition; definición asíncrona |CODE SNIPPET| Une una función asíncrona con la declaración o definición de una función en su interior, formado por objetos con valores de uso concreto. --> Contiene una lista que permite enviar y tomar tantos parámetros o ítems como queramos
    async def funcname(parameter_list):
        pass

3] "async/for" # asynchronous for; asíncrono/para |CODE SNIPPET| Permite una iteración secuencial sobre una fuente asíncrona (pero sin paralelizar dichas operaciones), esperando el resultado para más adelante en lugar de finalizar inmediatamente cada tarea recién empezada. --> https://stackoverflow.com/questions/56161595/how-to-use-async-for-in-python
    async for target in iter:
        block

4] "async/for/else" # asynchronous for else; asíncrono/para/otro |CODE SNIPPET| lo mismo que lo anterior derivando a otra operación cuando termina la iteración.
    async for target in iter:
        block
    else:
        block

5] "async/with" # asynchronous with; asíncrono con |CODE SNIPPET| función asíncrona con una expresión. La expresión es una combinación de valores, variables y operadores representado como un único valor. --> http://www.openbookproject.net/thinkcs/archive/python/spanish2e/cap02.html
    async with expr as var:
        block

ArithmeticError # The base class for those built-in exceptions that are raised for various arithmetic errors: OverflowError, ZeroDivisionError, FloatingPointError.
AssertionError # Raised when an assert statement fails.
AttributeError # Raised when an attribute reference or assignment fails. (When an object does not support attribute references or attribute assignments at all, TypeError is raised.)

BBB B11 BBB

bin # DDD
bool # Expresión booleana cuyas sentencias estarán condicionadas a dos resultados: 'True' or 'False' (importante la mayúscula en ambas funciones).
break # DDD
breakpoint # DDD
bytearray # DDD
bytes # DDD
BaseException # DDD
BlockingIOError # DDD
BrokenPipeError # DDD
BufferError # DDD
BytesWarning # DDD

CCC C9 CCC

callable # DDD
chr # DDD
class # DDD
classmethod # DDD
compile # DDD
complex # DDD
continue # Cancela la ejecución de las instrucciones que quedan pendientes del bucle a partir del mismo momento de su aparición
copyright # DDD
credits # DDD

6] "class" # Code Snippet que muestra:
    class classname(object):
        pass

ChildProcessError # DDD
ConnectionAbortedError # DDD
ConnectionError # DDD
ConnectionRefusedError # DDD
ConnectionResetError # DDD

DDD D11 DDD

def # DDD
del # DDD
delattr # DDD
dict # DDD
dir # DDD
divmod # DDD

7] "def" # Code Snippet que muestra:
    def funcname(parameter_list):
        pass

8] "def(abstract class method)" # Code Snippet que muestra:
    def funcname(self, parameter_list):
        raise NotImplementedError)

9] "def(class method)" # Code Snippet que muestra:
    def funcname(self, parameter_list):
        pass

10] "def(static class method)" # Code Snippet que muestra:
    @staticmethod
    def funcname(parameter_list):
        pass

DeprecationWarning # DDD

EEE E11 EEE

ellipsis # DDD
enumerate # DDD
eval # DDD
exec # DDD
exit # DDD

11] elif # Code Snippet que muestra:
    elif expression:
        pass

12] else # Code Snippet que muestra:
    else:
        pass

Ellipsis # DDD
EnvironmentError # DDD
EOFError # DDD
Exception # DDD

FFF F14 FFF

filter # DDD
float # DDD
for # DDD
format # DDD
from # DDD
frozenset # DDD
funcname # DDD

13] "for" # Code Snippet que muestra:
    for target_list in expression_list:
        pass

14] "for/else" # Code Snippet que muestra:
    for target_list in expression_list:
        pass
    else:
        pass

False # DDD
FileExistsError # DDD
FileNotFoundError # DDD
FloatingPointError # DDD
FutureWarning # DDD

GGG G4 GGG

getattr # DDD
global # DDD
globals # DDD
GeneratorExit # DDD

HHH H4 HHH

hasattr # DDD
hash # DDD
help # DDD
hex # DDD

III I18 III

id # DDD
if # Ejecución condicional que encabeza una expresión booleana y un cuerpo de sentencias tras terminar la línea con dos puntos ':'.
import # DDD
input # DDD
int # DDD
isinstance # DDD
issubclass # DDD
iter # DDD

15] "if" # Code Snippet que muestra:
    if expression:
        pass

16] "if/else" # Code Snippet que muestra:
    if condition:
        pass
    else:
        pass

17] "ipdb" # Code Snippet que muestra:
    import ipdb; ipdb.set_trace()

ImportError # DDD
ImportWarning # DDD
IndentationError # DDD
IndexError # DDD
InterruptedError # DDD
IOError # DDD
IsADirectoryError # DDD

JJJ J0 JJJ

KKK K2 KKK

KeyboardInterrupt # DDD
KeyError # DDD

LLL L7 LLL

lambda # función anónima, para tareas simples, pequeñas y repetitivas, traducidas como una sola línea en el código.
len # DDD
license # DDD
list # DDD
locals # DDD

18] "lambda" # Code Snippet que muestra:
    lambda parameter_list: expression

LookupError # DDD

MMMM M7 MMM

map # DDD
max # función de biblioteca que toma más de un argumento. Su llamada a función devuelve el máximo de los valores enviados
memoryview # DDD
min # DDD

19] "mark/markdown" # Code Snippet que muestra:
# %% [markdown]

MemoryError # DDD
ModuleNotFoundError # DDD

NNN N8 NNN

next # DDD
nonlocal # DDD
not # Operador lógico.
NameError # DDD
None # DDD
NotADirectoryError # DDD
NotImplemented # DDD
NotImplementedError # DDD

OOO O7 OOO

object # DDD
oct # DDD
open # DDD
or # Operador lógico.
ord # DDD
OSError # DDD
OverflowError # DDD

PPP P9 PPP

pass # Ejecutar o continuar la ejecución sin hacer nada. Un 'pasapalabra'.
pow # toma dos argumentos: la base y el exponente, los cuales una vez asignado el valor matemático o simbólico que representan, pasan a ser los parámetros de la función pow.
print # DDD
property # DDD

20] "pdb" # Code Snippet que muestra:
    import pdb; pdb.set_trace()

21] "pudb" # Code Snippet que muestra:
    import pudb; pudb.set_trace()

PendingDeprecationWarning # DDD
PermissionError # DDD
ProcessLookupError # DDD

QQQ Q1 QQQ

quit # DDD

RRR R11 RRR

raise # DDD
range # DDD
repr # DDD
return # DDD
reversed # DDD
round # DDD
RecursionError # DDD
ReferenceError # DDD
ResourceWarning # DDD
RuntimeError # DDD
RuntimeWarning # DDD

SSS S14 SSS

set # DDD
setattr # DDD
slice # DDD
sorted # DDD
staticmethod # DDD
str # string. Cadena de caracteres que se convierte en un 'argumento'.
sum # DDD
super # DDD
StopAsyncIteration # DDD
StopIteration # DDD
SyntaxError # DDD
SyntaxWarning # DDD
SystemError # DDD
SystemExit # DDD

TTT T14 TTT

target # DDD
target_list # DDD
try # DDD
tuple # DDD
type # DDD

22] "try/except" # Code Snippet que muestra:
    try:
        pass
    except expression as identifier:
        pass

23] "try/except/else" # Code Snippet que muestra:
    try:
        pass
    except expression as identifier:
        pass
    else:
        pass

24] "try/except/else/finally" # Code Snippet que muestra:
    try:
        pass
    except expression as identifier:
        pass
    else:
        pass
    finally:
        pass

25] "try/except/finally" # Code Snippet que muestra:
    try:
        pass
    except expression as identifier:
        pass
    finally:
        pass

26] "try/finally" # Code Snippet que muestra:
    try:
        pass
    finally:
        pass

TabError # DDD
TimeoutError # DDD
True # Verdadero. Valor booleano (en minúsculas no sería tal valor)
TypeError # DDD

UUU U7 UUU

UnboundLocalError # DDD
UnicodeDecodeError # DDD
UnicodeEncodeError # DDD
UnicodeError # DDD
UnicodeTranslateError # DDD
UnicodeWarning # DDD
UserWarning # DDD

VVV V3 VVV

var # DDD
vars # DDD
ValueError # DDD

WWWW W7 WWW

while # DDD
with # DDD

27] "while" # Code Snippet que muestra:
    while expression:
        pass

28] "while/else" # Code Snippet que muestra:
    while expression:
        pass
    else:
        pass

29] "with" # Code Snippet que muestra:
    with expression as target:
        pass

Warning # DDD
WindowsError # DDD

XXX X0 XXX

YYY Y1 YYY

yield # DDD

ZZZ Z2 ZZZ

zip # DDD
ZeroDivisionError # DDD

BARRA___ _6 ___BAJA

30] "__main__" # Code Snippet que muestra:
    if __name__ == "__main__":
        pass

__doc__

__file__

__import__

__name__

__package__

CARACTERES ESPECIALES__________________________________________________________

>>> # prompt de Python. Indica que la consola de comandos está a la espera de recibir órdenes para darnos resultados inmediatos.
TAB # Genera cuatro espacios y jerarquiza secuencias y líneas de código.
\ # partir visualmente un código (misma línea)
| # DDD
' ' # DDD
" " # DDD
""" """ # DDD
# # DDD
$ # Modo de guión, una manera de usar el intérprete de Python junto con el modo en comandos '>>>'.
% # Operador módulo. Funciona con integers devolviendo el resto (lo residual, sobrante) de la división entre el primer y el segundo operando.
& # DDD
/ # DDD
() # parámetros de variables de ámbito local. 
= # DDD
+ # DDD
* # DDD
[] # DDD
{} # llaves que incluyen DDD.
: # DDD
... # DDD
- # DDD
_ # DDD

BARRA INVERSA MÁS LETRA_____________________________________________________________

\a # Bell.
\b # Retroceso, elimina el anterior caracter.
\f # Formfeed, traslada los caracteres siguientes una línea más abajo, respetando su emplazamiento sin entrar en jerarquía.
\n # Nueva línea, salto equivalente al 'Enter'.
\r # Carriage return, borrar todo lo anterior dentro de una delimitación DDD [todavía por concretar] DDD.
\t # Añadir tabulación o sangrado horizontal de 4 espacios.
\v # Añadir tabulación vertical
\' # Guarda una sola '. Es una manera de introducir caracteres de escape en un string o encadenado de texto.
\" # Guarda una sola ".
\» # DDD
\\ # Guarda una sola barra inversa "\"

COMBINACIONES CON OPERANDOS____________________________________________________

= # Operador de asignación. También operador matemático de equivalencia o igualdad.
== # Comparador. Operador que DDD.
<= # Menor o igual que.
>= # Mayor o igual.
!= # Operador que indica que no es igual.
+= # Sumar un número 'n' (a la derecha) a la expresión (de la izquierda).
-= # Restar un número 'n' (a la derecha) a la expresión (de la izquierda).
*= # Multiplicar un número de un lado por el de otro.
%= # Dividir un número de un lado por el de otro.
**= # Calcula el exponente desde la variable del lado izquierdo al valor del lado derecho.
//= # Calcula la división entera a la variable del lado izquierdo el valor del lado derecho.

BIBLIOTECA DE IMPORTACIONES____________________________________________________
Listado de PEP: https://www.python.org/dev/peps/

gasp: Graphics API for Students of Python.

-------------------------------------------------------------------------------
SUMA EN TOTAL
A16 + B11 + C9 + D11 + E11 +F14 + G4 + H4 + I18 + J0 + K2 + L7 + M7 + N8 + O7 + P9 + Q1 + R11 + S14 + T14 + U7 + V3 + W7 + X0 + Y1 + Z2 + _6 = 190