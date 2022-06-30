import asyncio                  # Módulo o librería de Python que viene con su propio script de funcionalidades/instrucciones para dejar respirar un poco entre cada ejercicio/actividad.
async def w8():                 # Dos funciones: 'async' y 'def' junto a la palabra clave (y variable) 'w8' (wait en inglés de la calle).
    await asyncio.sleep(0.5)    # Toda referencia a las líneas de código de nuestro script, es decir, de nuestro guion titulado '2-Práctica de iniciación' [como esta línea de código que contiene 'await asyncio.sleep(0.5)'], toda referencia dentro de los comentarios precedidos por el hashtag o la almohadilla ('#') será indicada con comillas 'simples' en vez de comillas "dobles".



## Imprimir en pantalla ##
print('1- IMPRIMIR PANTALLA EN TEXTO'), print()             # Observaciones: título del ejercicio contenido en un entrecomillado 'simple'. Daría lo mismo si fuera en un entrecomillado "doble" o """triple""" (si bien a esta última se le suelen dar otros usos más cercanos al comentario con almohadilla o hashtag '#').
print("Hello Darkness my old friend")                       # Definición: la función 'print': permite imprimir en pantalla lo que sea, en este caso todo el texto que esté entrecomillado. En esta versión de Python se debe incluir los paréntesis que envuelven a las comillas.
# print("Hello"), print("Darkness my old friend")           # Observaciones: la coma ',' lo que hará será cambiar a otra línea (igual que la tecla Enter cuando escribimos) la siguiente impresión, ocupándonos dos líneas. Las líneas de código cuyos comentarios digan algo como "Observación" o "Alternativa" se pueden borrar sus almohadillas y ejecutarlas que funcionarán correctamente. Lo que hará Python [el programa que estamos usando, siendo nuestro ordenador el dispositivo, la máquina o el sistema informático (Python no es un sistema)] en la línea de código comentada anterior será imprimir dos textos distintos, dos conjuntos de caracteres diferentes.
# Print("Hello Darkness my old friend")      
#                # Errores: las mayúsculas 'Print' por convención no se usan, empiecen o no al principio de una línea de código.
# print("Hello Darkness my old friend"):                    # Errores: Si le diésemos a la tecla 'Enter' en el script nos generaría una tabulación (equivale a cuatro espacios), una jerarquía contenida donde toda esta línea sería el encabezado y todo el cuerpo posterior presentaría cual lista de la compra las funciones, parámetros, argumentos o variables locales (variables contenidas dentro de una función y/o un encabezado) que contendría.
# print    ("Hello Darkness my old friend  ")               # Observaciones: Los espacios entre la función y el abre paréntesis no influyen en la ejecución de la instrucción. Los espacios dentro del entrecomillado sí quedarán reflejados, en este caso dos espacios.
# print """Hello Darkness my old friend"""                  # Errores: En versiones anteriores no era necesario el paréntesis. Ahora sí. Las comillas 'simples', "dobles" y """triples""" son lo mismo, si bien la última opción suele ser para cadenas de código largas, que ocupan varias líneas.
# print ("20250812941983411")                               # Observaciones: imprimirá un un número entero pero que es 'string' (cadena de caracteres) y no un 'int' (integer, número entero). La diferencia entre 'str' e 'int' radica en el tipo o la naturaleza de los caracteres introducidos, dado que el entrecomillado hace que su interior lo considere automáticamente string.
# print ("")                                                # Observaciones: imprimirá una línea entera en blanco al igual que si quitaras el entrecomillado. Útil para hacer separaciones de texto.
# print ('')                                                # Observaciones: la ejecución de la instrucción y el resultado mostrado sería el mismo que en la anterior observación a ésta.
# print ("""""")                                            # Observaciones: el triple entrecomillado realiza lo mismo que el entrecomillado 'simple' y "doble".
# print.                                                    # Errores: sintaxis inválida. Aquí no se cierra con ; que es habitual en otros lenguajes. Generalmente los sistemas de puntuación '.' ':' ';' '...' tienen su estructura y ciertas finalidades, si no, da error.
# print                                                     # Observaciones: No imprimirá nada. Se ejecutará la orden con éxito, pero no se nos mostrará el resultado en pantalla.
#                                                           # Observaciones: La almohadilla sirve para hacer comentarios que serán completamente ignorados por el programa.
print()                                                     # Un 'print()' sin más equivale visualmente a una separación de línea (deja una línea en blanco para que el texto devuelto en pantalla "respire").
# Vuelvo a colocar la almohadilla ('#') en los comentarios de las líneas de código de arriba por si se desea ejecutar la ordenanza errónea solo se tenga que borrar la primera almohadilla, conservando la segunda '#' dentro de cada línea de código, evitando así el error de que registre lo que antes era un comentario tras muchas tabulaciones en parte de un código ejecutable.
# A la hora de copiar y pegar partes de un código hay dos tipos de selección: está el lineal, que si arrastras el puntero cogerás toda la información incluida la que no aparece en pantalla (por limitaciones físicas del monitor doméstico promedio) y está el de recuadro, que realizará una selección cuadricular de los caracteres que se vean involucrados dentro del área dibujada. Para cambiar de un modo a otro DDD.
print(), print("______________________________________")    # Observación: imprimiré estos guiones bajos en pantalla para marcar una separación visual entre los distintos apartados que conforman el script (o guion) de códigos.



## Variables y asignación ##
print('2- CREAR UNA VARIABLE CON VALOR'), print(), asyncio.run(w8())        # En "('2- CREAR UNA VARIABLE CON VALOR'), print()," si quitásemos esa coma anterior a dicho 'print()' daría exactamente lo mismo (la impresión final mostrada en pantalla no variaría). Ocurre igual con las restantes funciones de color azul (azul si usas Solarized Dark como interfaz visual de Python [Acceso directo: Ctrl + K + T]).
nombre = "Me llamo Iñigo Montoya, tú mataste a mi padre, prepárate a morir" # Definición: 'nombre = ""' es una variable (con un valor) de "texto". Se crea otorgando un valor ya sea definido (defined = 'def') o a través de un operador de asignación con el símbolo de igual ('=').
print     ( nombre  )                                                       # Observaciones: la función 'print' imprimiría en pantalla el texto entrecomillado de arriba incluido entre esos paréntesis. Los espacios extra no afectan a la asignación, ni a las instrucciones ni a la ejecución de una función cualesquiera.
# nombre="1234..."                                                          # Observaciones: los espacios a ambos lados del igual dan lo mismo. No obstante si hay dos variables de texto con la misma asignación pero distinto contenido, si lo imprimimos (de ahí el print), solo mostrará la más reciente de todas, la última (en este caso '1234'). Esto se debe a que Python es un lenguaje débilmente tipado, interpreta automáticamente el tipo de dato que tiene dentro de la variable. Habría que indicar en la función que desempeñara nuestra variable si es un string, un integer, un float...
# print(nombre)                                                             # Observaciones: si eliminamos el hashtag de esta línea y la de arriba (y el espacio posterior que tienen también, no queremos crear tabulaciones y por lo tanto supeditaciones), nos imprimirá por un lado el texto entrecomillado del principio y por otro el texto que simplemente dice "1234...".
# nombre2 = "My name is Jeff"                                               # Observaciones: al ser una, llamémosla "etiqueta" distinta por ese '2', tendremos dos variables de texto distintas (cuyo contenido entrecomillado podría ser el mismo si quisiéramos).
# numero = "Me llamo Iñigo Montoya, tú mataste a mi padre..."               # Observaciones: como si quieres llamar a la etiqueta 'xjasduwewj'. Estás generando tu propio vocabulario personal y local (solo útil para este archivo .py salvo que se exportase a otro script).
# nombre_y_amenaza = "Me llamo Iñigo Montoya, tú mataste a mi padre..."     # Observaciones: el guion bajo permite crear variables compuestas de dos o más palabras para indexar mejor las denominaciones de nuestro código.
# nombre "Me llamo Iñigo Montoya, tú mataste a mi padre..."                 # Errores: sintaxis inválida. El signo '=' debe emplearse para establecer la creación de un "texto" de valor específico (letras y/o números).
# nombre me llamo Iñigo Montoya, tú mataste a mi padre...                   # Errores: sintaxis inválida. El entrecomillado es para escribir cualquier cosa que quieras. Además los espacios le hacen pensar al programa que estás invocando muchas funciones sin sentido propio.
# $1print = "Me llamo Iñigo Montoya, tú mataste a mi padre..."              # Errores: no puede empezarse el encabezado de una línea con caracteres raros (no alfanuméricos) ni con números ni con palabras reservadas, que son las 31 excepciones (como print, elif, while...) que tiene Python que no pueden usarse para menesteres como éste.
asyncio.run(w8()), print(), print("______________________________________") # Observación: invoco de nuevo la variable 'w8', anteriormente definida, para establecer un breve lapso de tiempo entre ejercicio y ejercicio sin que se ejecuten todos los ejercicios de golpe y sin que los inputs nos distraigan cuándo hay que pasar a la siguiente actividad de cuándo hay que introducir letras o números para no inducir al sistema a error dado que a muchos de los códigos de los ejercicios les falta esa parte de prever salidas no esperables básicas y establecer un retorno inmediato a la pregunta originalmente formulada hasta su correcta y concreta resolución.



## Format{} y concatenación ##
print('3- CONCATENACIÓN'), print(), asyncio.run(w8()),                              # Al parecer, si se deja esa coma al final de esta línea no afecta a la ejecución del código. Igual simplemente Python lo ignora y sigue con su flujo de ejecución.
name1 = "Carlos"                                                                    # Las variables de la izquierda no pueden sucederse en la misma línea separada por comas. Es decir, no puedo poner "Carlos, Tomás, Cisneros Abellán", porque serían tres argumentos, tres valores para una misma variable.
name2 = "Tomás"                                                                     # Porque si no sucede un error sintáctico de imposibilidad de asignar un valor literal.
#nombre1 = "Tomás"                                                                  # Observaciones: esta variable global (Ver ejercicio 29) tomará la asignación más cercana. Python leerá una asignación (el valor de texto Carlos) y luego la otra (Tomás), y si imprimimos en pantalla entre ambas variables nos aparecerían dos valores distintos. Pero si imprimimos después de haber asignado [de esta manera] dos textos distintos, solo mostrará el más reciente.
apellidos3 = "Cisneros Abellán"                                                     # Hay que cuidar que no repetir la misma denominación en aquellas variables susceptibles de pertenecer a trozos de código que luego en el futuro quisiéramos reutilizar. La máquina "olvida" los valores anteriormente dados [incluso dentro de un mismo ejercicio, obviamente, dado que son separaciones que hace el autor, no la máquina].
print(f"{name1} {name2} {apellidos3}")                                              # Concatenar consiste en unir dos variables, generalmente strings y/o integers. La f permite incrustar o interpolar mediante dobles llaves el nombre de la variable que queramos introducir (ejecutando los valores que les hayamos asignado).
# print(f{name1} {name2} {apellidos3})                                              # Errores: sin el entrecomillado la f no adquiere el poder de la incrustación. De hecho se puede incrustar lo que se desee en el valor de una variable cualesquiera.
print("Hola me llamo {} {} y de apellidos {}".format(name1, name2, apellidos3))     # El método 'format' va introduciendo posteriormente (por orden) las variables (anteriormente asignadas y por lo tanto definidas) en los huecos sin {incrustar}.
# print("name1 + name2 + apellidos3")                                               # Alternativa: dará como resultado 'CarlosTomásCisnerosAbellán'. Con un espacio entrecomillado " " añadido entre medias de las variables se concatenarían esos tres strings correctamente. También como medida estética se puede separar/espaciar con guiones el texto que queramos mostrar dentro de esas "dobles comillas".
# print(name1, name2, apellidos3)                                                   # Alternativa errada: realmente esta línea de código no es una concatenación, son variables usadas como parámetros (lista de la compra) a imprimir, de ahí que esas variables parezcan concatenadas, pero en realidad están siendo ejecutadas por separado, mostrándonos un resultado similar al buscado pero no a la idea inicial o intencionalidad deseada por parte del usuario.
asyncio.run(w8()), print(), print("______________________________________")         # Observación: si no cerrásemos el entrecomillado nos saldría «EOL while scanning string literal», lo cual significa que ese End Of Line es un error sintáctico porque el set (o cadena) de caracteres que tenían que ocurrir en una línea específica no fueron encontradas o halladas antes del Final De la Línea.



## Lista y tupla ##
print('4- TIPOS DE LISTA'), print(), asyncio.run(w8())                                                  
lista_cambia = ["el número", "es", 27, "27", "en texto"]                                                # La principal diferencia visual entre ambas es que en una se usan paréntesis y en la otra corchetes. Por lo demás son muy idénticos. Las variables que vayamos escribiendo serán variables locales. Es decir, una vez se ejecute la variable, ésta habrá cumplido con su cometido final. Si incorporásemos la función 'return', sí que se podría aprovechar las funciones una vez escritas para cualquier invocación o llamada posterior. (Sobre variables y funciones locales y globales ver el ejercicio '29 FUNCIONES LOCALES Y GLOBALES').
tupla_no_cambia = ("el número", "es", 27, "27", "en texto inmutable")                                   # Porque si cambiase el valor de tupla (los datos en su interior), sucedería un error sintáctico de imposibilidad de asignar un valor literal. Se cambian por ejemplo haciendo DDD.
print((lista_cambia), type(lista_cambia))                                                               # Esa forma de inclusión permite colocar el tipo de lista al lado de la misma variable en vez de imprimirnoslo en una línea aparte.
print((tupla_no_cambia), type(tupla_no_cambia))                                                         # Los paréntesis más internos suceden primero y después el resto de cajones/compartimentos inmediatamente más externos (en el mismo nivel de jerarquización). Por ello nos imprimirá el tipo de función que es irremediablemente.
# print(lista_cambia), print(tupla_no_cambia), print(type(lista_cambia)), print(type(tupla_no_cambia))  # Observaciones: Sería lo mismo que la instrucción ejecutada pero ocupando una línea cada una (4 en total). Mostraría las dos variables impresas y su respectiva identificación después [mutable] (inmutable).
# tupla_no_cambia = ["el número", "es", 27, "27", "en texto"]                                           # Observaciones: corchetes y paréntesis son las diferencias entre ambos tipos de lista [mutable] (inmutable).
# tupla-no-cambia = ("el número", "es", 27, "27", "en texto")                                           # Errores: el guion se seguirá considerando un operador matemático de resta en el intento de crear una variable con dicho signo incluido.
# print[lista_string], print[type[lista_string]]                                                        # Errores: "'builtin_function_or_method' object is not subscriptable".
# print((lista_cambia)type)                                                                             # Errores: sintaxis inválida. está definiendo la nada y además mal colocada.
asyncio.run(w8()), print(), print("______________________________________")                             # Observación: pese a ir seguidos por comas, esos dos prints ejecutarán un salto de línea y el texto de guiones bajos en otra, no sin antes esperar un poquito porque primero se ejecuta la variable 'asyncio' (asincronización) que pone en marcha la función 'await' dentro de 'w8'.



