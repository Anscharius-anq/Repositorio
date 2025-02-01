## Introducción a la programación
---
### Conceptos.

&ensp; **Algoritmo:** Serie de intrucciones redactada para seguir una ruta con el propósito de solucionar problemas.
  
&ensp; **Dato:** es una representación simbólica (número, texto, símbolo, etc.) de una característica o atributo que, por sí solo, no tiene significado. Los datos son elementos básicos que se procesan para generar información cuando se les da contexto.
  
* Por ejemplo:
    * **42** es un dato, pero solo adquiere sentido si sabemos que representa la edad de una persona, un resultado matemático, o algo más específico.
    * **rojo** es un dato que, sin contexto, no indica si se refiere a un color, una advertencia, o un concepto abstracto.
  
    En resumen, un dato aislado es simplemente un valor que carece de significado intrínseco.
  
&ensp;  **Información:** Cuando un dato se asocia con otro o se interpreta dentro de un contexto, se convierte en información, ya que ahora tiene un significado claro.
  
* Ejemplos:
    * 42 años: la edad de una persona.
    * Auto rojo: la descripción de un vehículo.
  
&ensp; **Identificador:** Es el nombre que se asigna a un dato. Sirve como una etiqueta que permite referenciar una identidad.
  
* por ejemplo:
    * **x = 10**: El dato 10 se le asigna al identificador x. Sin embargo, 10 sigue siendo solo un valor sin significado específico.
    * **edad = 10**: Ahora, al usar el identificador edad, el dato 10 adquiere el contexto de "años".
    * **cantidad = 10**: Ahora, el dato 10 se refiere a una cantidad de unidades de algo.
  
&ensp; Es importante utilizar nombres que tengan sentido.
  
&ensp; **Variable y constantes:** Una variable es un conjunto formado por:
  
1. **Dato:** El valor que se almacena.
2. **Identificador:** El nombre usado para referirse al dato.
3. **Espacio en memoria:** El lugar donde se almacena el dato en la computadora
  
&ensp; Las variables pueden cambiar su valor durante la ejecución del programa, mientras que las constantes tienen un valor fijo que no puede ser modificado después de su definición.
  
---
### Tipos de datos 
  
&ensp; **String (str):** Un string es un conjunto de caracteres que puede incluir letras, números, símbolos y espacios, es decir, texto. Los strings se delimitan con comillas simples (') o dobles (")
  
```python
    animal = "chancho" -> str
    numero = "1234" -> str
```
&ensp; Aunque "1234" parezca un número, sigue siendo un string porque está entre comillas y el programa de ejecución lo reconocerá como cadena de texto y no como número realmente.
  
&ensp; **Integer (int):** Un entero, Integer del inglés, es un tipo de dato que representa números enteros, es decir, números sin decimales. Pueden ser positivos, negativos o cero.
  
```python
    numero = 36 -> int
    negativo = -21 -> int
```
&ensp; **Float:** es un tipo de dato numérico que contiene decimales, se utiliza punto (**.**) y no comas (**,**) para los decimales.
  
```python
    precio = 4.99 -> float
```
&ensp; En este caso, 4.99 es un número con decimales, por lo que se almacena como un float en la variable precio.
  
&ensp; **Boolean (bool):** es un tipo de dato que solo puede tener uno de dos valores posibles: **True** (verdadero) o **False** (falso). Se utiliza comúnmente para representar condiciones lógicas en los programas.
  
```python
    feliz = True -> bool
    llueve = False -> bool
```
  
  
&ensp; **Carácter (char):** Consiste en un tipo de dato que solo tiene un carácter. *Realmente se usa muy poco.*
```python
    caracter = "a" -> char
```
  
---
### Funciones
  
&ensp; antes de comenzar, veamos un ejemplo de algoritmo:
  
**entrar a la casa**:
1. Acercarse a la puerta.
2. Levantar la mano.
3. Tomar la manilla.
4. Girar la manilla hacia la izquierda.
5. Empujar la puerta.
6. Soltar la manilla.
7. Caminar hacia adelante.
8. Darse la vuelta en 180 grado.
9. Levantar la mano.
10. Tomar la manilla
11. Empujar la puerta suavemente hacia el tope.
  
&ensp; estas son las instrucciones para entrar a la casa, si quisiéramos ejecutar esta acción "entrar a la casa" varias veces tendríamos que escribir estas líneas reiteradas veces lo que lo hace lento y difícil de mantener puesto que revisaríamos una tras otras las reiteradas ocurrencias donde aparece las instrucciones que queremos modificar. Afortunadamente, existe las funciones que recuerdan el algoritmo que escribimos, luego solo hace falta *llamarlas* para ejecutar las instrucciones. 
  
Entonces, Una función nos permite reutilizar algoritmos que hemos construido.
  


```pseudocode
function entrar_a_la_casa():
    1. Acercarse a la puerta.
    2. Levantar la mano.
    3. Tomar la manilla.
    4. Girar la manilla hacia la izquierda.
    5. Empujar la puerta.
    6. Soltar la manilla.
    7. Caminar hacia adelante.
    8. Darse la vuelta en 180 grados.
    9. Levantar la mano.
    10. Tomar la manilla.
    11. Empujar la puerta suavemente hacia el tope.

entrar_a_la_casa():
```
&ensp; en *function* hemos definido la funcion que se ejecutará cada vez que le llamemos, en este caso para entrar a la casa sería: entrar_a_la_casa():

&ensp; otro ejemplo

```pseudocode
function entrar_a_la_casa():
    1. Acercarse aa la puerta.
    2. patear muy fuerte la puerta.
    3. caminar hacia adelante.
```
&ensp; la funcion cumple con entrar a la casa, pero evidentemente es muy mala solución, por lo tanto muy mal algoritmo.

---
### Programación orientada a objetos (OOP)

&ensp; es un paradigma de programación que es una forma de filosofía en cuanto en resolver en algo. Se basa en el uso de **clases** son como plantillas para crear **objetos**. por ejemplo las personas tienen **atributos** (caracteristicas) tales como: nombre, edad, color de pelo:

```pseudocodigo
Personas {
    nombre: string
    edad: integer
    color_cabello: string
}
```
&ensp; En el ejemplo anterior, la **clase** es personas con **atributos** como **nombre, edad, color_cabello**, entones Personas son los planos para crear una persona. Ahora creemos personas:

```pseudocodigo
class Personas {
    nombre: string
    edad: integer
    color_cabello: string
}

persona_1 = new Personas(
    nombre = "Juan"
    edad = 36
    color_cabello = "castaño"  
)
```
ahora, hemos creado un objeto con la variable persona_1, este objeto tiene sus atributos: Juan, 36, castaño. entonces **persona_1** se creo con **Personas**, de manera mas tecnica: **Persona_1 es una instancia de Personas**

&ensp; Decimos entonces que un objeto es una instancia de clase.

...


*"No seguiré con esto por que lo explico de manera mas completa en lenguaje python: [Clases Apuntes](notebooks/clases_python.md)."*

