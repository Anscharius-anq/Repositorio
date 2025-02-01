## Clases
---
*Aqui escrbiré unos apuntes para aprender la programacion orientada a objetos <b>OOP</b>. aqui repasaré la sintaxis de una clase, y conceptos como encapsulamientos, herencia de clase, etc.*

---
###   1. Sintaxis de una clase

&emsp;&emsp; En la programación orientada a objetos, un objeto es una instancia de una clase. Es decir, un objeto es una entidad que se crea a partir de la plantilla definida por una clase. Cada vez que instanciamos una clase, estamos creando un nuevo objeto con su propio conjunto de atributos y métodos.

* ***Definición clave***

    * **Clase:** Es un plano o plantilla que define los atributos y métodos comunes para los objetos que serán creados a partir de ella.
   
    * **Objeto (Instancia):** Es una instancia específica de una clase, con atributos y comportamientos definidos por la clase, pero con valores particulares para sus atributos.



&emsp;&emsp; Aquí se muestra la sintaxis basica para escribir una clase. Para definirla se escribe **class NombreClase():**

```python

class Coche():  # Definición de la clase
    '''Esta clase define el estado y comportamiento de un coche'''  # Docstring

    ruedas = 4  # Atributo de clase (valor compartido por todas las instancias)

    def __init__(self, color, aceleracion):  # Método constructor
        # Atributos de instancia (valores únicos para cada objeto instanciado)
        self.color = color
        self.aceleracion = aceleracion
        self.velocidad = 0

    # Métodos de la clase
    def acelera(self):
        """Incrementa la velocidad del coche"""
        self.velocidad += self.aceleracion

    def frena(self):
        """Reduce la velocidad del coche hasta 0 como mínimo"""
        v = self.velocidad - self.aceleracion
        self.velocidad = max(v, 0)
```

* **class**  es la palabra reservada utilizada para crear una clase.
* En este ejemplo, usamos **Coche** como identificador (nombre). Por convención, los nombres de las clases utilizan **mayúsculas iniciales** en las palabras y camel case para nombres compuestos o acrónimos.
* Los paréntesis **()** son opcionales, excepto cuando la clase hereda de otra clase.de clase. 
* **docstring**  Es una cadena de texto utilizada para documentar la clase, es decir, explicar su funcionalidad.
* **Atributos** son variables o datos definidos dentro de la clase.
* **Métodos** son funciones definidas dentro de una clase que operan sobre sus atributos y realizan acciones.<br>

---
###  2. Objetos 

&emsp;&emsp; Los objetos son elementos creados a partir de una clase, estos tienen todos los atributos y metodos de la clase a la que pertenecen Además, los objetos pueden tener atributos propios que no están definidos directamente en la clase. los objetos son creados comumente a traves de variables que nos permita manejar el objeto con un identificador asignado.<p>

* ***Características de los objetos***
    * Los objetos son instancias de una clase
    * Permiten manejar datos y comportamientos definidos en la clase.
    * Se crean comúnmente asignándolos a una variable, que actúa como identificador

* ***Cómo crear un objeto***
    * La sintaxis básica para crear un objeto es:

        * **variable = Clase()**

    * En el ejemplo de abajo:

        * **obj = NombreClase()**
    
```python
# Declaración de clase
class NombreClase:

    # Atributos de clase
    atributo_1 = "valor 1"
    atributo_2 = "valor 2"

    # Métodos de clase
    def metodo_1(self):
        print("Método llamado con el objeto.")

# Objeto creado a partir de la clase
obj = NombreClase()

# Llamado del método. Recordar usar paréntesis, ya que un método es una función.
obj.metodo_1()  # Salida: Método llamado con el objeto.
```
#### &emsp;&emsp; Estados y Comportamientos de los Objetos

* Los objetos pueden poseer tanto estados como comportamientos, que se reflejan a través de sus atributos y métodos.


    * **El estado** de un objeto está representado por sus atributos, que son los datos que lo caracterizan. Por ejemplo, un objeto que represente un usuario podría tener los siguientes atributos: 
        * nombre
        * apellido
        * edad
        * teléfono
        * dirección
        * etc

    * **Los comportamientos** El comportamiento de un objeto está representado por sus métodos, que son las acciones que puede realizar. Por ejemplo:
        * caminar()
        * correr()
        * saltar()
        * comer().
        * etc.
    * Otro  ejemplo en una aplicacion web los usarios pueden tener comportamiento como:
        * consultar_datos()
        * cambiar_contraseña()
        * inicia_sesion()
        * cierra_sesion()
        * eliminar_cuenta()

**Ejemplo práctico:** Jugador con estado y comportamiento.
*se crea dos objetos de tipo Jugador*
```python
class Jugador():
    # Atributos de clase
    edad = None

    # Método
    def permitir_acceso(self):
        print("Puedes entrar.")

    def denegar_acceso(self):
        print("No puedes entrar.")

    def comprobar_edad(self):
        if self.edad < 18:
            self.denegar_acceso()
        else: 
            self.permitir_acceso()

# Instanciamos dos objetos de tipo Jugador
jugador1 = Jugador()
jugador2 = Jugador()
# se modifica el atriburo edad (None) para cada objeto y no de la clase
jugador1.edad = 15
jugador2.edad = 60

# Acceder un método
jugador1.comprobar_edad() # No puedes entrar.
jugador2.comprobar_edad() # Puedes entrar.
```