## Diccionario ##
print('5- DICCIONARIO'), print(), asyncio.run(w8()) 
diccionario = {                                 # Colección de datos que permite tener una clave y un valor. A la izquierda la variable 'diccionario'. A la derecha su valor, en este caso desarrollado abajo entre llaves.
    "nombre": "Jason",                          # Un bloque de instrucción desarrollado dentro de un encabezado iniciado por el abrir llave '{'. Las llaves indican pues clave y valor separados por comas con cada salto de línea que se haga en este documento Json. Un documento Json [JavaScript Object Notation; Notación de Objeto de JavaScript] es un formato de texto sencillo para el intercambio de datos. Se trata de un subconjunto de la notación literal de objetos de JavaScript y se considera un formato independiente del lenguaje.
    "valor dado por los dos puntos":"equis"     # Estos cuatro entrecomillados ofrecidos como argumentos se mostrarán tal cual, sin jerarquía alguna cual lista de la compra. Si tabulásemos una o má veces esta línea de código no pasaría nada respecto al resultado impreso en pantalla.
}                                               # La raya vertical encima de '}' indica la supeditación (la jerarquía) de esas líneas de código a la parte o el trozo del código desde donde se origina.
print(diccionario), print(type(diccionario))    # Otra tipología distinta: 'dict.', que actúa como diccionario interno del código (o de la función o variable que perteneciese al cuerpo de un encabezado concreto).
# }, print(diccionario)                         # Errores: el nombre de diccionario no estará definido si intentamos imprimir la variable justo tras el cierre de chunk o colección de datos incluidos como valores en la clave 'diccionario'.
# "nombre": "Jason"                             # Error asociado: Si le falta la coma en el salto de línea (tras 'Jason')...
# "valor dado por los dos puntos":"equis"       # Error asociado: ... nos señalará la sintaxis inválida en el siguiente ':' que haya en vez de indicarnos que falta ahí una dichosa coma, cosas del flujo de ejecución del programa supongo.
asyncio.run(w8()), print(), print("______________________________________")     ## Escribir la variable 'asyncio.run(w8))' de esta línea ejecutará las instrucciones anteriormente definidas de arriba del todo de nuestro script. La clave está en la función 'await', que hace que el programa espere un tiempo determinado antes de pasar a ejecutar la siguiente instrucción.



## Conversión de tipo número a string ##
print('6- CONVERSIONES'), print(), asyncio.run(w8())
priest = "Wololooo"             # Esto es un operador de asignación, siendo el valor un texto entrecomillado (guiño al Age of Empires II) y la variable 'priest', sacerdote en español.
numerito = str(69)              # Recordemos que Python es un lenguaje débilmente tipado que interpretará automáticamente el tipo de dato de dentro de la variable. De ahí que siga pintado el número en color distinto al string o al "texto".
print(priest + " " + numerito)  # imprimir: variable 1 ("texto") + espacio + variable 2 ('número').
# numerito = 69                 # Errores: ese integer no sería un string, para ello hay que convertir ese dato de la manera impresa, para que salga como "69".
# numerito = int(69)            # Errores: nos saldrá un error de tipología, diciendo que solo puede concatenar strings (cadenas) y no números enteros como strings.
# numerito = float(69)          # Errores: al intentar meter un número decimal '69.0' nos sucederá lo mismo que antes. La tipología eso sí cambiaría en cada una de ellas según la conversión que le preceda al paréntesis si imprimimos únicamente el 'numerito'.
asyncio.run(w8()), print(), print("______________________________________")



## Sumas, restas, multiplicaciones y divisiones ##
print('7- OPERADORES ARITMÉTICOS (MATEMÁTICOS)'), print(), asyncio.run(w8()) 
numero1 = 77                        # Operador matemático 1. El = funcionaría como operador de asignación, habiendo siete en total para este apartado 7. Y no, no se pueden disponer entre comas. Cada operador (cada variable) debe encabezar siempre una nueva línea (creo, igual me equivoco).
numero2 = 45                        # Operador matemático 2. No puede coincidir la misma denominación del operador anterior (y llamarlo otra 'vez numero1') o la variable global omitiría el valor anteriormente dado, mostrando solo el resultado del valor más reciente.
resta = numero1 - numero2           # Operador de asignación que reúne a los dos operadores matemáticos previos (matemáticos porque contienen números con los cuales luego se harán operaciones aritméticas), que son variables con valor definido. Si se hiciera la resta al revés (numero2 {45} - numero1{47}), daría '-32'.
antirresstta = numero1 + numero2    # Debes colocar las variables de asignación antes de la orden de impresión (esta línea después del 'print' sería irreconocible para el programa). Nosotros solemos leer el código de arriba a abajo, pero el sistema sigue el llamado flujo de ejecución.
multipl=numero2*numero1             # El flujo de ejecución no funciona buscando variables a posteriori de la instrucción dada (en este caso, 'print'), la ejecución se interrumpe para buscar en los operadores de asignación de líneas anteriores. Los espacios puedes quitarlos o añadir más si quieres, no afectará a la operación ni a su resultado.
divis = numero1/numero2             # El resultado dará un número con decimal ('float'), mostrando hasta quince cifras después del punto (un 'float' nunca se escribe con comas ni abajo ',' ni arriba ·'·, sino con punto '.').
resto = numero1%numero2             # Esos dos números se dividirán y lo que sobre se guardará en este operador de asignación. Recuerda que el 'print' no está diseñado para que prosiga con la división, en busca de decimales.
print(f"LOS NÚMEROS SON {numero1} y {numero2}. CALCULADORA:")                                                       # Encabezado para mostrar en pantalla los números valorados (modificables al llamar a las variables como incrustaciones {}, siempre mencionados antes por la literalidad 'f').
print(resta), print(f"La resta es {resta}")                                                                         # Ambos resultados dan lo mismo, el primero tomando directamente la variable, el segundo incrustando la variable en la doble llave mediante la literalidad (de 'f'), lo cual nos permite introducir ese texto entrecomillado como acompañante para que la respuesta sea más humana.
print(f"La suma es {antirresstta}"), print("La multiplicación es: ", multipl), print (f"La división es: {divis}")   # Puedes llamar a la variable con la categoría accidental que te dé la gana ("antirresstta - Guillermo de Ockham" por ejemplo). Estos tres resultados no aparecerán en la misma línea en la consola pese a estar separados por comas. Muestro distintas maneras de imprimir prácticamente lo mismo.
print(f"El resto de la división {numero1} y {numero2} es:", resto)                                                  # ¿Por qué el resto es 32? Porque dividir 77 entre 45 te da 1 y de resto por dividir 32. Si dividieses 100 entre 2, el resto sería 0 porque daría exacto. Y si fuera 2 entre 100 te daría 2 como resto, porque sería una división menor que la unidad.
asyncio.run(w8()), print(), print("______________________________________")



## Lista de operadores de asignación ##
print('8- OPERADORES DE ASIGNACIÓN'), print(), asyncio.run(w8()) 
edad=55                                 # Operador de asignación (matemático al ser un número).
edad +=10                               # Sería lo mismo que poner edad = edad + 10. Es añadir un número a la expresión de la izquierda 'edad'.
print(edad)                             # Imprime la variable 'edad' junto con los operadores de asignación asociados a dicho término (o denominación).
"""OTROS OPERADORES DE ASIGNACIÓN"""    # No podría poner todo el texto siguiente con el triple entrecomillado, porque reconocería algunos caracteres y funciones (salvo que las pongas en mayúsculas, al igual que las palabras reservadas) lo cual haría saltar múltiples errores. Al no imprimir estas comillas triples, simplemente es DDD, como "código no ejecutable que no es # comentario".
# = Operador de asignación. También operador matemático de equivalencia o igualdad.
# == Comparador.
# <= Menor o igual que.
# >= Mayor o igual.
# != Operador que indica que no es igual.
# += Sumar un número 'n' (a la derecha) a la expresión (de la izquierda).
# -= Restar un número 'n' (a la derecha) a la expresión (de la izquierda).
# *= Multiplicar un número de un lado por el de otro.
# %= Dividir un número de un lado por el de otro.
# **= Calcula el exponente desde la variable del lado izquierdo al valor del lado derecho.
asyncio.run(w8()), print(), print("______________________________________")



## Operadores +- ##
print('9- OPERADORES DE INCREMENTO Y DECREMENTO'), print(), asyncio.run(w8()) 
year = 2025         # 'year++', 'year--', '++year' y '--year' son operadores cuya sintaxis no funciona en Python (en otros lenguajes puede). year +=1 y year -=1 sería la forma correcta de hacerlo.
year = year+1       # Esta variable condicionará a la otra variable, incrementando su valor numérico en uno.
print(year)         # Si ahora imprimiésemos year, nos saldrá 2026 en lugar de 2025, porque le hemos incluido un operador de incremento a posteriori.
year = 4 - year     # El resultado de este pre-decremento sería -2022, porque va antes de la variable y ello convierte a 'year' en un número negativo por ese guion de resta (4 - 2026 = +4 -2026).
print(year)         # 4 + year sería un preincremento, y daría 2030.
print(), print("______________________________________") 



## Input strings e integers ##
print('10- ENTRADA Y SALIDA DE DATOS'), print(), asyncio.run(w8())
input ("Pulse Enter para continuar ")                                                       # Resulta que 'Enter' es la única tecla del teclado que en verdad permitiría continuar la ejecución del código. Le meto un espacio al final del entrecomillado para separar la respuesta del usuario respecto al texto imprimido en pantalla.
#input("")                                                                                  # Daría el mismo resultado que input(), generando un salto de línea. Se consigue el mismo efecto usando la expresión "\n" [o función, vete a saber cómo demonios llaman a eso realmente]. Sin el 'input' ejecutaría las órdenes de cada ejercicio nuestro, realizando los resultados de golpe y porrazo (otra cosa es que dichos resultados nos sean mostrados. Para ello, usar la función 'print' y tal).
#input(" ")                                                                                 # El primer caracter de la línea lo ocuparía un espacio. Todos los espacios que introduzcamos dentro del entrecomillado serán impresos como caracteres vacíos, existiendo en/ocupando una posición determinada. Cuatro espacios equivalen a una tabulación.
maruja = input("¿Tú no eres el hijo del hermano de la Paqui? ¿Cómo te llamabas?: ")         # la consola (cmd) o Símbolo del Sistema esperará a que nosotros le respondamos de alguna manera con el teclado. No devolverá ninguna salida una vez introducido nuestros datos.
print(f"Uyyy pues si que estás goordo {maruja}")                                            # Podríamos poner 001010101 o darle a la tecla 'Enter' sin responder en absoluto, que al sistema le daría igual. Por eso podríamos añadirle str (argumento) dentro de la doble llave y la variable 'maruja' entre paréntesis, para limitar la capacidad de trolleo del usuario y evitar que su nombre comience por un número.
asyncio.run(w8())
print("«Ves como la maruja no te deja en paz. Todavía tiene otra cuestión que hacerte»")    # Habría que añadir una función 'else' en caso de considerar ciertos outputs (salidas) como no correctas o esperables por un ser humano corriente.
asyncio.run(w8()), asyncio.run(w8())
añitos=input("¿Y cuántos añitos dices que tienes?: ")                                       # Ahí debemos contestar "27" en lugar de "veintisiete" o simplemente pretando 'Enter' como respuesta, porque la función definida que interactuará con el resultado que le proporcione al usuario tiene 'int' delante de la incrustación, marcando la tipología necesaria para realizar la operación matemática que lleva dentro. Necesitaríamos alguna función condicional para reconducir posibles respuestas o conductas erróneas previstas por el programador/a.
asyncio.run(w8())
print(f"¡UUUUY! Pues yo te echaba {int(añitos) + 2} años por lo menos jaja, adiosito!")     # 'añitos + 2' nos daría error porque el dato introducido sería un string y para ello debemos convertir el formato de la respuesta a nuestra edad en integer ('int), para así poder hacer esa suma entre números enteros (de base 10). Para ello solo debemos añadirle 'int' dentro de la doble llave y un paréntesis a 'añitos'.
asyncio.run(w8())
print("«La señora se aleja por fin.»")
asyncio.run(w8()), print(), print("______________________________________")



## If, else, elif ##
print('11- LAS CONDICIONALES IF, ELSE Y ELIF'), print(), asyncio.run(w8()) 
color = "azul"                                              # Operador de asignación gracias a ese '=' entre una variable (izquierda) y su valor ("texto").
if color == "azul":                                         # Esos ':' hace entrar en jerarquía la siguiente línea (o añadiendo una tabulación manualmente, cada raya sería un rango). '==' indica comparador.
    print("El color es azul.")                              # Al coincidir ambos valores de "texto", la condición se cumple.
    asyncio.run(w8())
