# Regular expression
---
El módulo re o RegEx en Python proporciona herramientas para trabajar con expresiones regulares, lo 
que permite la búsqueda, comparación y manipulación de patrones(texto) de manera eficiente. Es una herramienta 
útil para detectar patrones en cadenas de caracteres.


## Módulo re

```python
import re
```

## Funciones importantes

* `re.match(pattern, string, flags=0)`: Busca el patrón de un string desde al princio (índice 0). Si
    encuentra una coincidencia, devuelve un objeto *match*; de lo contrario, devuelve *none*

 **ejemplo:**

```python
import re

txt = '''Python is the most beautiful language that a human being has ever 
created. I recommend python for a first programming language'''

match = re.match("Python is the most", txt)
print(match) # <re.Match object; span=(0, 18), match='Python is the most'>

span = match.span()
print(span) # (0, 18)

start, end = span
print(start, end) # 0 18

substring = txt[start:end]
print(substring) # Python is the most
```
<br>

* `re.search(pattern, string, flags=0)`:Busca en toda la cadena hasta encontrar dl primer patrón. 
Devuelve un objeto *match* si hay coincidencia; de lo contrario, devuelve *None*.

 **ejemplo:**

```python
import re

txt = '''Python is the most beautiful language that a human being has ever 
created. I recommend python for a first programming language'''


match = re.search('first', txt, re.I)
print(match)  # <re.Match object; span=(100, 105), match='first'>

span = match.span()
print(span) # (100, 105)

start, end = span
print(start, end) # 100 105

substring = txt[start:end]
print(substring) # first
```
<br>

* `re.findall(pattern, string, flags=0)`: Retorna una lista con todas las coincidencias en la cadena.
Si no hay coincidencias, devuelve una lista vacía [].

 **ejemplo:**

```python
import re

txt = '''Python is the most beautiful language that a human being has ever 
created. I recommend python for a first programming language'''

matches = re.findall('Python|python', txt)
print(matches)  # ['Python', 'python']

matches = re.findall('[Pp]ython', txt)
print(matches)  # ['Python', 'python']    
```
<br>


* `re.sub(pattern, repl, string, count=0, flags=0)`: reemplaza uno o varios patrones con un string
    * `pattern`: Expresión regular que define lo que se va a reemplazar.
    * `repl`: Lo que va a reemplazar la coincidencia. Puede ser una cadena o una función.
    * `string`: La cadena en la que se buscarán coincidencias y se harán reemplazos.
    * `count`: (Opcional) Número máximo de reemplazos a realizar. Por defecto es 0 (todos).
    * `flags`: (Opcional) Modificadores como re.IGNORECASE, re.MULTILINE, etc.

**ejemplo:**

```python
txt = '''Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language'''

match_replaced = re.sub('Python|python', 'JavaScript', txt)
print(match_replaced)  # JavaScript is the most beautiful language that a human being has ever created.
# OR
match_replaced = re.sub('[Pp]ython', 'JavaScript', txt)
print(match_replaced)  # JavaScript is the most beautiful language that a human being has ever created.
```
**ejemplo:**
```python
txt = '''%I a%m te%%a%%che%r% a%n%d %% I l%o%ve te%ach%ing. 
T%he%re i%s n%o%th%ing as r%ewarding a%s e%duc%at%i%ng a%n%d e%m%p%ow%er%ing p%e%o%ple.
I fo%und te%a%ching m%ore i%n%t%er%%es%ting t%h%an any other %jobs. 
D%o%es thi%s m%ot%iv%a%te %y%o%u to b%e a t%e%a%cher?'''

matches = re.sub('%', '', txt)
print(matches)
```
```plain text
I am teacher and I love teaching.
There is nothing as rewarding as educating and empowering people. 
I found teaching more interesting than any other jobs. Does this motivate you to be a teacher?
```
<br>

* `re.split`: Divide la cadena en una lista, usando el patrón como delimitador.

```python
txt = '''I am teacher and  I love teaching.
There is nothing as rewarding as educating and empowering people.
I found teaching more interesting than any other jobs.
Does this motivate you to be a teacher?'''

print(re.split('\n', txt)) # divide usando \n que son los saltos de lineas implicitos del texto
```
```plain text
['I am teacher and  I love teaching.', 'There is nothing as rewarding as educating and empowering people.', 'I found teaching more interesting than any other jobs.', 'Does this motivate you to be a teacher?']
```

## Expresiones regulares 

aqui se muestran las expresiones más comunes.

|Patrón	|Descripción|
|-------|-
|\d     | Dígito (0-9)
|\D     | No es un dígito
|\w     | Caracter alfanumérico (letras y números)
|\W     | No es alfanumérico
|\s     | Espacio en blanco (espacio, tabulación, salto de línea)
|\S     | No es un espacio en blanco
|.      | Cualquier caracter excepto nueva línea
|^      | Inicio de la cadena
|$      | Final de la cadena

Se puede encontrar más expresiones en este [link](https://github.com/Anscharius-anq/30-Days-Of-Python/blob/master/images/regex.png)


## Principales flags
 `flags`  modifica el comportamiento de la búsqueda y permite mayor flexibilidad en el uso de expresiones regulares.


|Flag                |	Descripción
|--------------------|-
|`re.IGNORECASE` `(re.I)`| Hace que la búsqueda ignore mayúsculas y minúsculas.
|`re.MULTILINE` `(re.M)` | Permite que ^ y $ coincidan con el inicio y fin de cada línea, no solo de toda la cadena.
|`re.DOTALL` `(re.S)`    | Hace que . coincida con cualquier carácter, incluyendo saltos de línea.
|`re.VERBOSE` `(re.X)`   | Permite escribir expresiones regulares con espacios y comentarios para mayor legibilidad.
|`re.ASCII` `(re.A)`     | Hace que \w, \d y \s solo coincidan con caracteres ASCII en lugar de Unicode.

Las banderas pueden combinarse usando el operador `|`:
**por ejemplo**
```python
resultado = re.match(r'hello', 'HELLO world', re.IGNORECASE | re.MULTILINE)
```