---

### 3. Acceso a atributos y métodos

* **Instanciación de objetos:** Los objetos se crean en tiempo de ejecución y se almacenan en la memoria RAM. Cada objeto tiene una dirección de memoria única que se asocia con él durante la ejecución.

* **Acceso a atributos:** Los atributos de los objetos se acceden mediante la sintaxis *objeto.atributo*. Se pueden modificar directamente o crear nuevos atributos específicos para cada objeto.

* **Precaución con atributos fuera de la clase:** Aunque Python permite crear atributos fuera de la clase, esto puede prestarse a confusiones que provocarian errores, especialmente si se manejan múltiples objetos. Es recomendable definir todos los atributos dentro de la clase para evitar inconsistencias.

```python
class Vehiculo:
    color = None 
    longitud_metros = None
    ruedas = 4

    def arrancar(self):
        print("El motor ha arrancado")

    def detener(self):
        print("El motor está detenido")


# Se instancia dos objetos de tipo Vehiculo
objeto_vehiculo_1 = Vehiculo()
objeto_vehiculo_2 = Vehiculo()

# Se crea los objetos
print(objeto_vehiculo_1)  # Salida: <__main__.Vehiculo object at 0x000001E755FBFE00>
print(objeto_vehiculo_2)  # Salida: <__main__.Vehiculo object at 0x000001E755F9FD90>

# Acceder a los atributos de un objeto. Se indica: nombredelobjeto.atributo
print(objeto_vehiculo_1.ruedas)  # Salida: 4

# Almacenar externamente valores de los objetos
rueda_vehiculo = objeto_vehiculo_1.ruedas  # Se almacena el atributo rueda en una variable
print(rueda_vehiculo)  # Salida: 4

# Reasignar valores a los atributos de los objetos
print(objeto_vehiculo_1.color)  # Salida: None
objeto_vehiculo_1.color = "Negro"  # Reasignación de valor del atributo para este objeto
print(objeto_vehiculo_1.color)  # Salida: Negro

# Crear atributos para el objeto inexistente en la clase
objeto_vehiculo_1.velocidad_maxima = 161  # Atributo creado para este objeto
print(objeto_vehiculo_1.velocidad_maxima)  # Salida: 161

```
&emsp;La salida **`print(objeto_vehiculo_1)`** de un objeto en Python da un resultado como **`<__main__.Vehiculo object at 0x000001E755FBFE00>`**, este tiene el siguiente significado:

* **`__main__`** Este es el nombre del módulo donde se ejecuta el código. Si el código se ejecuta directamente desde un archivo *(por ejemplo, python archivo.py)*, **`__main__`** es el nombre del módulo principal.

* **`Vehiculo`** Es el nombre de la clase del objeto que se imprime. En este caso, es una instancia de la clase **`Vehiculo`**.

* **`object`** Es un término genérico que indica que lo que se está imprimiendo es un objeto.

* **`at 0x000001E755FBFE00`** Esta es la dirección de memoria donde está almacenado el objeto en la memoria RAM. Cada vez que se crea un objeto, Python le asigna una ubicación en la memoria y esa dirección es única para cada objeto en particular. La dirección 0x000001E755FBFE00 es una representación hexadecimal de esa ubicación en la memoria. Python lo imprime para indicar dónde está guardado el objeto.<br>

---
### 4. El método init y el parámetro especial self.

#### &emsp; 4.1 Método init

 &emsp; El método **`__init__`** es un método especial que actúa como el constructor de una clase. Su principal propósito es dar un estado inicial al objeto esto permite que tenga sus propios valores de atributos en el momento de instanciar (crear) el objeto.

 &emsp; No necesita ser llamado explcitamente. Pues el metodo **`__init__`** se invoca automaticamente por el interprete de python cuando se crea una nueva instacia de clase, es decir, en el tiempo de ejecución. 

**Ejemplo:** sin usar el método **`__init__`**.

```python
class Usuario:
# atributos 
    nombre = "Sin Nombre"
    apellido = "Sin apellido"
    edad = 0 
    direccion = "Sin direccion"
    telefono = "Sin telefóno"

    # metrodos
    def iniciar_sesion(self):
        print("El usuario ha iniciado sesión")
    def cerrar_sesion(self):
        print("El usuario ha cerrado sesión")
    def cambiar_nombre_perfil(self):
        print("SE cambió el nombre")

# instanciación
usuario_1 = Usuario()
# inicializacion de datos 
usuario_1.nombre = "Pedro"
usuario_1.apellidos = " Fernandez"
usuario_1.edad = 32
usuario_1.direccion = "C/program/carpeta_x"
usuario_1.telefono = "123456"
```
&emsp; Evidentemente, en el ejemplo anterior, crear varios objetos de la clase **`Usuario`** llevaría demasiadas líneas de código. Para optimizar este proceso de construcción inicial de los objetos, se utiliza el método **`__init__`**, que resulta mucho más sencillo y práctico. Sin embargo, antes de profundizar en su uso, es importante diferenciar entre los **atributos de clase** y los **atributos de instancia**