else:                                                       # Si el valor introducido a la variable color fuese "verde" por ejemplo, imprimiría la otra opción de abajo.
    print("El color no es azul.")                           # O la respuesta es una (if) o la respuesta es otra (else), básicamente.
color2 = "rojo"                                             # Ahora con otro ejemplo ('color2'), esta vez con intervención del usuario (función 'input').
color2 = input("Adivina cuál es mi color favorito: ")       # Si no lo delimitamos con 'str' (cadena de caracteres), podríamos introducir números (integers, enteros) también en esa respuesta.
if color2 == "rojo":                                        # La variable color2 ha sido definida con un valor que ha de coincidir exactamente en esta condición.
    print("Exacto, como el color de mis ojos {:v")          # Enhorabuena.
else:                                                       # Una curiosidad sobre 'else' es que DDD.
    print("Ese no, sorry.")                                 # Si haces doble clic en el espacio que hay entre la línea de código y este comentario, aparecerá resaltado una serie de puntos centrales '···' que simboliza el número de caracteres de espacio (o el número tabulaciones, que cada una equivale a 4 espacios seguidos) que hay, por si te interesa borrar esos excedentes de espacio en el futuro para el menester que sea.
    asyncio.run(w8())
    print("Te daré una pista, empieza por \"r\", ojo.")     # La barra inversa con comilla es para introducir las comillas anulando su valor de función, dejándolas como parte del texto.

print(), asyncio.run(w8()), asyncio.run(w8())               # Estaría bien crear una función de retorno a la misma pregunta de antes o a otra pregunta distinta, dependiendo de nuestra intención de seguir insistiendo o pasar a otra cosa.

color3=str(input("A ver una vez más. Mi color favorito: ")) # Esta fórmula es necesaria para que la variable dependa de lo que escriba el usuario. Si esta línea fuese un 'input' normal, siempre nos imprimiría "Alright" da igual el color que escribiésemos.
if color3 == "rojo":
    print("Alright!!")                                      # Esta parte de la conversación, en caso de que el usuario escriba rojo por primera vez, no tendría sentido en la vida real. Por ello no estaría mal incorporar justo debajo de la línea donde digo "# Enhorabuena" la función 'break' para romper la condición previamente si el resultado ya fue correcto a la primera.
    asyncio.run(w8())
else:
    print("Bueno... ser daltónico no es un gran problema hoy día"), asyncio.run(w8())   # Comentario asociado: Justo abajo dejaré una línea de espacio vacío en el código, como forma visual de representar otros ejemplos y alternativas dentro de una misma actividad. Si pusiese este comentario así sin más... #DDD meter aquí un await en lugar de input.
                                                                                        # Comentario asociado: ...generaría tantas tabulaciones como fuesen necesarias hasta ocupar el lugar de comentario que quisiera. Y visualmente queda como el culo vamos. Generalmente en vez de hacer estas cosas haré un simple 'print()' y ya está.
asyncio.run(w8())
dia=int(input("Y bien, dime antes de marcharme, ¿a qué día de la semana estamos? "))    # La función await podría introducirse para expresar la impaciencia por tiempo de espera de la otra persona ante nuestra tardía respuesta.
if dia == 1:                                                                            # 'if' siempre al principio.
    print("Odio los lurnes")
elif dia == 2:                                                                          # 'elif' ('else + if') siempre en medio como otros condicionantes entre el 'if' inicial y el 'else' final.
    print("No están mal los marnes")
elif dia == 3:                                                                          # Evita los anidamientos de if, que sería una escalada jerárquica en diagonal derecha demasiado fea y amplia.
    print("Xcoles, se llama xcoles, causa pánico en la ciudad")
elif dia == 4:                                                                          # Estaría bien incluir la variable escrita por si el usuario no introduce número, el código se ejecutase correctamente.
    print("Juernes maldita sea SIIIUUUUHHH!")
elif dia == 5:                                                                          # Curiosidad: si pulsas Alt + flechas de arriba y abajo trasladarás la línea de código entera.
    print("Ya es viernes madafacas")
else:                                                                                   # 'else' siempre al final.
    print("Se nota que ya es fin de semana eh!")                                        # Si el usuario escribiese un 8 o superior, podríamos incorporar la función 'while' para mantener el bucle de seguir preguntando tras decirle en plan "si solo hay 7 días en la semana", o programar la manera de que por escrito también se cumpla, duplicando cada respuesta numérica por su homóloga escrita.
asyncio.run(w8()), print(f"Bueno {maruja}, hasta luegorrr"), asyncio.run(w8()), print(), print("______________________________________")



## For, if, else ##
print('12- EJECUCIONES ALTERNATIVAS: PAR E IMPAR'), print(), asyncio.run(w8()) 
for contador in range(0,11):            # Muestra los números pares e impares del uno al diez.
    if contador%2 == 0:                 # Divide la condición dependiendo de si el resto es cero o es uno. Un '1' nos llevaría a que los impares estuviesen arriba y los pares abajo.
        print(f"{contador} es par")     # La literalidad de "f" no tiene que estar obligadamente unida a la función 'print', ambas pueden ir por separado.
    else:
        print(f"{contador} es impar")

print(), asyncio.run(w8())

number1 = int(input("Introduce un número y te diré los impares e impares hasta llegar a él: ")) # En este caso es el usuario el que debe introducir un número entero positivo.
for number1 in range(int(f"{number1}")):                                                        # Otra manera avanzada de eliminar el límite superior de la ecuación.
    if number1 % 2 == 0:                                                                        # El resto necesario para calcular si es par o impar.
        print(f"{number1} es par")  
    else:
        print(f"{number1} es impar")

print(), asyncio.run(w8())

number2 = int(input("Ahora solo el número que tú me digas: "))      # Ahora solo imprimir el número que nos indique el usuario y decir si es par o impar.
if number2 % 2 == 0:                                                # Para ello se elimina la función de 'range' usada con anterioridad, dado que queremos solo calcular un número.
    print(f"{number2} es par")
else:
    print(f"{number2} es impar")

# El bucle for nos permite recorrer todos los elementos de una lista de manera secuencial y elegante, donde en vez de hacer print 365 veces para cada día de un año no bisiesto, se puede hacer simplemente:
# año = ['1 Enero', '2 Enero', '3 Enero' ...
# '14 Abril', '15 Abril' ...
# '30' Diciembre, '31 Diciembre']

# for dia in año:                   # Y ya estaría, los 365 elementos manualmente metidos (o utilizando ciertas librerías/módulos si ya están fabricadas para tales menesteres) se imprimirían de manera sencilla y elegante.
#    print(año)
asyncio.run(w8()), print(), print("______________________________________")



## If, else, if not ##
print('13- OPERADORES LÓGICOS EN CONDICIONES MÚLTIPLES'), print(), asyncio.run(w8()) 
edad_minima=18
edad_maxima=65
edad_oficial=int(input("Di tu edad expresada en números y te leo el futuro laboral que te espera: "))
if edad_oficial >= 18 and edad_oficial <= 65:                           # 'and' es un operador lógico que une esas dos condiciones que en este caso forman una especie de rango artificial, poniendo límites entre dos extremos buscando esa franja de edad concreta.
    print("Enga a currar! #todossomoshacienda")
else:
    print("Pos sigue estudiando!")

asyncio.run(w8()), print()

pais= "España"                                                          # Para la variable pais, asignamos "España", la cual debería imprimirnos la primera opción.
if pais == "México" or pais == "España" or pais == "Colombia":          # 'or' y 'and' permiten unir dos o más condiciones en una misma sentencia.
    print(f"{pais} es un país de habla hispana")
else:
    print(f"{pais} no es un país de habla hispana")
pais2= "Rusia"                                                          # Para la variable pais2, al ser Rusia nos dará la primera opción.
if not(pais2 == "México" or pais2 == "España" or pais2 == "Colombia"):  # 'if not' debe involucrar en paréntesis el objeto al cual le afectará dicha negación.
    print(f"{pais2} NOPE, no es un país de habla hispana")              # Recuerda que si pongo en la incrustación {pais3}, estará escogiendo el valor que no es "Colombia", dado que estaré escogiendo la variable incorrecta "pais3".
else:
    print(f"{pais2} YEP, sí que es un país de habla hispana")
pais3= "Colombia"                                                       # No es necesario agrupar las variables pero sí introducirlas antes de ejecutar instrucciones que las invoquen o llamen.
if pais3 != "Mexico" and pais3 != "España" and pais3 != "Colombia":     # '!=' es el cuarto operador (junto con 'and', 'or', e 'if not') que comprueba si el país es diferente a cada uno de los ahí señalados.
    print(f"{pais3} NOPE, no es un país de habla hispana")
else:
    print(f"{pais3} Sí, son de habla hispana (y qué cumbias macho)")
asyncio.run(w8()), print(), print("______________________________________")



## Range, if, for, else, while, break ##
print('14- BUCLES Y RANGOS'), print(), asyncio.run(w8())
rango = range(3), print(range)          # Mostrará "class range". Y si le pongo un 'type' delante de range me sale "class type", no sé por qué, debería salir un rango del 0 al 3 aún sin ponerle el cero seguido de una ','.
contador=0                              # Da igual el valor que le concedamos a esta variable, al parecer nunca será realmente llamada. Se podría omitir esta variable de hecho.
resultado  =0                           # No obstante el valor que le añadamos a esta variable sí afectará a la impresión (al 'print') final. Los espacios entre operadores de asignación dan lo mismo
for contador in range(-1,4):            # 'for' e 'in' permiten la combinación de hacer un bucle con una variable en un rango/lista... El rango irá del -1 al 3. Los rangos no van en plan del 0 al veinte "0-20", sino "0, 20" o "0,20", dado que los decimales van con punto "0.20".
    print("Voy por el "+str(contador))  # El string (la cadena de texto "Voy por el " solo puede concatenar otro string, al ser range un conjunto de integers, de ahí que la conversión sea necesaria/menester.
    resultado=resultado+contador        # Esto permite sumar todos los números dentro del rango siendo el valor de la variable resultado cero. "resultado += contador" nos daría exactamente lo mismo.
print(f"El resultado es {resultado}")   # -1 +0 +1 +2 +3 +4 = 5. Recuerda meter un espacio antes de la incrustación o saldría "El resultado es5".
asyncio.run(w8())
numero_usuario = int(input("¿De qué número quieres la tabla de multiplicar?: "))    # Ejemplo con el bucle 'for' y las tablas de multiplicar.
if (numero_usuario) < 1:                                                            # Si lo ponemos así en lugar de >= 1, así nos evitamos tener que poner la función 'else'.
    numero_usuario = 1                                                              # De esta manera si el usuario introduce un número menor que uno, en lugar de dar error al menos dará la tabla del uno.
print(f"\nTabla de multiplicar del {numero_usuario}")                               # Incrustación sencilla a partir del input tecleado por el usuario. '\n' hará un salto de línea conservando la funcionalidad de la instrucción aunque la pusiésemos a mitad o al final, haciendo el salto en un diferente lugar, claro está.
for numero_tabla in range (-3,11):                                                  # Por aquí solo aparece mencionado el valor de la tabla cogiéndonos un solo número de todo ese rango. Cualquier número menor de uno nos dará la tabla del uno al diez, así que no calculará números negativos. No obstante ante números mayores que 1 comenzará a multiplicar por el -3.
    if numero_usuario == 69:                                                        # Condiciones extra que podemos añadir, produciendo un resultado concreto como ese de ahí o para otros rangos que se podrían considerar "prohibidos" para la tarea que se pretende realizar.
        print("Guarro")                                                             # Si lo dejásemos así, multiplicaría el 69 por cada número del rango con un encabezado que dijese "Guarro".
        break                                                                       # Con la estructura 'break' romperíamos el bucle inmediatamente, dejando un solo mensaje de advertencia sin multiplicación alguna para el número "69".
    print(f"{numero_usuario} x {numero_tabla} = {numero_usuario * numero_tabla}")   # Importante: las incrustaciones pueden interactuar y operar entre sí dentro de una misma doble llave.
else:                                                                               # De esta manera cuando termina la iteración (el recorrido), nos mostrará ese mensaje final.
    print("Tabla finalizada. Soy una máquina"), asyncio.run(w8())

asyncio.run(w8()), print()

contador = 95                                   # No me toma el valor del "contador" usado en el ejercicio anterior. Al parecer no es necesario romper el binomio variable-valor una vez que se ha invocado y realizado dicha instrucción con anterioridad (siempre y cuando no se hubiese anulado por el motivo que fuere).
while contador <= 100:                          # El bucle 'while' es una estructura de control que itera la ejecución de unas instrucciones hasta que la condición deja de cumplirse. Debe contener además de un bloque de instrucciones, un actualizador del contador, si no el loop (las vueltas) serían infinitas.
    print(f"Estoy en el número: {contador}")    # Irá del 95 al 100. No es necesario poner 101 en el 'contador' porque hemos puesto menor o igual a 100, así que el programa continuará hasta la centena.
    contador +=1                                # Lo mismo que "contador = contador + 1".
contador=90                                     # Misma denominación de variable, distinto valor, distintos resultados en sus distintas ejecuciones. Todo correcto.
muestrame = str(0)                              # para hacer una cadena de caracteres a la sucesión de números. El primer número que saldrá será ese cero, y después el primer nº del contador, 90, y luego la sucesión hasta cien.
while contador <= 100:                          # "while valor < 1 or valor > 6", esta condición es un ejemplo de cómo pediríamos un número
    muestrame = muestrame + ", " +str(contador) # Esta concatenación permite que los resultados se muestren entre comas muy seguidamente en la misma línea
    contador = contador + 1                     # Lo mismo que "contador +=1".
print(muestrame)                                # Si no, no veríamos este segundo resultado puesto entre comas.
asyncio.run(w8()), print(), print("______________________________________")



## contador y operadores de asignación delimitadores ##
print('15- MOSTRAR CUADRADOS DE LOS PRIMEROS 20 NÚMEROS NATURALES'), print(), asyncio.run(w8())
contador=0                                                  # Valor del número por el cual empezaremos: cero.
while contador <= 20:                                       # Límite superior menor o igual a 60.
    cuadrado = contador*contador                            # No se usa '*=' porque eso multiplicaría la variable cuadrado con la de contador, y queremos que esta segunda variable se multiplique por sí misma.
    print(f"El cuadrado de {contador} es {cuadrado}")       # También podríamos poner contador*contador dentro de la segunda doble llave como operación entre incrustaciones.
    contador +=1                                            # Al ser un bucle 'while', es necesario que avance o se quedaría en el primer valor ('0') para siempre.
for numero in range(21):                                    # Misma operación con 'for' pero más breve. El programa interpreta del 0 al 61 al no indicar el límite inferior del rango.
    cuadrado = numero*numero                                # 'numero' está definido en esta instrucción concreta para el rango de la línea anterior
    print(f"el cuadrado de {numero} es {numero*numero}")    # Como decía antes, es igual a poner es el equivalente a poner "{numero} es {cuadrado}". Las incrustaciones varían, pero no son variables.
asyncio.run(w8()), print(), print("______________________________________")



## input, while, if y elif ##
print('16- EL JUEGO DE LOS DADOS'), print(), asyncio.run(w8())
valor = int(input("Escribe un número del 1 al 6: "))
while valor < 1 or valor>6:                             # Colocando ese rango, si el usuario lanza un número que no esté comprendido entre el 1 y el 6 (porque <=1 y >=6 nos dejaría con un dado de cuatro caras, del 2 al 5) imprimirá eso.
    print("del 1 al 6 illo")
    valor = int(input("Introduce un nº del 1 al 6: "))  # Lo mejor de esto es que es la misma frase de antes, solo que este operador de asignación se encuentra dentro de la condición. De esta manera, podemos equivocarnos cuantas veces queramos, que nos seguirá haciendo la misma pregunta hasta que acertemos.
if valor == 1:
    print("Menudo ojo, un uno")
elif valor == 2:
    print("Pim pam, un dos")
elif valor == 3:
    print("El señor del tres")
elif valor == 4:
    print ("Un cuatro")
elif valor == 5:
    print ("Por el culo te la hinco")
elif valor == 6:
    print ("Menuda chorra has tenido con el seis")
asyncio.run(w8()), print(), print("______________________________________")



## conversión integers a string haciendo operaciones matemáticas ##
print('17- LA CALCULADORA HUMANA'), print(), asyncio.run(w8())
print("Voy a usar todas las operaciones aritméticas entre los dos números que me des"), print()
nº1=int(input("Introduce un número: "))
nº2=int(input("Introduce otro número: "))
print("Suma: " + str(nº1+nº2))
print("Resta: " + str(nº1-nº2))
print("Multiplicación: " + str(nº1*nº2))
print("División: " + str(nº1/nº2))
print("Suma: " + str(nº1+nº2))
asyncio.run(w8()), print(), print("______________________________________") # Si subiera estos prints a la línea anterior separándolos con más comas, no habría un enter de separación respecto a la última instrucción.



## Número aleatorio entre el rango de un número pequeño y otro mayor ##
print('18- DOS NÚMEROS RANDOM'), print(), asyncio.run(w8())
num1 = int(input("Introduce el primer nº: "))
num2 = int(input("Introduce el segundo nº [que sea más grande que el anterior]: "))
if num1<num2:
    for contador in range (num1+1), (num2+1):       # Para incluir el rango introducido por el usuario hay que sumarle +1 entre paréntesis
        print(contador)                             # Si al final de cualquier condición ('if, for, else, while...') no imprimes ('print'), no te saldrá el resultado en pantalla.
else:
    print("El número 1 debe ser menor al número 2")
asyncio.run(w8()), print(), print("______________________________________")



## Tablas de multiplicar de golpe ##
print('19- MOSTRAR LAS DOCE TABLAS'), print(), asyncio.run(w8())
input("Haga los honores. Enter para mostrarlas en su plenitud:")
for cabecera in range(1, 13):
    print("··································")                 # Separación visual.
    print(f"Tabla del {cabecera}")                              # ¿Por qué no es necesario convertir la incrustación en integer? Porque "cabecera" ha sido definida como un rango de números. Si la hubiésemos definido con texto entrecomillado, sería string, una cadena de caracteres.
    print("··································")
    print()                                                     # Comentario asociado: Mismo resultado que el salto de línea '\n' (eso sí, tiene que estar impreso para verse).
    for numero in range(1,13):
        print(f"{numero} x {cabecera} = {numero * cabecera}")   # Multiplicación de incrustaciones (método visto con anterioridad). Si quisiéramos cambiar la naturaleza de estas dobles llaves habría que poner entre paréntesis 'str'. No obstante si posamos el puntero del ratón encima nos sale 'set' pero el 'type' de valor sigue siendo 'str'. No sé qué puede ser 'set', ya veremos.
    print("\n")                                                 # Comentario asociado: Mismo resultado en pantalla que el "print()".
asyncio.run(w8()), print("______________________________________")



## Porcentajes ##
print('20- PORCENTAJE DE IDIOTAS'), print(), asyncio.run(w8())
idiotas= int(input("¿Cuántos idiotas conoces? "))
porcentaje =int(input(f"¿Qué porcentaje de {idiotas} quieres sacar a pasear hoy? "))
operacion=(idiotas*(porcentaje/100))
print(f"El {porcentaje} por ciento de {idiotas} idiotas que tocan para hoy es: {operacion}")
asyncio.run(w8()), print(), print("______________________________________")



## Bucle infinito de números ##
print('21- SUSURROS DE LA ETERNIDAD'), print(), asyncio.run(w8())
"""Pediremos números al usuario indefinidamente hasta que saque el 111. Porque somos malvados, y ya está.""" # Estas triples comillas deben encabezar una sentencia vacía o libre. Si lo situara justo después del 'input' que le precede, Python nos daría una sintaxis inválida. El 'input' al igual que los 'print', pueden compartir línea separados por ','.
contador=1                                                                                                      # Como luego definimos la función 'while' menor que 100, mientras este valor sea menor a dicha cifra, entraremos en un bucle infinito porque no hay contador +1 tras cada intento o algo parecido incorporado a esta parte del código.
print("«Oyes una aguda risa malvada»")
while contador<100:
    numero = int(input("\"Introduce el número que quieras, estarás aquí atrapado para toda la eternidad\": "))  # "\" permite incluir comillas dentro de un texto entrecomillado.
    if numero == 111:                                                                                           # No sé qué me pasa, pero debo prestar más antención entre las diferencias de '=' y '==' (comparador).
        print("¡¡Nooooooooo!! «escuchas cómo la vocecilla aguda va disminuyendo progresivamente»"), asyncio.run(w8())
        print("<<GRAAACIAS. POR FIN PODRÉ DESCANSAAAR>>")                                                       # Si esta instrucción fuese después de 'break', no se ejecutaría y por lo tanto no se mostraría en pantalla.
        asyncio.run(w8()), print("<<AAADIOOOS.>>")
        asyncio.run(w8()), print("«notas cómo el fantasma se marcha, al fin en paz»")
        break                                                                                                   # Cuando un bucle es cortado/abandonado repentinamente por un 'break' se le llama bucle controlado por centinela.
    else:
        print(f"Introdujiste el {numero}")
        asyncio.run(w8())
        print("«Oyes un grave susurro en la lejanía <<TREEES VECES UUUNOOO>>»")
asyncio.run(w8()), print(), print("______________________________________")



## Acumulación y valoración de notas (datos) con alumnos (variables) ##
print('22- MAMÁ, EL PROFE ME TIENE MANÍA'), print(), asyncio.run(w8())
"""Para pedirle la nota a 7 alumnos e imprimir los aprobados y los septiembres"""
contador = 1                                                        # Es 1 porque si no se incluiría el "alumno 0".
aprobados = 0
suspendidos = 0
numero_alumnos = int(input("¿Cuántos alumnos tenías en la clase? ¿Eran 7?: "))
while contador <= numero_alumnos:                                   # El contador condicionado por 'while' seguirá iterando hasta llegar al último alumno.
    nota=int(input(f"Qué nota tiene el \"alumno {contador}\"? "))   # La fórmula in(input)) recuerda que es para meter integers en vez de texto (string).
    if nota >= 5:                                                   # condición anidada
        aprobados += 1                                              # Porque si no no contabilizaría. Si fuese un 3 en vez de un 1 pondríamos la misma nota a tres alumnos distintos con cada cifra introducida.
    else:
        suspendidos += 1                                            # Si quisiéramos introducir distintas notas para un mismo alumno, habría que añadir más variables que sumasen de la misma manera que ahora el tope lo tiene el contador y la variable que va escalando es la de los alumnos, a su vez tanto aprobados como suspensos.
    contador += 1                                                   # Imprescindible porque sin esa progresión, atasco indefinido salvo que introdujésemos un valor que superara al valor asignado a la variable en la propia definición de la condición 'while'
print(f"Alumnos aprobados: {aprobados}") 
print(f"Alumnos que han cateado: {suspendidos}")
asyncio.run(w8()), print(), print("______________________________________")



## Invocaciones ##
print('23- FUNCIONES Y PARÁMETROS'), print(), asyncio.run(w8())
def muestraNombre():        # 'def' es una palabra reservada (equivalente a function en otros lenguajes) que significa 'defined'. El 'def' puede aparecer en verde si se considera "str".
    print("Charlie")
    print("Ermenegildo")
    print("M-BOT")
muestraNombre()             # Invoca a la función mostrándola en pantalla (equivalente a 'print' en este aspecto, pero si pones print(muestraNombre) daría error). Y es necesario ese "()" para la invocación.

print()

# nombre = "Carlitos Brown"                 # Esta sentencia queda invalidada al poner "nombre" en la siguiente línea, eliminando el texto fijo "Carlitos Brown" que antes nos imprimía en pantalla.
def mostrarTuNombre(nombre):
    print(f"Tu nombre es: {nombre}")        # Por lo demás nos mostraría esos tres resultados en pantalla.
mostrarTuNombre("RBK")
mostrarTuNombre("Juana")
mostrarTuNombre("Lilith")
nombre = input("Introduce tu nombre: ")     # Y después preguntarían al del usuario, para volver a introducir y mostrar en pantalla el nuevo valor escrito por la invocación de abajo.
mostrarTuNombre(nombre)

print()

def mostrarTuNombre(nombre, edad):                              # Tercer ejemplo. Python me muestra como problema que esta función ya está definida anteriormente dentro de este mismo ejercicio "function already defined line XXX pylint(function-redefined) [XXX, 1]". No sé por qué esas equis aparecen en verde.
    print(f"Tu nombre es: {nombre}")
    if edad >= 18:                                              # Variable que a la hora de ejecutar no la incrustación sino la definición, el programa realizará un flujo de ejecución buscando que se cumpla la función de los números enteros.
        print("Sí que es mayor de edad, sí. Sisi.")
nombre = input("Por favar, introduzca el nombre de un adulto: ")
mostrarTuNombre(nombre, 19)                                     # Si lo introdujésemos con 'def' al principio, no estaríamos invocando la función, nos saldría sintaxis inválida y el integer se mostraría como otro argumento más que como otro valor.
# Se puede cambiar ese '19' por 'edad', y colocar un input de la variable edad debajo de la variable nombre, para cambiar ese valor fijo por un valor cambiante (el que nos pusiera el usuario). Recuerda que antes de ese input vendría 'int' para convertir los datos introducidos en integers, en números enteros. Si no saldría un error tipológico. Y si eres menor de edad no sucederá nada porque nos da pereza.

print()

def function():              # Aquí definimos la función 'function'.
    return "Hola Mundo"     # 'return' sirve para muchas cosas, en este caso para devolver un valor (o mejor dicho, devolver datos).
frase = function()           # 'frase' es la variable de un valor definido, el cual nos devolverá como valor el texto entrecomillado.
print(frase)                # Finalmente se imprimirá 'frase', el invocador de la invocación 'function()' cuya definición nos retornará el valor de dicho texto entrecomillado.
asyncio.run(w8()), print(), print("______________________________________")



## Tabla específica ##
print('24- TABLAS DE MULTIPLICAR EFICIENTES'), print(), asyncio.run(w8())

def tabla(nº):                                          # 'def' define una función para crear 'objetos funciones' definidas por el usuario. La función no será ejecutada hasta que no sea invocada.
    print(f"Tabla de multiplicar del número: {nº}")
    for contador in range (11):
        operacion = nº*contador
        print(f"{nº} x {contador} = {operacion}")
    print ("\n")
tabla (1)
tabla (2), tabla (3), tabla (4)                         # Sale los mismos resultados, espacios y saltos de línea que en la tabla (1).
# tabla in range (10, 101)                              # No sería la manera correcta de abarcar un rango de números para este caso.
for numero_tabla in range(10, 15):                      # Para que sacase directamente las tablas de multiplicar invocando múltiples números en un rango sería 'for' + variable2 + 'in range'...
    tabla(numero_tabla)                                 # ... y luego ejecutar el bloque de instrucciones "tabla" (definido como "nº") pasando por el rango que le acabamos de dar del 10 al 14.
# no saldría la tabla del 5 al 9 pero sí las restantes del 1 al 14. Si quisiéramos que saliera el cero, habría que añadir -1, 11 en el rango del principio. Y para que saliera 15, pues aumentar en uno el límite '15' del 2º rango escrito.
asyncio.run(w8()), print(), print("______________________________________")