&emsp; **Los atributos de clase:** son los los atributos que hemos creados hasta ahora, están sueltos en el cuerpo de la clase. Estos atributos comparten un mismo valor entre todas las instancias de la clase, salvo que se sobrescriban en una linea específica que la modifique. en el ejemplo anterior si defines un atributo como **`nombre = "Sin nombre"`** dentro de la clase **`Usuario`**, todos los objetos instanciados de la clase Usuario tendrán inicialmente el mismo valor **`"Sin nombre"`** para el atributo nombre.
```python
class Usuario:
    # atributo de clase  
    nombre = "Sin nombre"

persona_1 = Usuario() 
```


&emsp; **Atributos de instancia:** Son atributos que se asignan y personalizan para cada instancia específica al momento de crearla. Estos atributos se definen típicamente dentro del método **`__init__`** y pueden recibir valores únicos para cada objeto.

sintaxis para el metodo **`__init__`**

```python
def __init__(self, parametro_1, _5)
self.atributo_1 = parametro_1
self.atributo_2 = parametro_2
self.atributo_3 = parametro_3
self.atributo_4 = parametro_4
self.atributo_5 = parametro_5
```
&emsp;  En general, la sintaxis para designar los atributos es la siguiente manera: **`self.atributo = parametro`**. Suele ser mejor poner el mismo nombre para el atributo y el parametro esto le da mucho mas legibilidad al codigo.

**ejemplo** utilizando metodo **`__init__`*** 
*esta vez usamos el código anterior usando el método constructor. Con el metodo **`__init__`** podemos dar un estado inicial a los atributos de los objetos en la propia instanciación*

```python
class Usuario:
    # atributo de clase
    hora_ultima_sesion = None

    # método constructor   
    def __init__(self, nombre, apellido, 
                 edad, direccion, telefono):  
    # atributos de instancia
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.direccion = direccion
        self.telefono = telefono
    
    def iniciar_sesion(self):
        print("El usuario ha iniciado sesión")
    def cerrar_sesion(self):
        print("El usuario ha cerrado sesión")
    def cambiar_nombre_perfil(self):
        print("Se cambió el nombre")


# crear un objeto 
usuario_1 = Usuario.__init__("Pedro", "Fernandez", 
                    32, "C/program/carpeta_x", "123456")

print(usuario_1.nombre)
```
*tambien es posible resignar los valores de los atributos de instancia como los atributos de clase.*
 
```python
# Estado inicial a los atributos de instancia
usuario_1 = Usuario("Pe(dro", "Fernandez", 
                    32, "C/program/carpeta_x", "123456")

# reasignaciones 
usuario_1.nombre = "Quique" # reasignando atributo de clase
usuario_1.hora_ultima_sesion = ("10/01/2025") # reasignando atributo de instancia

# probar atributos
print(usuario_1.nombre) # Salida: Quique
print(usuario_1.hora_ultima_sesion) # Salida: 10/01/2025
```

**Ejemplo:** en el caso, si queremos inicializar el atributo nombre.
*El metodo init nos obliga inicializar los objetos con todos parámetros que se especifiquen en la clase.*

```python
usuario_2 = Usuario(nombre = "Enrique") # TypeError 
```
<br>

#### 4.2. self

&emsp; self es un parámetro que debe estar en la primera posición en los métodos y en el **`__init__`** , puesto no ponerlo resultará en 0error al llamar un método sin self. 

```python
class Clase:

    def metodo_sin_self():
        print("no se ejecutrá")

objeto_1 = Clase()

# llamando el método sin el self como parametro
objeto_1.metodo_sin_self() # TypeError: Clase.metodo_sin_self() takes 0 positional arguments but 1 was given
```

&emsp; Al llamar la funcion <b>`metodo_sin_self()`</b> resultará en un error de argumeto posicional, aqui aparace que el método no tiene argumentos(correcto por que no le hemos puesto un parámetro) pero en el error si aparece que fue añadido un argumento al llamarlo, esto es raro por que en la llamada no hemos puesto nada. sin embargo, el interprete de Python si lo ha hecho, ha pasado un argumento para self. entonces se debe colocar siempre el parámetro self para que necesita para funcionar inaternamete de manera correctamente.

&emsp; El parámetro <b>`self`</b> sirve para representar a los propios objetos creados a partir de cierta clase, gracias a esto podemos acceder mediante él a los atributos y métodos de una clase. Sin <b>`self`</b> los métodos de una clase no tendrían forma de saber a qué instancia de la clase se están aplicando, es decir, es decir en el código general de la clase "la plantilla" para todos los objetos y gracias a ese self el interprete de Python apunta de manera correcta a cada objeto.

&emsp; El nombre self no es una palabra reservada de python si no mas bien es una convención, osea puede tomar cualquier nombre, pero se usa el nombre self simplemente.

&emsp; <b>Por ejemplo:</b> si llamo a <b>`usuario_1.iniciar_sesion`()</b> pues con el self se sabrá con que objeto se está llamando este método, self se emplea como comodín para remplazarse por el objeto con el que se llama a un atributo de la clase o a un método dento de ella.