## Booleanos True-False, None ##
print('25- PARÁMETROS OPCIONALES'), print(), asyncio.run(w8())
def getemployee(nombre, dni):
    print("EMPLEADO")
    print(f"Nombre: {nombre}")
    print(f"DNI: {dni}")
getemployee("Swan", 7777)                   # Sin el "7777" no habría segundo argumento en la invocación de la variable "getemployee", así que nos daría fallo.

asyncio.run(w8()), print()

def getemployee(nombre, dni = False):       # Entran aquí en juego los booleanos 'True' y 'False'. También podríamos usar la función None. Para convertir en opcional el parámetro de introducir el "dni" hay que incluir un parámetro opcional.
    print("EMPLEADO")
    print(f"Nombre: {nombre}")
    print(f"DNI: {dni}")
getemployee("Swanros")                      # Ejecutando el programa no nos dará error, nos mostrará "dni: False".

asyncio.run(w8()), print()

def getemployee(nombre, dni = None):        # El sistema nos señalará como problemilla de repetición las dos definiciones siguientes cuyo valor le hemos cambiado añadiendo "False" a una y "None" a otra.
    print("EMPLEADO")
    print(f"Nombre: {nombre}")
    if dni != None:                         # Si fuera == None no mostraría el dni. Pero si es diferente a None (!=) directamente no te muestra el dni y el programa se ejecuta correctamente.
        print(f"DNI: {dni}")                # Se les llama parámetros opcionales por eso. Para distinguir lo obligatorio de lo voluntario para que no nos de error ni problema.
getemployee("Swanrose", "8888")             # Podríamos incluir un número (integer) como string entrecomillado separado por una coma del nombre o como integer directamente tras una coma.
asyncio.run(w8()), print(), print("______________________________________")



## Función return ##
print('26- OPERACIÓN RETORNO'), print(), asyncio.run(w8())
def saludame(nombre):
    saludo = f"Hola, saludos {nombre}"
    return saludo                           # Devolverá un dato dentro de la función pero fuera de la misma.
saludame("Charleston")                      # Ahí ejecutas el programa, pero la función no muestra nada. Es por la posición del return en este chunk, que te lo devuelve (para imprimirlo fuera), pero no te lo imprime.
print(saludame("Charles Stone"))            # Ahora sí saldría en pantalla, respecto a la duda mostrada en el comentario anterior de arriba.

asyncio.run(w8()), print()

def calculadora(numero1, numero2, basicas = False):
    suma=numero1+numero2
    resta=numero1-numero2
    multi=numero1*numero2
    divi=numero1/numero2
    cadena = ""
    if basicas != False:                    # != es un operador que indica que algo no es igual a otro algo.
        cadena += "Suma: "+str(suma)        # Se le puede concatenar y añadir a la variable original en lugar de integers, diferentes trozos de string en este caso.
        cadena += "\n"
        cadena += "Resta: " + str (resta)   # Esas 'cadena' deben ir tabuladas al haberle metido la condición 'if' y 'else'.
        cadena += "\n"
    else:                                   # De esta manera hemos intercalado esta condición así de buenas solo para cumplir con el objetivo de sacar solo las operaciones matemáticas básicas de suma y resta
        cadena += "Multiplicación: " +str(multi)
        cadena += "\n"
        cadena += "División: " + str (divi)
    return cadena                           # Retornará todos esos datos "cadena" la cual a su vez incluyen las operaciones anteriormente definidas a "cadena". Esto es parecido a poner incrustaciones y las operaciones aritméticas dentro de cada doble llave, pero es más fancy y breve.
print(calculadora(5,5))                     # Según los números que les pongamos, nos dará distintos resultados aritméticos.
print(calculadora(7,7,True))                # Aquí se le pide que saque solo las operaciones básicas al haber añadido el argumento True, el cual sería direccionado a básicas, haciendo que la condición 'if' sea un operador 'True' distinto a 'False', y que si no fuera así y solo introdujésemos dos valores (dos integers en este caso), pues nos de también la multiplicación y la división.
# Si eliminamos ese 'True' de arriba, borramos dicho parámetro opcional, ejecutando todas las instrucciones indicadas en el valor de 'return'.
asyncio.run(w8()), print(), print("______________________________________")



## Return y cúmulo de funciones ##
print('27- FUNCIONES DENTRO DE OTRAS FUNCIONES (INCEPTION)'), print(), asyncio.run(w8())
def getNombre(nombre):
    texto = f"El nombre es: {nombre}"                           # Te puedes creer que hasta ahora no había visto ejemplos de la literalidad 'f' sin estar adyuvantes (gracias Miguel Bosé's) a la función 'print'.
    return texto                                                # El return convierte a la variable local getNombre en una variable global de nuestro código.
def getApellidos(apellidos):
    texto = f"Los apellidos son: {apellidos}"
    return texto                                                # Sin este 'return', Python nos diría que solo puede concatenar string a string, no "NoneType". Es decir, sería una función de No Tipo sin este 'return' en este caso.
print(getNombre("Víctor"), getApellidos ("Robles Web"))         # Tienes que asignar valores a ambos parámetros/argumentos (no son variables) con la definición lista para ser argumentada.
def devuelveTodo(nombre, apellidos):                            # Ejemplo de cómo usar funciones dentro de otras funciones.
    texto = getNombre(nombre) + "\n" + getApellidos(apellidos)  # Concatenación de strings. 'getNombre' es la función. 'nombre' es el parámetro, se le concatena un salto de línea y luego la función de getApellidos y el argumento de apellidos.
    return texto                                                # Sin este 'return' concreto, nos daría "None" como resultado entero de la función. Resultado diferente a quitar los otros return de arriba porque no son invocados en las incrustaciones de texto entrecomillado.
print(devuelveTodo ("Víctor", "Robles Dep"))                    # Esto nos daría como resultado la misma funcionalidad que en las incrustaciones anteriores. El texto entrecomillado que mostremos separados por comas irán a parar a sus respectivos {argumentos}. Sin el texto entrecomillado Python nos avisaría de que la tercera función "texto" (la línea de justo arriba) sería una variable no usada, y nos la subrayaría en amarillo, color no visto hasta ahora en los avisos de errores y advertencias [de hecho sale en la cmd <function devuelveTodo at 0x018D8148>].
# Si no incluyésemos todos los mismos argumentos (el texto entrecomillado separado por sus respectivas comas para las funciones getNombre y getApellidos respectivamente), saldría ""None".
# De esta manera con esa función escrita después del primer 'print' se reutiliza el mismo código invocando la sencilla función de devuelveTodo para que a su vez invoque a tantas funciones como las dejadas en las instrucciones internas definidas dentro de la misma función "devuelveTodo".
# Si ofreciésemos otra función en el último print separado por una coma, nos sale como tipo de error en la cmd que esa función toma dos posiciones argumentales pero le fueron dadas tres. Así que error.
asyncio.run(w8()), print(), print("______________________________________")



## Función lambda ##
print('28- LAMBDA ANÓNIMA'), print(), asyncio.run(w8())
dime_el_year = lambda year: f"Estamos en el año {year}"     # Todo debe definirse en una sola línea, sean operaciones aritméticas, incrustaciones, devolución de datos... etc
print(dime_el_year(2034))                                   # La incrustación podría contener operaciones dentro de sí misma sin problemas. Normas: definición completa en una sola línea. ¿Condicionales if/else? No porque no son sencillas y ya a ver cómo manejarías las tabulaciones.
asyncio.run(w8()), print(), print("______________________________________")



## Variables locales y globales e invocaciones ##
print('29- VARIACIONES LOCALES Y GLOBALES'), print(), asyncio.run(w8())
juramento = "Vida antes que muerte"
print(juramento)                                # Imprimirá nuestra variable global "juramento" (porque no está declarada dentro de una función), con el texto entrecomillado "Vida antes que muerte". Una variable global se declarada fuera de la función, pero están siempre disponibles dentro y fuera de la función.
def juramentosradiantes():
    juramento = "Fuerza antes que debilidad"    # Valor asignado a la función definida de la variable 'juramentosradiantes'. La variable local es una variable definida dentro de la función única y exclusivamente. No servirá para otras funciones salvo que hagamos 'return'.
    print(juramento)
juramentosradiantes()                           # Si solo pusiésemos "juramento" en su lugar, nos saldría el error de que no estaría definida. La invocación 'juramentosradiantes' sería necesaria para llamar al segundo texto 'juramento', dado que dicho 'print' definido como "Fuerza antes que debilidad" solo sería efectivamente mostrado si se llama a ejecutar la función 'def' [nombrada como 'juramentosradiantes', no como 'juramento'], y así ejecutar la definición que le hemos dado (y todas las otras instrucciones que le incorporásemos).

asyncio.run(w8()), print()

juramento = "Vida antes que muerte"
print(juramento)                            
def juramentosradiantes():
    # juramento = "Fuerza antes que debilidad"  # Si comentamos esta línea, si no "machacas" [o sobreescribes] el contenido o generas una variable local te mostrará los mismos datos que en la primera asignación [recordando que si das diferentes valores a la misma variable, solo se mostrará el último resultado de todos ellos, en plan el más "actualizado"].
    print(juramento)                            # Ahora este print accede a la variable 'juramento', la cual es una variable global (la primera línea que contiene el valor de texto "Vida antes que muerte"). Así que esa accesibilidad se daría desde cualquier parte del código, dado que no hemos definido una función concreta para la variable 'juramento' ("Fuerza antes que debilidad") distinta al 'juramento' de la primera línea ("Vida antes que muerte").
    # Pero seguirá sin imprimirse en la pantalla de nuestro ordenador al estar contenida dentro de esta función. Para ello es necesario llamar a la variable 'juramento' o imprimir la variable para que se muestr en pantalla.
juramentosradiantes()                           # si metes aquí un 'print(juramentosradiantes)' sale que "<function juramentosradiantes at 0x03AD7148 [equivalen a localización cartesiana de nuestros caracteres]>" , pero no nos muestra un subrayado amarillo como en el ejemplo 27. ¿Dónde está el error? Pues DDD.

asyncio.run(w8()), print()

juramento = "Vida antes que muerte"
print(juramento)                   
def juramentosradiantes():
    juramento = "Fuerza antes que debilidad"
    print(juramento)               
    año_de_desolacion = 99
    print(año_de_desolacion)
    return str(año_de_desolacion)   # línea de código necesaria para hacer accesible la variable 'año_de_desolacion' fuera de la función, en la impresión posterior de afuera. Str es para convertir en cadenas de caracteres el integer "99".
juramentosradiantes()
print(juramentosradiantes())        # Recuerda, estamos imprimiendo una invocación, no una variable, de ahí el '()' extra. Aunque ahora año_de_desolacion esté accesible, no puedes invocarla directamente como tal. Porque no está definida. En realidad forma parte de la definición de 'juramentosradiantes'. Sería el equivalente a definir lo siguiente: el ser humano = una forma de vida basada en carbono. Si ahí tratamos de definir carbono, ¿qué nos va a devolver? si no hay nada. Es el contenido de un continente mayor y definido como es "ser humano" en este comentario concreto.
#print(año_de_desolacion)           # Introducir esta línea de código estaría mal. Habría que llamar a la función definida 'juramentosradiantes' y no llamar a la variable contenida dentro de una función local [en este caso 'año_de_desolacion'], porque aunque esté dentro de una definición, no tiene una definición por sí misma. Así que también daría igual que la llamásemos como variable o como invocación [añadiendo '() al final de la misma, como en la línea de arriba]
# E insisto en el hecho de que en este último caso no imprimiría en pantalla, porque 'año_de_desolacion' solo es accesible dentro de la función local, no es una variable local, no existe fuera de ella. Para ello, habría que retornar los datos de la variable local mediante la función 'return año_de_desolacion'. 

asyncio.run(w8()), print()

# Para actualizar una variable dentro de una función o que la variable dentro de una función sea una variable global:
juramento = "Vida antes que muerte"
print("Kaladin, haz la promosió: ")
print(juramento)                   
def juramentosradiantes():
    juramento = "Fuerza antes que debilidad"
    print(juramento)
    global website                              # Función 'global' para poder hacer un print dentro de la función.
    website = "cosmere.es"                      # Para lograr que esta variable pueda accederse desde fuera se tendría que incorporar la función 'global' y hacerla así global.
    print("DENTRO: ", website)                  # Si no cerrásemos el paréntesis tras "website", el programa nos daría «SyntaxError: unexpected EOF while parsing». Sucede cuando el parser (módulo contrario a 'format' que actúa como un compilador de códigos byte [byte-code compiler]) encuentra inesperadamente el fin de un archivo.
    return "Viaje antes que destino"            # Debemos meter un 'return' o entre medio de las dos webs DENTRO y FUERA o nos saldría "None" en el Símbolo del Sistema. Y los datos devueltos no tienen por qué ser los dados anteriormente por nosotros en la definición de 'juramentosradiantes'. En realidad nos devolverá el texto "Viaje antes que destino" porque nos ha dado por ahí.
print(juramentosradiantes())                    # Si no incluyésemos '()' después de introducir el nombre que le hayamos puesto a la variable o asignación, nos saldrá error del tipo "<function holaMundo at 0x010AD190>". Siempre que una variable sea "definida" ('def'), '()' al final de la variable [junto al cierra paréntesis si está dentro de otra función, como 'print' por ejemplo].
print("FUERA: ", website)                       # De esta manera la variable local se hizo global gracias a la función homónima dentro de la definición de 'juramentosradiantes', pero solo tras haber sido ejecutada la función anterior.
asyncio.run(w8()), print(), print("______________________________________")



## funciones type, if, else, if not, del y métodos'.' ##
print('30- FUNCIONES PREDEFINIDAS'), print(), asyncio.run(w8())
# Imprimir tipología de una variable (string, integer, float...).
nombrecillo = "Carlillos"
print("Carlillos")
print(type(nombrecillo))