```python
class Usuario:
    # atributo de clase
    hora_ultima_sesion = None

    # atributos de instancia
    def __init__(self, nombre, apellido, 
                 edad, direccion, telefono):  
    
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.direccion = direccion
        self.telefono = telefono
    # aqui he modificado iniciar_sesion() para que muestre el nombre del usuario de la instancia en el mensaje.
    def iniciar_sesion(self):
        print(f"{self.nombre} ha iniciado sesión")
    def cerrar_sesion(self):
        print("usuario ha cerrado sesión")
    def cambiar_nombre_perfil(self):
        print("Se cambió el nombre")


# creando el objeto
usuario_2 = Usuario("Adriana", "Lopez", 28,
                     "sin dirección", "987654321")
```

Una vez instanciado `usuario_2` de tipo `Usuario` se puede llamar algún método:

* cuando llamamos un método con un objeto usualmente se realiza de la siguiente forma: **`usuario_2.metodo(argumentos)`**

```python
        usuario_2.iniciar_sesion()
```
* Sin embargo Python convierte esa llamada en esto: **`clase.metodo(usuario_2, argumentos)`**. aquí el identificador usuario_2 como argumento corresponde al parámetro self
```python
        Usuario.iniciar_sesion(usuario_2) 
```


Se concluye que self automatiza y simplfica la sintaxis, ya que si no se tendría que indicar el objeto cada vez que se llama a un método. entonces self referencia al objeto.

---
### 5. Herencia

&emsp;&emsp; La herencia de clases permite crear nuevas clases que posean características y funcionalidades de otras clases sin repetir código innecesariamente.

&emsp;&emsp; En herencia, se le llama **`clase base`** a la clase principal; también se conoce como clase madre o **`superclase`**. Por otro lado, la **`clase derivada`** es la clase que hereda de la base; también se denomina clase hija o **`subclase`**. La sintaxis para crear una herencia es la siguiente:
```python
class NombreSubclase(NombreSuperclase):
    # Código de la subclase
    # (NombreSuperClase) se herederá la clase 
```

**Ejemplo:** Sin utilizar herencia.
```python
class Ciudadano:
    def __init__(self, nombre, profesion):
        self.nombre = nombre
        self.profesion = profesion
    
    def saludar(self):
        print(f"Hola, soy {self.nombre}. Mi profesión es {self.profesion}")


class Medico:
    def __init__(self, nombre):
        self.nombre = nombre 
        self.profesion = "médico"

    def saludar(self):
        print(f"Hola, soy {self.nombre}. Mi profesión es {self.profesion}")


a = Ciudadano("María", "informática")
b = Medico("Javier")

a.saludar() # Salidad: Hola, soy María. Mi profesión es informática
b.saludar() # Salida: Hola, soy Javier. Mi profesión es medico
```
&emsp;&emsp;  El problema aquí es que está repitiendo mucho código. ambas clases (Ciudadano y Medico) son muy similares, pero el código se repite innecesariamente. Al crear instancias de ambas clases, se observa que tienen métodos y atributos redundantes. Para evitar esta repetición, se puede hacer que la clase Medico herede de la clase Ciudadano. Esto permite reutilizar el método  **`__init__`** y el método saludar de la superclase. La subclase solo necesita especificar el valor predeterminado para profesion

**Ejemplo:** Ahora utilizamos herencia.
```python
lass Ciudadano:
    def __init__(self, nombre, profesion):
        self.nombre = nombre
        self.profesion = profesion
    
    def saludar(self):
        print(f"Hola, soy {self.nombre}. Mi profesión es {self.profesion}")


class Medico(Ciudadano): # la clase heredará todo de la clase Ciudadano
    def __init__(self, nombre):
        super().__init__(nombre, "médico")

class Policia(Ciudadano):
    def __init__(self, nombre): # la clase heredará todo de la clase Ciudadano
        super().__init__(nombre, "policía")

    def pedir_refuerzos(self): # nuevo método de la subclase
        print("Llamada a todas la unidades.")



persona_2 = Ciudadano("Ana", "informática")
persona_1 = Medico("Raúl")
persona_3 = Policia("Raquel")

persona_1.saludar() 
persona_2.saludar() #  el objeto de la subclase Medico llama a un método de la superclase Ciudadano
persona_3.saludar() # el objeto de la subclase Policia llama a un método de la superclase Ciudadano

persona_3.pedir_refuerzos() # llamada al método propio de la subclase
```
&emsp;&emsp; La función **`super()`** es una función predefinida en Python que se utiliza para acceder a métodos y atributos de la superclase desde una subclase. En este ejemplo,**`super()`** permite inicializar el método **`__init__`** de la superclase Ciudadano, evitando repetir código en las subclases. Por ejemplo, en la subclase Medico, el método **`__init__`** llama al de la superclase, pasando un valor predefinido "médico" como segundo argumento:
```python
class Medico(Ciudadano):  # La clase hereda todo de la clase Ciudadano
    def __init__(self, nombre):
        # super() llama al método constructor de la superclase
        super().__init__(nombre, "médico") # el parámetro médico sobreescribe al parárameto nombre de la superclase.

persona_1 = Medico("Raúl")
```
&emsp;&emsp; De este modo, al crear una instancia de Medico [ por ejemplo, **`Medico("Raúl")`** ], no es necesario especificar el valor de la profesión manualmente, ya que está establecido como **"médico"** dentro de la subclase.