# 'isinstance' comprueba que la variable es el tipo de variable que nosotros queremos, definiendo qué tipología nos esperamos en el segundo parámetro del valor asignado.
comprobar = isinstance(nombrecillo, str)
if comprobar:                                           # Si no le añadimos ninguna condición (ni '=' ni comparación '=='), este 'if' entiende automáticamente que el usuario quiere que esa variable de 'True'.
    print("Esa variable es un string")
else:
    print("No es una cadena")
if not isinstance(nombrecillo, float):
    print("La variable no es un número con decimales")
asyncio.run(w8()), print()


# Con ese punto y '()' se llama a la función strip, limpiando solo los espacios anteriores y previos tangentes al entrecomillado, no a los espacios internos.
frase = "      mi cont enido t iene  muchos espacios   "
print(frase)
print(frase.strip())                                        
asyncio.run(w8()), print()
# Si volviésemos a imprimir esa variable nos saldría error. Porque 'del' (delete) elimina la definición adjudicada a una variable.
del nombrecillo


# 'len' (lenght) mide el número de caracteres. De esta manera nos indicará que 'textamen' contiene siete caracteres.
textamen = " FfFf  "
if len(textamen) <= 0:                                      # 'len' también es aplicable a listas.
    print("La variable tiene contenido")
else:
    print("La variable tiene contenido: ", len(textamen))
asyncio.run(w8()), print()


# Para encontrar caracteres dentro de un string. Saldrá un número que indicará a partir de qué caracter se ubica (empieza por el cero, así que el 3º será la 'v' y no el espacio tras el 'La').
frase = "La vida es bella"
print(frase.find("vida")), asyncio.run(w8()), print()


# Reemplazar palabras en un string
frase2 = frase.replace("vida", "bida")      # Sustituirá el primer parámetro por el segundo.
# frase2 = frase.replace("vida, bida")      # Error: el sistema tendrá un argumento donde esperaba dos, ya que solo hay un entrecomillado en lugar de dos separados por comas.
print(frase2), asyncio.run(w8()), print()


# Procesar mayúsculas y minúsculas
print(textamen)             # Porque ALGUIEN ha quitado la variable 'nombrecillo', tenemos que usar este otro.
print(textamen.lower())     # Todo en minúsculas.
print(textamen.upper())     # Todo en mayúsculas.


# Medir elementos de una lista
lista = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']
totaldiascuentavieja = 0

for dia in lista:
    totaldiascuentavieja += 1

print("El número de elementos de la lista, por la cuenta de la vieja es",
 totaldiascuentavieja)
print("El número de elementos de la lista según la función len es", len(lista))
# En el caso de las sublistas (dentro de listas) cuando referenciemos fuera de sus límites no nos dará error (como sí pasaría en una lista), ya que más que tomarlo como un índice real, lo tomará como una cota superior, extrayendo todo lo que haya en medio de esa sublista sin importar que dicha lista concluya antes.
asyncio.run(w8()), print(), print("______________________________________")


# Return, definiciones e invocaciones
print('31- CURIOSIDADES'), print(), asyncio.run(w8())
# Se recomienda definir todas las variables en un mismo segmento, preferentemente arriba de todo el fichero.
# Más que nada porque si invocas una función '(textamen())' antes de definirla, no funcionará porque la función no estará definida. Si bien respetando este orden de los acontecimientos, puedes escribir donde te de la gana en el código.
def mi_funcion():
    print("Hola que tal, amigo")
def mi_segunda_funcion():
    print("Hola, hijo de puta")
mi_funcion()
mi_segunda_funcion()

asyncio.run(w8()), print()

# Se recomienda en vez de hacer 'print' dentro de una función que devuelva siempre un dato. Es lo más estándar y la mejor práctica.
def mi_funcion():
    return "Hola que tal, amigo"
def mi_segunda_funcion():
    return "Hola, hijo de puta"
print(mi_funcion())                 #'()' siempre que se invoque una variable [¿o función también?] definida.
print(mi_segunda_funcion())

asyncio.run(w8()), print()

#Acceder a variables globales dentro de funciones locales definidas escogiendo variables del lejano tercer ejercicio:
def mi_funcion():
    return "Hola que tal, amigo " + name1       # El espacio tras 'amigo' es necesario para que respire el texto siguiente de la variable a invocar dentro de una función local.
def mi_segunda_funcion():
    return "Hola, hijo de puta " +  apellidos3  # Ambas variables 'name1' y 'apellidos3' son de la actividad que lleva por título '3 CONCATENACIÓN'.
print(mi_funcion())                             # Si no incluyese de nuevo estas dos funciones, no me imprimiría estos últimos cambios hechos sobre la definición de 'mi_funcion' y 'mi_segunda_funcion'.
print(mi_segunda_funcion())
asyncio.run(w8()), print(), print("______________________________________")



## listas, tuplas, listas con rangos ##
print('32- LISTAS/ARRAYS/ARREGLOS'), print(), asyncio.run(w8()) # Parecidas a las tuplas salvo que los datos de las tuplas no se pueden modificar.
# 'array': colección o conjunto de datos o valores bajo un único nombre [lista]. Para acceder a dichos valores se puede usar un índice numérico.
# En el caso de otros lenguajes cuando se usa array se utilizan índices alfanuméricos, siendo en Python necesario utilizar en su lugar el diccionario.
peliculas= ["Batman", "Spiderman", "LOTR"]      # "Batman" sería el elemento uno (índice cero), "Spiderman" el elemento o argumento dos (índice uno), "LOTR" el elemento tres (e índice dos)... En programación siempre se empieza a contar por el cero. Pueden modificarse el contenido interno de cualquiera de esos índices.
print(peliculas)                                # Imprime cada uno de esos índices señalados entre corchetes. Así se define una lista.
cantantes=list(("AC/DC", "AB/CD", "Airbourne")) # Ese doble paréntesis extra es la 'tupla', un array necesario para que la función 'list' funcione como una lista. Spoiler: es más sencillo de la otra manera, entre corchetes.
# cantantes=list("AC/DC", "AB/CD", "Airbourne") # Error: la lista espera un argumento y ha recibido tres. 
print(cantantes)                                # Imprimir la variable mostrará entonces una colección de elementos, una colección de valores de strings convertidos en lista y ahora sí modificables y pudiendo ser usadas como una lista normal.
years = list(range(2020, 2030))                 # Así se genera una "array", es decir, una lista de números siguiendo el rango señalado.
print(years)
variada = ["Blyat", 2, 2.2, True,]              # No obliga a ningún argumento a pertenecer a una tipología concreta.
print(variada)
asyncio.run(w8()), print(), print("______________________________________")



## índices y su significado ##
print('33- ÍNDICES DE LISTAS'), print(), asyncio.run(w8())
print(peliculas[1])             # Para sacar un índice concreto. 'Spiderman'. Un gran índice conlleva una gran...
print(peliculas[-3])            # Lo que hace es empezar desde atrás del todo de la lista en lugar de al principio, saliendo Batmaaaaan.
print(cantantes[1:3])           # Saca dos elementos: el '1' y el '2'. Si omitiésemos el primer valor del 'slice' y fuera "cantantes[:3]", Python sobreentiende que lo omitido sería el comienzo de la lista (es decir, lo interpretaría como "cantantes[0:3]"). Y si fuese [3:] pues del tercero hasta el final de la lista. Y si fuese [:] la lista completa de cantantes de principio a fin.
print(cantantes[0:1])           # Saca un elemento, el cero. Y con '0:2' los dos primeros elementos el cero y el uno.
print(cantantes[1:5])           # Simplemente mostrará toda la lista si te sobrepasas respecto al número de elementos que la componen.
print(peliculas[1:])            # Mostrará todos los elementos a partir del índice uno "Spiderman" (el elemento dos), dado que el índice cero "Batman" es el primer elemento de una lista cualesquiera en muchos programas de lenguaje.
peliculas[1] = "Gran Torino"    # Sustituirá el índice uno (el segundo elemento), siendo ahora en vez de "Spiderman" pues "Gran Torino".
# peliculas[5] = "Wat the heck" # Error: "IndexError: list assignment index out of range". Aquí si te sorpasas dará error de índice.
print(peliculas)                # Batman, Gran Torino y LOTR.
asyncio.run(w8()), print(), print("______________________________________")



## for - in, while, format ##
print('34- AÑADIR ELEMENTOS Y RECORRER UNA LISTA'), print(), asyncio.run(w8())
cantantes.append("Kase Drugs")  # Se pueden añadir cuantos se quieran a la lista...
print(cantantes)                # ... así se añadirá al final de la lista impresa (o imprimida).

asyncio.run(w8()), print()

for pelicula in peliculas:      # Para mostrar una película detrás de otra como una lista que recorra de arriba a abajo sin mostrar los restantes elementos.
    print(pelicula)
for pelicula in peliculas:
    print(f"{peliculas.index(pelicula)+1}. {pelicula}")   # Los elementos aparecerán mostrando un número (a causa del método 'index') y junto a ese punto de texto entre ambas incrustaciones termina dando un efecto de lista 1. Batman, 2. Gran Torino... Ese +1 es para que no empiece la lista por el "0.".
# Observación: si juntase ambos print en la misma función 'for' saldrían ambos resultados alternadamente.

asyncio.run(w8()), print()
nueva_pelicula = ""
while nueva_pelicula != "parar":                        #!= es el operador "mientras sea diferente".
    nueva_pelicula = input("Introduce la peli ya [escribe \"parar\" cuando te canses de meter truños en la cartelera]: ")   #Si no introducimos ninguna nueva peli, saldrá
    peliculas.append(nueva_pelicula)                    # Sacará un listado infinito de películas, siendo la última de todas ellas "parar", porque no hemos introducido un bucle 'break' ni un contador con límite superior. Esto se podría subsanar si justo encima de esta línea incorporásemos en la misma tabulación interna la condición "if nueva_pelicula != 'parar'".
for pelicula in peliculas:
    print(f"{peliculas.index(pelicula)+1}. {pelicula}") # Si no copiásemos esta función con su print local, no obtendríamos el resultado del input que hiciera el usuario ni tampoco del listado de películas.
asyncio.run(w8()), print(), print("______________________________________")



## Suma de números con opción de finalizar ##
print('35- CADA MOCHUELO CONTINÚE EN SU OLIVO'), print(), asyncio.run(w8())
suma = 0
while True:
    numero = int(input('Introduce un número (0 para terminar):'))
    if numero == 0:
        break               # Si introducimos el número cero terminará la función.
    if numero % 2 != 0:     # No sumará los números impares dado que el resto sería algo distinto a cero. No obstante la función de después permitiría continuar con el proceso ad infinitum.
        continue            # Hace que se salte inmediatamente a la siguiente repetición, volviendo a comprobar si se cumple una condición, y en caso afirmativo, ejecutar el bloque desde el principio otra vez.
    suma = suma + numero    # Observaciones: sumará los números pares que introduzcamos. Si eliminamos esa segunda 'suma', solo nos daría el último número introducido por el usuario. Si esta línea fuese "suma+=numero" daría exactamente lo mismo.
print(suma)                 # Como variable global es '0'. No obstante al final de la función 'while' viene cargada de valor al sumársele su propio valor (cero) y los números pares introducidos como 'input'.
asyncio.run(w8()), print(), print("______________________________________")



## Listas y dimensiones ##
print('36- LISTAS MULTIDIMENSIONALES DEL DR. STRANGE'), print(), asyncio.run(w8())
"""Listas dentro de listas, con varias dimensiones inside"""
print("*********************LISTA CONTACTOS*********************")
contactos=[                         # Este corchete y el final involucrarán otras dimensiones (otras jerarquías) de lista (porque se usan corchetes).
    [                               # Observación: estos corchetes internos podrían ser paréntesis. En la pantalla saldría imprimido [('x')] en lugar de [['x']].
        'José Antonio',             # Siempre ha de ir tabulado los corchetes internos en el desglose de contenidos de una lista o parecido.
        'primorivera@fachada.com'
    ],                              # Error: sin la coma de esta línea de código nos saldría: "TypeError: list indices must be integers or slices, not tuple".
    [
        'Luis',                     # Si no estuviese esa coma saldría el nombre y el correo todo seguido (al carecer de un caracter de espacio entre ellos).
        'ptcdiscneft@gmail.com'     # No obstante si el elemento final tiene o no tiene coma proporciona el mismo resultado si se imprime en pantalla.
    ],
    [   'Mamá'                      # Observaciones: podría ponerse una línea más arriba respecto a los anteriores ejemplos que el resultado sería lo mismo. Si no ponemos coma se juntará con la siguiente línea, de ahí que 'alarma llamar cena' tenga un caracter de espacio extra.
        ' alarma@llamar.uk'
    ]
]
print(contactos)
# Tenemos las listas 0, 1 y 2, las cuales contienen dos elementos 0 y 1 en cada una de ellas. Si quisiera acceder únicamente al email de 'Luis' pondría: print(contactos[1][1]).
for contacto in contactos:          # Aquí contacto es una nueva variable que es
    print(contacto[0])              # De esta manera usando los corchetes se podría acceder al índice, para sacar únicamente el nombre de los contactos.

asyncio.run(w8()), print()

for contacto in contactos:          # Duda: ¿por qué si pusiera 'contactos' donde 'contacto' en toda esta función de aquí me saldría exactamente el mismo resultado? Explayándome: ¿cómo el programa interpreta que esa nueva variable 'contacto' se refiere a los elementos internos de esa lista como índices 0 [Antonio], 1 [Luis] y 2 [Salvador] en lugar de 0 [Antonio], 1[email de Antonio], 2[ Luis], 3[email de Luis], 4[Salvador], 5[email de Salvador]?
    for elemento in contacto:       # Duda1: ¿Cómo sabe el sistema que 'elemento' refiere a que saque el nombre y el email de cada persona automáticamente? Resulta que esa función dentro de la otra función permite recorrer ese array (esa lista) dentro del otro bucle...
        print(elemento)             # Duda1: ...de tal manera que saca nombre e email.
    print ("\n")                    # Si este salto de línea estuviese una tabulación más a la derecha, el salto se haría cada bloque de dos, después de cada índice principal en la primera dimensión, no en la segunda dimensión. La 1ª dimensión es el primer corchete en la variable definida al principio del ejercicio y la 2ª los otros corchetes que hemos ido introduciendo nombre e email.