&emsp;&emsp; Además, las subclases pueden agregar nuevos métodos específicos para diferenciarse de la superclase. En este caso, **`Policia`** incluye un método adicional llamado **`pedir_refuerzos`**. Al crear una instancia de Policia, esta puede usar tanto los métodos heredados como el nuevo método definido en la subclase.

```python
class Policia(Ciudadano):
    def __init__(self, nombre):
        super().__init__(nombre, "policía")

    def pedir_refuerzos(self): 
        print("Llamada a todas la unidades.")

```
---

### 6. sobreescritura.

&emsp;&emsp; La sobrescritura de atributos y métodos en herencia permite personalizar o modificar el comportamiento de una subclase, basándose en una superclase. Para ello, simplemente se define un atributo o método con el mismo nombre que el de la superclase dentro de la subclase. De esta forma, el elemento de la subclase reemplaza al de la superclase.

&emsp;&emsp;Esto es útil para crear variaciones específicas en métodos o atributos heredados, ajustándolos a las necesidades de la subclase.

```python
class Ciudadano:
    def __init__(self, nombre, profesion):
        self.nombre = nombre
        self.profesion = profesion
    
    def saludar(self):
        print(f"Hola, soy {self.nombre}. Mi profesión es {self.profesion}")


class Medico(Ciudadano): # la clase heredará todo de la clase Ciudadano
    def __init__(self, nombre):
        super().__init__(nombre, "médico")


class Policia(Ciudadano):
    def __init__(self, nombre):
        super().__init__(nombre, "policía")
    # sobrescribiendo el método saludar
    def saludar(self):
        print("En la oscuridad, la luz brillará. En la injusticia, la ley" \
               " prevalecerá. siempre serviré y protegeré.")



policia_1 = Policia("Raquel")
medico_1 = Medico("Ana")


policia_1.saludar() # En la oscuridad, la luz brillará. En la injusticia, la ley prevalecerá. siempre serviré y protegeré. 
medico_1.saludar() # Hola, soy Ana. Mi profesión es médico  
```
---

### 7. Tipos de herencia

&emsp;&emsp; La herencia en programación orientada a objetos se clasifica en diferentes tipos según la relación entre las clases y el número de clases involucradas. Estos tipos permiten organizar el diseño del código dependiendo de las necesidades del sistema. estas son:

* Herencia simple o única.
* Herencia múltiple.
* Herencia Multinivel.
* Herencia Jerárquica.
* Herencia  Híbrida.

#### 7.A Antes de comenzar: la clase object

&emsp;&emsp; En Python, todas las clases (ya sean predeterminadas o creadas por el usuario) heredan implícitamente de la clase object. Esta es la clase raíz o la superclase de todas las clases en Python. Aunque no se vea explícitamente en la mayoría del código, cada clase en Python está directamente o indirectamente relacionada con la clase object.

```python
class MiClase:
    pass  
```
Aunque parece que esta clase Clase no hereda de nada, de hecho hereda de la **clase object** de manera implícita. de 


```python
class MiClase(object):
    pass   
# esto realmente no afeca el código, puesto es lo que realmente lo que sucede en el código.
```
&emsp;&emsp; Aquí hemos declarado explícitamente que Clase hereda de object. Sin embargo, este código no cambia el comportamiento de la clase, ya que todas las clases en Python heredan de object de manera predeterminada, incluso si no se especifica.

&emsp;&emsp; La clase object proporciona varios métodos predeterminados que pueden ser utilizados o sobrescritos por las clases derivadas. Entre estos métodos están:

* **`__str__()`:** Representación en forma de cadena de un objeto.
* **`__repr__()`:** Representación más detallada del objeto (usada en la consola).
* **`__eq__()`:** Compara si dos objetos son iguales.
* **`__init__()`:** El constructor de la clase, si no se define, heredará uno de object.

#### 7.B Herencia simple o única

&emsp;&emsp; Esta herencia ocurre cuando una subclase hereda una única superclase. esta este es el tipo de herencia utilizada anteriormente.

* **Clase A --> Clase B**

```python
        class A: # superclase
            pass

        class B(A): # subclase
            pass
```
**Ejemplo:**
```python
class Animal:
    def mover(self):
        print("El animal se está moviendo.")


class Perro(Animal):
    def ladrar(self):
        print("El perro está ladrando.")


mi_perro = Perro("Firulais")
mi_perro.mover()  # Salida: Rex se está moviendo.
mi_perro.ladrar()  # Salida: Rex está ladrando.
```

#### 7.C Herencia múltiple.

&emsp;&emsp; Es una subclase que recibe herencia de múltiples superclases. Esto permite combinar características de múltiples clases.

+ ***diagrama***

&emsp;&emsp; **Clase A** &emsp;&emsp;--->
&emsp;&emsp; **Clase B** &emsp;&emsp;---> &emsp;**Clase D** 
&emsp;&emsp; **Clase C** &emsp;&emsp;--->

  ***sintaxis***

```python
        class A: # superclase
            pass

        class B: # superclase
            pass

        class C: # superclase
            pass

        class D(A, B, C): # subclase
            pass
```

**Ejemplo:**
```python
class Volador: # superclase
    def volar(self):
        print("Este objeto puede volar.")


class Nadador: # superclase
    def nadar(self):
        print("Este objeto puede nadar.")


class Pato(Volador, Nadador): # subclase
    pass


mi_pato = Pato()
mi_pato.volar()  # Salida: Este objeto puede volar.
mi_pato.nadar()  # Salida: Este objeto puede nadar.
```

#### 7.D Herencia multinivel.

&emsp;&emsp;  Se refiere a una cadena de herencia en la que una subclase hereda de otra subclase que, a su vez, hereda de una superclase.

* **Diagrama**
&emsp;&emsp;  **clase A** --> **clase B** --> **clase C** --> **clase D**

<br>

***sintaxis***

```python
class A: # superclase
    def saludar(self):
        print("Hola! esta es la clase A")
class B(A): # subclase de A
    def saludar(self):
        print("Hola! esta es la clase B")

class C(B): # subclase de B
    def saludar(self):
        print("Hola! esta es la clase C")

class D(C): # subclase de C
    pass

# se ejecuta el método mas proximo
prueba = D() 
prueba.saludar() # salida: Hola! esta es la clase D 

# mro() es una funcion muestra el camino de herencia, sirve para depurar.
print(A.mro()) # salida: [<class '__main__.A'>, <class 'object'>]
print(D.mro()) # salida: [<class '__main__.D'>, <class '__main__.C'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>]
```


| Clase | Nivel | Herencias |
| --- | --- | --- |
| A| 1| object (clase base de python) |
| B | 2 | object, A |
| C | 3 | object, A, B |
| D | 4 | object, A, B, C |

**Ejemplo:**
```python
class Vehiculo:
    def encender(self):
        print("El vehículo está encendido.")


class Automovil(Vehiculo):
    def conducir(self):
        print("El automóvil está en movimiento.")


class Deportivo(Automovil):
    def acelerar(self):
        print("El deportivo está acelerando.")


mi_deportivo = Deportivo()
mi_deportivo.encender()   # Salida: El vehículo está encendido.
mi_deportivo.conducir()   # Salida: El automóvil está en movimiento.
mi_deportivo.acelerar()   # Salida: El deportivo está acelerando.
```
#### 7.E Herencia Jerárquica.

&emsp;&emsp; Ocurre cuando varias subclases heredan de una misma superclase.

&emsp; ***Diagrama***

&emsp;&emsp;&emsp;&emsp;&emsp; --> Clase 
&emsp; Clase A  ---> Clase C
&emsp;&emsp;&emsp;&emsp;&emsp; --> Clase D 

&emsp; ***Sintaxis***
```python
        class A: # superclase, clase jerarquica
            pass

        class B(A): 
            pass

        class C(A): 
            pass

        class D(A): 
            pass
```
**Ejemplo:**
```python
class Instrumento:
    def tocar(self):
        print("Tocando música.")


class Guitarra(Instrumento):
    def rasguear(self):
        print("Rasgueando la guitarra.")


class Piano(Instrumento):
    def presionar_teclas(self):
        print("Presionando las teclas del piano.")

    
mi_guitarra = Guitarra()
mi_guitarra.tocar()  # Salida: Tocando música.
mi_guitarra.rasguear()  # Salida: Rasgueando la guitarra.

mi_piano = Piano()
mi_piano.tocar()  # Salida: Tocando música.
mi_piano.presionar_teclas()  # Salida: Presionando las teclas del piano.
```

#### 7.F. Herencia híbrida mixta.

&emsp;&emsp; &emsp; Es una combinación de diferentes tipos de herencia, como jerárquica, múltiple o multinivel. El uso puede ser complejo, especialmente con el orden de resolución de métodos (MRO, por sus siglas en inglés).

**sintaxis**
```python
class A:
    def mensaje(self):
        print("Mensaje desde la clase A.")


class B(A):
    def mensaje(self):
        print("Mensaje desde la clase B.")


class C(A):
    pass


class D(B, C):
    pass
```

---

### 8.Encapsulamiento.

&emsp;  El **encapsulamiento** es el concepto de agrupar atributos y métodos en un mismo conjunto. Al crear una clase, estamos implementando este principio. Su propósito es controlar el acceso a los atributos y métodos internos de una clase, utilizando diferentes niveles de **visibilidad** mediante el uso de **modificadores de acceso**. Estos modificadores permiten que ciertos detalles de la implementación del código queden ocultos para el usuario, es decir, para quien utiliza las clas es.

&emsp; *Python es bastante laxo con el tema de encapsulamiento. Por lo tanto, en esta sección se mostrará principalmente meras convenciones más que reglas de sintaxis definidas del lenguaje, esto es útil para  añadir legibilidad a distintos propósitos con los miembros de las clases (atributos y métodos).*

&emsp; se destinguen tres tipos de acceso a miembros: **público**, **protegido(\_)**, **privado(\_\_)**.