asyncio.run(w8()), print()

for contacto in contactos:          
    for elemento in contacto:                   # 
        if contacto.index(elemento) == 0:       # Si no pusiésemos 'elemento' dentro del índice nos daría error de índice que esperaba un argumento '(elemento)' y recibió ninguno '()'. Si el elemento 0 es el nombre, si no es el cero es el 1 así que mostraría el email directamente.
            print("Nombre: " + elemento)        # Concatenación de texto string + variable 'elemento'.
        else:
            print("Email: " + elemento)
    print("\n")                                 # «El 'print' debe ir en el 'for' principal» [así fue referido a ese segundo 'for', nuse. Ahí está bien y punto].
asyncio.run(w8()), print(), print("______________________________________")



## Métodos en listas y función 'in' ##
print('37- FUNCIONES Y MÉTODOS EN ARRAYS'), print(), asyncio.run(w8())
cantantes = ["Romano Aspas", "Yo en la ducha", "Rosalía", "Julio Iglesias"]
numeros=[1,2,5,8,3, 4,27]
print(numeros)
numeros.sort()                      # Se le podrían añadir parámetros al método sort. Lo que hará será ordenar de manera creciente los números depositados en ella.
print(numeros)                      # Lista ordenada.
cantantes.append("Natos y Waor")    # Agrega dos nuevos elementos al final de la lista.
print(cantantes)
cantantes.insert(2, "Bisbal")       # Agrega otro elemento pero especificando su posición [de ahí el nº 2], si no saldrá un error de tipo de insuficiente número de argumentos entregados. Si fuera un número negativo empezaría desde el final de la enumeración, recuerda.
print(cantantes)
cantantes.pop(1)                    # Para eliminar ciertos elementos dentro de una lista '.pop'. En este caso borraríamos a "Yo en la ducha". Cuidado que si quisiéramos borrar a un número concreto tras haber insertado otro índice por delante anteriormente, el orden de los índices importa.
cantantes.remove("Natos y Waor")    # Para eliminar un elemento el cual debe ser mencionado exactamente igual. Así es otra manera de eliminar elementos de un array, de una lista.
print(cantantes)
numeros.reverse()                   # Para empezar la lista al revés, desde el final al principio.
print(numeros)                      # Es ese resultado y no el de la variable al inicio del ejercicio porque se mantiene el método de ordenación creciente '.sort'.
print("Romano Aspas" in cantantes)  # Dará como resultado 'True'. Vale para buscar un elemento dentro de una lista.
print(len(cantantes))               # Contar elementos, en este caso el número de cantantes actual que habría tras todos esos cambios hechos ('len' = lenght).
print(numeros.count(8))             # Para ver cuántas veces aparece un mismo número o elemento si fuese texto.
print(cantantes.index("Rosalía"))   # Conseguir índice.
cantantes.extend(numeros)           # Unir dos listas.
print(cantantes), asyncio.run(w8()), print(), print("______________________________________")



## Campos de identificación ##
print('38- SETS Y DICCIONARIOS'), print(), asyncio.run(w8())
personas = {        # Un 'set' es una colección de datos sin índice ni orden que se fabrica a partir de la siguiente disposición de llaves '{}'.
    "Víctor",       # Sin esas comas todo el texto aparecería unido "VíctorManoloFrancisco". Con esas comas aparecen entre llaves delimitadas por 'comillas simples'.
    "Manolo",       # Lo que ocurre es que estos elementos integrados no tienen realmente ningún orden predefinido. Con cada impresión su posición puede variar aleatoriamente (random).
    "Francisco"     # Aunque a éste le falte una coma, se muestra igualmente como los otros strings.
}
personas.add("Juana")       # Se añadirá con el orden aleatorio que el set quiera. con cada impresión.
# personas.remove("Víctor") # Eliminaría a la persona "Víctor".
print(type(personas))       # Un 'set' no es tan útil ni bueno como una lista, pero existe.
print(personas)

asyncio.run(w8()), print()
# Los diccionarios tienen índices alfanuméricos (también llamado array asociativo u objeto Json) en su almacenaje de datos.
persona = {                     # Visualmente aparecerán encorsetados entre llaves.
    "nombre": "Víctor",
    "apellidos": "Robles",
    "web": "victorroblesweb.es"
}
print(persona)
print(persona["web"])           # Solo sacará el valor de la web.

asyncio.run(w8()), print()
# array o diccionario multiasociativo dimensional
contacts = [
    {
        'nombre': 'Cillo',
        'email': 'cillocabesa@arriquitaun.ozú'
    },
    {
        'nombre': 'Carles',                 # Sin esa coma sale error de sintaxis.
        'email':  'carlesjohanson@yo.es'    # Si pusiésemos 'emilio' o 'correo' en lugar de 'email', estaríamos cambiando el campo de identificación de dicha dirección de correo electrónico y nos daría error de llave "KeyError: 'email'" si intentamos llamar a todos los campos de dominio si alguno de ellos es distinto, cosa rara que tendré que pulir cuando tenga mayores conocimientos al respecto DDD.
    },
    {   'nombre': "RBK",                    # Esos dos puntos no podrían ir con un espacio de separación de "email", porque entonces 
        "email" : 'rbkchan@shenzen.nyan'     
    }
]
print(contacts[0]['nombre'])           # Para acceder a 'Cillo' según su índice principal y luego a su índice de texto al que está asociado el valor 'Cillo'.
contacts[0]['nombre'] = 'Cabecillo'    # Modificará el valor a la propiedad designada.
print()
# Los índices son asociativos. Las claves son asociativas y si se les otorga un valor (como el valor de texto en esos casos de la variable 'contacts') ya sabremos usar diccionarios en Python.
for contact in contacts:
    print(f"Nombre del contacto: {contact['nombre']}")  # Porque es más fácil recordar campos de identificación como 'nomnbre' que recordar números o posiciones listadas de lo que se busca, aunque sumásemos 1 como al final del ejercicio 34.
    print(f"Email de contacto: {contact['email']}")     # No pongas 'correo' en lugar de 'email' porque entonces estarás buscando un campo de identificación que no existe en la lista que has creado.
    print("-----------------------------------------")  # Para una separación visual que irá sucedíendose con cada elemento guardado en la lista de diccionario (cada grupo de ítems asociados a cada llave).
asyncio.run(w8()), print(), print("______________________________________")



## for, in, return, while not, input, else ##
print('39- LA LISTA QUE ME PARIÓ'), print(), asyncio.run(w8())
""" Ejercicio 1. Hacer un programa que tenga una lista de 8 integers y que haga lo siguiente:
- Recorrer la lista y mostrarla
- Hacer una función que recorra listas de números y devuelva un string
- Ordenar y mostrarla
- Mostrar su longitud
- Buscar algun elemento que el usuario pida por teclado
"""
# Crear una lista ##
listado= [21, 3, 2, 13, 34, 1, 5, 8]

# Crear una función que recorra la lista y devuelva un string ##
def mostrarLista(numeros):
    resultado = ""
    #for lista in listado:          # No puede usarse 'listado' como sí usaba en 'for lista in listado:' [por poder se podría pero ya no sería un parámetro de la lista], de ahí que también ponga 'elemento en lugar de 'lista'
        #resultado += str(lista)
    for elemento in numeros:
        resultado += "Elemento: " + str(elemento) # Este 'elemento' se coloca aquí en lugar de 'lista' para abstraerlo del caso concreto, pudiéndole pasar así listas de números, de letras etc.
        resultado += "\n"
    return resultado
print(mostrarLista(listado))        # Sin ese print la invocación no mostraría nada dado que todo sería un string, y por lo tanto sería equivalente a texto entrecomillado sin función 'print' adyuvante.

# Recorrer y mostrar
for lista in listado:
    print(lista)
print()

# Ordenar y mostrar
listado.sort()
print(mostrarLista(listado))        # Si hiciésemos 'print(listado)' nos aparecería un resultado distinto al 'print(mostrarListad(listado))'

# Mostrar longitud
print(len(listado))

# Búsqueda en la lista
busqueda = int(input("Introduce el número a buscar: "))

comprobar = isinstance(busqueda, int)                       # La función 'isinstance' comprueba que la variable definida es la variable que queremos, condicionando después qué delimitación debe tener.
while not comprobar or busqueda <= 0:                       # Números negativos y el cero nos devolverían a este mismo input insistentemente. Si introdujésemos un número positivo distinto al del listado nos daría error.
    busqueda = int(input("Introduce el número a buscar: ")) # Interesante el hecho de copiar toda una variable global dentro de una función local.
else:
    print(f"Has introducido el {busqueda}")
print(f"Buscar en la lista el número {busqueda}")

search = listado.index(busqueda)
print(f"El número buscado es el índice (ordenado): {search}")
asyncio.run(w8()), print(), print("______________________________________")



## while, for ##
print('40- AÑADIR DESDE LA NADA A UNA LISTA'), print(), asyncio.run(w8())
""" Ejercicio 2. Escribir un programa que añada valores a una lista mientras que su longitud sea menor a 120 y luego mostrar la lista.
- Usar while y for, ambas funciones para este cometido. """
coleccion = []                  # El bucle se encargará de añadir elementos a esta lista vacía

for contador in range(0, 120):  # Y ahora se agregan elementos a la lista:
    coleccion.append(f"elemento: {contador}")       # 'append' era el método para añadir un elemento cualquiera dentro de una lista. Así aparecerán separados por comas en una única gran línea los 120 elementos (del 0 al 119).
    print("Mostrando el: " + coleccion[contador])   # Así luego nos mostrará en cada línea cada elemento añadido.
print(coleccion)                                    # Lo curioso es que la agregación de esos 120 números a la lista en una única gran línea, solo ocurrirá la primera vez. No volverá a mostrarse en pantalla. Si se cambia el rango, nos saldrá "IndexError: list index out of range".

(print)

collection = []
x = 0

while x < 120:
    collection.append(f"elemento-{x}")
    print("Mostrando el: " + collection[x])         # la ['x'] es el número concreto que estamos recorriendo en la función 'while'.
    x += 1                                          # Para que siga iterando el bucle y no sea un bucle infinito.
asyncio.run(w8()), print(), print("______________________________________")



## método .upper y .lower ##
print('41- MEDIR UNA VARIABLE'), print(), asyncio.run(w8())
""" Ejercicio 3. Programa que compruebe si una variable esta vacía y en cuyo caso rellenarla con texto en minúsculas y mayúsculas.
"""
vacio = ""
if len(vacio.strip()) <= 0:             # Para eliminar todo posible espacio a la hora de comprobar la longitud de caracteres escritos.
    vacio = "el vacío es mi hogar"      # Llamando a la variable.
    print(vacio.upper())
    print(vacio.lower())
else:
    print(f"La variable tiene contenido {vacio}")
asyncio.run(w8()), print(), print("______________________________________")



## Isinstance y categorización de valores ##
print('42- ISINSTANCE'), print()
""" Ejercicio 4. Crear un script con 4 variables: lista, string, entero y booleano, imprimiendo además
un mensaje según el tipo de dato de cada variable usando funciones.
"""
# Función que diseña mejor el resultado del tipo de dato
def traducirTipo(tipo):                                     # Esta función, escrita al final, es para dar un resultado más realista.
    result = None
    if tipo == list:
        result = "LISTA"
    elif tipo == str:
        result = "CADENA DE TEXTO"
    elif tipo == int:
        result = "NÚMERO ENTERO"
    elif tipo == bool:
        result = "BOOLEANO"
    return result                                           # Recuerda que ni 'else' ni 'return' son funciones obligatorias a la hora de definir una condición (pero porque está 'elif' en el primer caso, si no no existiría condición alguna vaya).

# Función isinstance
def comprobarTipado(dato, tipo):            # Las funciones suelen quedar siempre arriba de los programas para siempre tenerlas disponibles. De esta manera comprobando el dato y el tipo la función nos dará un tipo de resultado u otro. Eso siempre y cuando no mencione todavía a las variables que están todavía por definirse.
    test = isinstance(dato, tipo)           # Esta función siempre buscará dos argumentos: el dato y su tipología (o al menos la tipología de la variable que queremos tener).
    result = ""
    if test:
        print(f"This data is from type {type(dato)}")          # Curiosidad: si no hubiera un ')' en el 'dato' incrustado, el cierra paréntesis final de la línea aparecería en verde pese a estar el entrecomillado justo antes del último caracter de la línea. Está en inglés para diferenciarlo del otro texto.
        result = f"Este dato es del tipo {traducirTipo(tipo)}" # La diferencia entre ambas no solo está en que 'print' y mostrar el resultado (el cual aparece su función más abajo en 'return') imprimen la misma tarea, también en la {incrustación} aparece con mucho mejor estilo el tipo de dato que es respecto a cómo sucede en la línea de arriba.
    else:
        result = None                       # "El tipo de dato no es correcto" sería un sustituto string más claro si cabe.
    return result                           # Devuelva el resultado.

# Variables
mi_lista = ["hola mundo", 77]
titulo = "Master en Python"
numero = 100
verdadero = True                            # Debajo de estas variables podríamos haber puesto las condiciones tanto de tipo como del isinstance. Pero no debajo de las llamadas a funciones, pues deben ser definidas antes de ser llamadas.