* **miembros público:** Son accesible incluso fuera de la clase.
* **miembros protegidos:** según la convención podrán ser accedidos en su clase  y en las subclase que tengan herencia.
* **los miembroso privado:** solo serán accesible en la propia clase.

**Ejemplo:**

```python
class Usuario:
    def __init__(self, id, nombre, apellido):
        self.id = id # Público
        self._nombre = nombre # Protegido
        self.__apellido = apellido # Privado
```

 &emsp;&emsp;*recomendacion es conveniente que se empiece al crear una clase espedificar los miembros como privados primero, y que luego ir cambiando solo los que se necesiten en otro tipo de acceso¨*

 ```python
class Usuario:
    id = 1 # Público

# accedemos y modificamos al atributo públicoo
Usuario.id = 1000

# instanciamos el objeto
usuario_1 = Usuario()

# comprobamos el valor de la id
print(usuario_1.id)
```
al modificar al atributo público implicaría que todos los objetos instanciados tengas ese atributo modificado.
esto podria generar confusiones, consecuentemente errores inesperados.

```python
class Usuario:
    def __init__(self, id, nombre, apellido):
        self.id = id # Público
        self._nombre = nombre # Protegido
        self.__apellido = apellido # Privado

usuario_1 = Usuario(1, "Enrique", "Barros")
print(usuario_1.id) # salida: 1
print(usuario_1._nombre) # salida: Enrique
print(usuario_1.__apellido) # salida: AttributeError: 'Usuario' object has no attribute '__apellido'
```
##### Interfaz pública y acceso en Python

&emsp;Las API, módulos e incluso el lenguaje de Python proporcionan código listo para ser utilizado por los desarrolladores, lo que se conoce como interfaz pública. Esta interfaz incluye todos los elementos diseñados para ser accesibles y utilizados fácilmente. En contraste, el código de funcionamiento interno no forma parte de la interfaz pública, ya que está pensado para trabajar en segundo plano y no ser accedido directamente.

&emsp; En Python, los modificadores de acceso permiten diferenciar entre dos tipos de acceso:

* **Público**: Se refiere a cualquier miembro de una clase (atributo o método) que deseamos exponer en la interfaz pública y que esté accesible para los desarrolladores.
* **No público**: Incluye los miembros que no deben ser accedidos desde fuera de la clase, ya que están destinados exclusivamente a su funcionamiento interno, no necesitamos saber lo que pasa en el código interno.

##### Método público para acceso privado

&emsp; Se puede crear un método publico que sirva para acceder desde dentro de una clase a un miembro privado. lo que conseguimos con esto es que con la interfaz pública que se utilice el método público y no tengamos que acceder directamente al atributo principal.

**Ejemplo:** Método público para el acceso privado, buena práctica.

```python
class Usuario:
    def __init__(self, id, nombre, apellido):
        self.id = id # Público
        self.nombre = nombre # Protegido

        # self privado
        self.__apellido = apellido # Privado

    def muestra_apellidos(self):
        print(f"El apellido es: {self.__apellido}")

# buena práctica.
usuario_1 = Usuario(1, "Enrique", "Barros")
usuario_1.muestra_apellidos() # El apellido es: Barros
```
#### Name mangling

&emsp;Sirve para la modificacion de nombres de variables y métodos de una clase para evitar conflictos con nombres externos o accesos accidentales. Esto se logra poniendo el nombre de un miembro con __ de prefijo, es decir, haciendo miembros privados. por ejemplo en el codigo el nombre del miembro se designa de esta forma: **\_\_apellido**. Sin embargo, el interprete de python lo convierte realmente a esto **\_\_Usuario\_\_apellido**. la sintaxis general es **\_\_NombreClase\_\_Miembro**, es por eso que cuando se intenta acceder fuera de la clase a este atributo nos dará a un error de atributo inexistente.  

* **dir():** Es una función predefinida que nos devolverá una lista que contiene los nombres de los atributos y métodos de un objeto al que le pasemos argumento. esto nos sirve acceder al miembro privado, puesto que python no es tan extricto con los miembros privados, pero esto es una mala práctica.

**ejemplo:** *Método público para el acceso privado. mala práctica.

```python
class Usuario:
    def __init__(self, id, nombre, apellido):
        self.id = id # Público
        self.nombre = nombre # Protegido

        # self privado
        self.__apellido = apellido # Privado

    def muestra_apellidos(self):
        print(f"El apellido es: {self.__apellido}")

# mala practica para acceder un privado
usuario_1 = Usuario(1, "Enrique", "Barros")
print(dir(usuario_1)) # nos interesa esto de la salida: '_Usuario__apellido'
print(usuario_1._Usuario__apellido) # salida: Barros
```

```python
class Animal: 
    def __init__(self, nombre, edad):
        self.nombre = nombre # público,accesible desde cualquie subclase y fuera de la clase 
        self.__edad = edad # privado, en la convención solo deberá se accesible en la clase propia

class Perro(Animal):
    def __init__(self, nombre, edad, raza):
        super().__init__(nombre, edad)
        self.raza = raza 
    
    def mostrar_edad(self):
        print(f"Tengo {self.__edad} años")


perro_1 = Perro("Chester", 3, "Husky")
perro_1.mostrar_edad( ) # AttributeError: 'Perro' object has no attribute '_Perro__edad'
```

La restrinccion privada funciona. Si queremos que la subclase acceda al miembro seria mejor colocarlo en protegido

---

### 9. Métodos getter y setters.

* **Método getter:** sirve para acceder a los valores de una clase .
* **Método setters** sirve para poder modificar los valores de la clase.

```python
class Usuario:
    def __init__(self, id, nombre, edad):
        self.id = id
        self.nombre = nombre
        self.__edad = edad

    # Getter
    def obtener_edad(self):
        return self.__edad
    
    # setter
    def establecer_edad(self, edad):
        self.__edad = edad
        # sirve para modificar la edad desde la interfaz pública.


usuario_1 = Usuario(1, "Enrique", 32)

# Alamacenamos el valor de retorno
edad_usuario = usuario_1.obtener_edad()
print(edad_usuario)

# Establecer una edad 
usuario_1.establecer_edad(25)
print(usuario_1.obtener_edad())
```
---

### 10. Polimorfismo

 El polimorfismo es la capacidad de un objeto de tomar diferentes formas. un ejemplo de polimorfismo es la funcion predifinda **len()**. si se le pasa una cadena de carácteres devolvera la longitud total de carácteres que tiene. En cambio, al usarla en una tupla o lista esta cuenta los elementos ,sin embargo al pasarle un numero de la lista en la funcion len() retornara el numero de carácteres del elemento señalado, en los diccionario contara el numero de key-values.

```python
libro = "libro con mucho texto."
colores = ["Rojo", "Azul", "Amarillo", "Verde"]
usuario = {
            "nombre" : "Enrique",
            "apellido" : "Fernández"
        }

print(len(libro)) # Salida: 22
print(len(colores)) # Salida: 4
print(len(colores[2])) # Salida: 8 
print(len(usuario)) # Salida: 2
```
**Ejemplo:** creando una función con polimorfismo.

```python
class Animal:
    def hablar(self):
        print("Soy un animal")

class Perro(Animal):
    def hablar(self):
        print("woof!")

class Gato(Animal):
    def hablar(self):
        print("Meow!")

animal = Animal()
perro = Perro()
gato = Gato()

def dar_voz(objeto):
    objeto.hablar()

dar_voz(animal)
dar_voz(perro)
dar_voz(gato)
```
---

### 11. sobrecarga y sobrescritura.

&emsp;&emsp; **La sobrecarga** de un método es la capacidad que tiene una clase de tener dos o más con el mismo nombre pero diferentes parámetros, es deir, la sobrecarga varía la funcionalidad.

&emsp;&emsp; **La sobreescritura** de métodos es la capacidad de una subclase de poder modificar el comportamiento de un método heredado de la superclase, se consigue definiendo un nuevo método con el mismo nombre, parámetro y retorno, es decir, la sobreescritura añade más contenido a una funcioinalidad existente.

&emsp;&emsp; *Tanto como la sobrecarga y sobrescritura no existen como tal en Python a diferencia de otras lenguajes de programación, Python realmente solo tiene en cuenta la última definición del método o función.*

```python
# función con 4 parpametros
def multiplicacion(a, b, c, d):
    print(a * b *c * d)

# función con 2 párametos{}
def multiplicacion(a, b): # remplaza la funcion anterior y deja de existir 
    print(a * b)

multiplicacion(10, 2, 3, 6) # TypeError: multiplicacion() takes 2 positional arguments but 4 were given.
```
---

### 12. Abstracción

&emsp; Es un concepto que se utiliza para ocultar los detalles complejos e irrelevantes para los usuario. Como analogía un auto necesitas saber una serie de funciones para conducirlo como girar, acelerar, cambiar marchar, frenar, etc. Sin embargo, para conducir no tiene por que saber como ocurren todas estas cosas, ni hasta la última pieza implicada en ello. Por un lado tenemos el encapsulamiento que se encarga en definir la forma en que se van a utilizar internamente los elementos, centrandose el cómo se implementa mediante la agrupacion de sus miembros relacionados, pero la abstracción lo que busca es facilitar el entendimiento de los conceptos. La abstracción se centra en que hace un objeto, proporciona una vista simplificada del funcionamiento que tiene habilidaddes.

#### Clases Abastractas

&emsp;&emsp; las clases y métodos abstractos relacionan la abstraccion en Python. Este tipo de clases estan diseñadas para ser utilizada por las subclases mediante la herencia. Cuando un mpetodo es declarado dentro una clase sin su implementacion (sin código) se le conoce como método abstracto, una clase abstracta no puede instanciada directamente, no se puede crear objetos  de esa clase pero si de su subclase, entonces las clases abstracta sirve para definir una estructura general para las subclases, todas las subclases que hereden de la clase abstracta deberan implementar lso métodos de esta, pero con sus propias caracteristicas.

```python
from abc import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod
    def hablar(self):
        pass

class Perro(Animal):
    def hablar(self):
        print("Woof!")

class Gato(Animal):
    def hablar(self):
        print("Meow!")

perro = Perro()
perro.hablar()

gato = Gato()
gato.hablar()
```
la clase **Animal** es la clase abstracta en el código, yyy...