# Llamada a las funciones
print(comprobarTipado(mi_lista, list))      # Si no cambiásemos la variable o el tipo de dato para que correspondiesen con sus respectivas variables-datos, se ejecutaría la función 'else'.
print(comprobarTipado(titulo, str))
print(comprobarTipado(numero, int))
print(comprobarTipado(verdadero, bool))     
asyncio.run(w8()), print(), print("______________________________________")



## Diccionarios, tablas y recorridos 'for' ##
print('43- CREACION DE VARIABLES A PARTIR DE UN DICCIONARIO'), print(), asyncio.run(w8())
""" Ejercicio 5. Crear una lista con el contenido de esta tabla:
ACCION      AVENTURA            DEPORTES 
GTA         ASSASSINS CREED     FIFA 21
COD         CRASH               PRO 21
PUGB        PRINCE OF PERSIA    MOTO GP 21

Mostrar esta info ordenada (categoría y videojuego)
"""

tabla = [                                                       # Corchetes para tabla, llaves para diccionario.
    {
        "categoria": "ACCIÓN",
        "juegos": ["GTA", "Call Of Duty", "PUGB"]
    },
    {
        "categoria": "AVENTURA",
        "juegos": ["ASSASSINS CREED", "CRASH", "PRINCE OF PERSIA"]
    },
    {
        "categoria": "DEPORTES",
        "juegos": ["FIFA 21", "PRO 21", "MOTO GP 21"]
    }                                                           # Una vez hecha nuestra lista de diccionarios con listas de videojuegos a su vez en su interior, se deben mostrar ordenadamente. Para ello usaremos el bucle 'for'.
]
for categoria in tabla:
    print(f"---------{categoria['categoria']}---------")        # debe ser 'categoria' exactamente igual al índice asociativo que hemos metido dentro del diccionario "categoria".
    for juego in categoria['juegos']:                           # Dentro de cada una de esas categorías tiene varios juegos. Así que por cada categoría que tú pases por el 'for' principal debes hacer otro 'for' para mostrar el juego en sí.
        print(juego)                                            # De esta manera recorrerá la lista de juegos creando la variable "juegos" en cada vuelta que de a la lista.
asyncio.run(w8()), print(), print("______________________________________")



## Módulos y librerías. Funciones 'import', 'from' y  ##
print('44- MÓDULOS / LIBRERÍAS'), print(), asyncio.run(w8())    # Forma de empaquetar un código en módulo o librería para recuperar funcionalidades tantas veces como se necesite en cualquier parte del programa.
import mimodulo2                                   # La importación debe ubicarse en la misma carpeta de archivos, en el mismo directorio de carpeta.
print(mimodulo2.helloWorld("Swan"))                # Llamas a la librería y utilizas el método que desees (en este caso método pasa a ser la función que invocas desde tu módulo/librería) y luego si le otorgas ese valor de texto entre comillas el módulo tomará 'Swan' como el "nametag" (la variable) que aparece escrita en el archivo 'mimodulo2.py'.
# Al parecer no puedes importar un módulo desde otro módulo (si pusiésemos 'import asyncio' en 'mimodulo2' y luego importásemos 'mimodulo2' para utilizar la librería de 'asyncio' directamente no funcionaría. Pero para eso está la función 'from x import *' el cual sí que importaría las importaciones de una importación.
print(mimodulo2.calculadora(3,5,True))
from mimodulo2 import helloWorld                   # 'from' para importar una sola función de un módulo con varias funciones integradas.
from mimodulo2 import *                            # '*' equivale a importar absolutamente todo lo que haya en el módulo, errores incluidos (si los tuviere). Haciendo eso puedes realizar otras operaciones posteriores sin tener que llamar a tu otro archivo.
print(calculadora(4,8,True))                       # Ahora tras haber importado todo ('*'), podemos ejecutar la instrucción como si estuviera realmente aquí dentro del programa. Incluso estando cerrado el archivo a importar dentro de los archivos abiertos que tengamos en el Visual Code Studio.
asyncio.run(w8()), print(), print("______________________________________")



## Fechas y formateos de fecha ##
print('45- MÓDULO DE FECHAS'), print(), asyncio.run(w8())
import datetime
print(datetime.date.today())                # Sacar la fecha de hoy.
fecha_completa = datetime.datetime.now()    # Fecha completa, milisegundos incluido.
print(fecha_completa)
print(fecha_completa.year)                  # Así se accede a la propiedad '.year' (que es una variable dentro del objeto), mostrando solo el año.
print(fecha_completa.month)                 # Solo el mes, y '.day' solo el día...

fecha_personalizada=fecha_completa.strftime("%d/%m/%Y, %H:%M:%S")   # Para formatear fechas (colocar los datos en el orden que queramos):'%d' día, '%m' mes, '%Y' año, '%H' horas, '%M' minutos, '%S' segundos.
print("Mi fecha personalizá", fecha_personalizada)                  # Nos dará el resultado de la variable de arriba tras mostrar ese texto separado por una coma de lo que luego viene.
print(datetime.datetime.now().timestamp())                         # Saca la cifra temporal en Unix. Si pones "date.time.datetime.now().timestamp()", ese punto extra le hará pensar al programa que es una variable sin definir, y te dará error.
print(datetime.datetime.now().time())                              # El tiempo en otro formato.
asyncio.run(w8()), print(), print("______________________________________")



## Fechas y formateos de fecha ##
print('46- MÓDULO DE MATEMÁTICAS Y MÓDULO RANDOM'), print(), asyncio.run(w8())
import math
print("Raíz cuadrada de 10: ", math.sqrt(10))   # Respecto a las importaciones, Visual Studio Code autocompleta y sugiere distintas funciones tras poner 'math.'.
print("Número pi ", float(math.pi))             # Así saldrá lo mismo (dado que 'math.pi' es una función prediseñada del módulo 'math'), solo que cambiará el tipo de archivo al añadirle 'float' delante.
print("Redondear: ", math.ceil(6.5678))         # Redondeo al alza.
print("Redondear: ", math.floor(6.5678))        # Redondeo a la baja.

import random
print("Número aleatorio entre 15 y 67: ", random.randint(15, 67))   # Random integers entre esos rangos de número.
asyncio.run(w8()), print(), print("______________________________________")



## Paquetes de herramientas y módulos en un proyecto ##
print('47- PAQUETES E INSTALACIÓN DE PAQUETES'), print(), asyncio.run(w8())
# Paso 1: crear una carpeta donde incluirás diferentes archivos: 'pruebas.py', 'herramientas.py', 'main.py'
# Paso 2: llamar a un archivo '__init__.py' y dejarlo vacío. Así obtienes un módulo dentro de un paquete.
# Paso 3: puedes crear en otros archivos .py de distinto nombre funciones varias. De esta manera haces que cada archivo cumplimente una o diversas funciones concretas.
# Paso 4: para usar tus paquetes en el archivo o proyecto principal: 
# from "paquete" import "pruebas"
# from "paquete" import "herramientas"
# from "paquete" import "pruebas", "herramientas" haría lo mismo.
# Ello generará una carpeta de caché en Python dentro de la carpeta que hayas creado en el paso 1.
# 'pruebas.probando()' invocaría la función titulada 'probando' dentro del archivo 'pruebas'.
# Desde la web "pypi.org" se puede buscar e instalar cualquier tipo de paquete en Python. Buscas "pdf" y te salen diferentes bibliotecas populares, pudiendo ser un módulo o un paquete de módulos siguiendo el comando 'pip'.
asyncio.run(w8()), print(), print("______________________________________")



## Abrir y crear ficheros ##
print('48- FICHEROS'), print(), asyncio.run(w8())
# Dirigirse a la carpeta 02-sistema-archivos>>ficheros.py
asyncio.run(w8()), print(), print("______________________________________")



## Manejo de errores y excepciones: 'try', 'except', 'finally' ##
print('49- GESTIÓN DE ERRORES'), print(), asyncio.run(w8())
"""Capturar excepciones y manejar errores en código susceptible a fallos y/o errores"""

nombre = input("Cuál es tu nombre?: ")          # Introduces algo en el 'input' y sale luego en el 'print'.
print(nombre)                                   # Si introduces un 'enter' vacío o espacios sin más terminará su ejecución sin imprimir en pantalla este resultado pero sin darnos error tampoco.

if len(nombre) > 1:                             # Utilizando esta condición, si ahora introdujeses cero caracteres en el input o solo espacios daría error porque su longitud sería menor que 1 en lugar de mayor que 1 como está ahí escrito.
    nombre_usuario = "El nombre es " + nombre   # Aquí se recogería la variable global 'nombre' resultante del 'input' metido por el usuario.
print(nombre_usuario)                           # Si fuese 'print(nombre)', sucedería como está en el ejemplo de arriba, no estaría llamando a la función local 'nombre_usuario' dentro de la variable global pero también local en este caso, perteneciente a esta función 'nombre'.
# NameError: es como una excepción haciendo que el código sea susceptible a errores.

try:                                            # Con esta función integramos la variable con 'input' y la función anteriormente mencionada.
    nombre = input("Cuál es tu nombre?: ")
    if len(nombre) > 1:
        nombre_usuario = "El nombre es " + nombre
    print(nombre_usuario)                        
except:                                         # DDD
    print("Ha ocurrido un error.")              # Queda estéticamente mejor y es un mensaje más amable. Y lo más importante, no detendría el flujo de ejecución del programa.
else:                                           # DDD
    print("Todo ha ido dee lujoo")
finally:                                        # Detectar cuando ha terminado las funciones anteriores (try, if, except, else). Me parece una función suprimible a priori.
    print("Ya estaría")                         # Esta parte final siempre se ejecutará.
asyncio.run(w8()), print(), print("______________________________________")



## all is try and except ##
print('50- CAPTURA DE EXCEPCIONES'), print(), asyncio.run(w8())

listado= [21, 3, 2, 13, 34, 1, 5, 8]                # Retomando el ejercicio '39 LA LISTA QUE ME PARIÓ'.
def mostrarLista(numeros):
    resultado = ""
    for elemento in numeros:
        resultado += "Elemento: " + str(elemento)
        resultado += "\n"
    return resultado
print(mostrarLista(listado))

# Si el usuario introdujera letras en lugar de números
try:        # Si colocamos así el 'try' y el 'except' lograremos evitar que se interrumpa el flujo de ejecución ante una respuesta no deseada por parte del usuario.
    busqueda = int(input("Introduce el número a buscar: "))

    comprobar = isinstance(busqueda, int)
    while not comprobar or busqueda <= 0:
        busqueda = int(input("Introduce el número a buscar: "))
    else:
        print(f"Has introducido el {busqueda}")
    print(f"Buscar en la lista el número {busqueda}")



    search = listado.index(busqueda)        # Si una línea más arriba pusiésemos el 'try' y 'except' nos funcionaría en el caso de los números.
    print(f"El número buscado es el índice (ordenado): {search}")
except:
    print("El número no está en la lista, lo 100to")
asyncio.run(w8()), print(), print("______________________________________")



## Evitar múltiples errores ##
print('51- PREVER MÚLTIPLES EXCEPCIONES'), print(), asyncio.run(w8())
try:                                                                # Función susceptible de tratar posibles errores.
    numero = int(input("Número para elevarlo al cuadrado: "))
    print( "El cuadrado es: " +str(numero*numero))
except TypeError:                                                   # Si prevés que el sistema va a lanzar un tipo de error o de excepción concreta, se puede manipular a ese respecto.
    print("Debes convertir tu cadena a enteros en el código")
# except ValueError:                                                # Está comentado para que pueda funcionar la siguiente ejecución de comando de error que es más interesante y útil.
#    print("Introduce un número correcto: ")
except Exception as e:                                              # 'as' DDD. la 'e' es una variable cualquiera para designar a los 'errors'.
    print(type(e))                                                  # Imprimiría en pantalla <class 'x'>, el tipo de clase de error que nos daría.
    print("Pasó un error wey: ", type(e).__name__)                  # Si no tuviésemos el 'except' 'ValueError' activado nos indicaría con el 'type' de qué tipo de error estaríamos tratando.
asyncio.run(w8()), print(), print("______________________________________")



## Lanzar excepciones ##
print('52- EXCEPCIONES PERSONALIZADAS'), print(), asyncio.run(w8())
try:                                                        # Esta parte del try, escrita al final del código, sirve para que si ponemos una edad fuera del rango delimitado o un nombre de insuficiente longitud, podamos controlar la manera en que avisaría de los errores al usuario.
    nombre = input("Introduce el nombre: ")
    edad = int(input("Introduce la edad: "))                # El 'int' para convertir a enteros los números introducidos por el usuario debe ir antes/delante del 'input' y no después.

    if edad < 5 or edad > 110:
        raise ValueError("La edad introducida no es real")  # Para indicar tras el 'raise' qué tipo de error quiero (en este caso un error de valores, de datos introducidos por el usuario, no del código).
    elif len(nombre) <= 1:
        raise ValueError("El nombre no está completo")
    else:
        print(f"Bienvenido a un mundo sin errores {nombre}")
except ValueError:
    print("Introduce los datos correctamente")
except Exception as err:                                    # excepción as 'lo que sea' como excepción personalizada (si bien solo puede haber un tipo de error concreto, ya que en el caso de introducir veinte 'ValueError' distintos, funcionaría solo el último, al menos con los conocimientos actuales que tenemos).
    print("Existe un error: ", err)                         #
asyncio.run(w8()), print(), print("______________________________________")



## Definir una clase, principales propiedades, constructor de mundos ##
print('53- PROGRAMACIÓN ORIENTADA A OBJETOS: MÉTODOS Y CONSTRUCTOR'), print(), asyncio.run(w8())
"""ver archivos 'coche.py' y 'main.py' """
asyncio.run(w8()), print(), print("______________________________________")



## POO ##
print('54- PROGRAMACIÓN ORIENTADA A OBJETOS: HERENCIA'), print(), asyncio.run(w8())
"""ver archivo 'clases.py' """
asyncio.run(w8()), print(), print("______________________________________")