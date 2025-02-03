# Primeros pasos en Java

---

## Sintaxis de Java con "Hola Mundo"

```java
public class HelloWorld {
    public static void main(String[] args) {
        System.out.println("Hello, World!"); // Salida: "Hello, World!"
    }
}
```
Java es un lenguaje fuertemente orientado a objetos, lo que significa que siempre es necesario crear
una clase al inicio. Aunque en algunas versiones modernas de Java es posible escribir programas más
simples, el enfoque principal sigue siendo la programación orientada a objetos.

### Explicación del código:

* `public class HelloWorld`:
    En Java, todas las aplicaciones comienzan con una clase cuyo nombre debe coincidir con el nombre
    del archivo. En este caso, class `HelloWorld` hace referencia al archivo `HelloWorld.java`. La 
    palabra clave `public` indica que esta clase es accesible desde cualquier otro archivo.

* `public static void main(String[] args):`
    Este es el punto de entrada del programa.

    * `public`: Indica que el método es accesible desde cualquier parte del programa.

    * `static`: Significa que el método pertenece a la clase en lugar de a una instancia de la clase. 
        Por lo tanto, no es necesario crear un objeto de la clase para ejecutar este método.

    * `void`: Indica que el método no retorna ningún valor.

* `System.out.println("Hello, World!")`:
    Esta instrucción se utiliza para imprimir texto en la consola. System.out es el flujo de salida 
    estándar (la consola), y println es un método que imprime el texto y mueve el cursor a la siguiente 
    línea. 
    
Cada vez que escribas código en Java, el contenido principal estará dentro de las llaves { } 
del método main.

___

## Variables y tipos de datos

### Variables primitivas

Las variables primitivas almacenan valores básicos. A continuación, se describen los tipos de datos 
primitivos más comunes:

1. **Números enteros**:
Para almacenar números enteros, se recomienda utilizar el tipo adecuado según las necesidades de
precisión y espacio en memoria. Aunque en computadoras modernas no hay problema en usar siempre int,
existen otros tipos más específicos:

* `byte`: Número entero pequeño, con un rango de -128 a 127, ocupa menos espacio en memoria (1 byte).
* `short`: Número entero de tamaño intermedio, con un rango de -32,768 a 32,767 (2 bytes).
* `int`: Número entero, con un rango de -2,147,483,648 a 2,147,483,647 (4 bytes).
* `long`: Número entero grande, con un rango de -9,223,372,036,854,775,808 a 9,223,372,036,854,775,807 (8 bytes).

2. **Números decimales**:
Para números decimales:

* `float`: Número de punto flotante con precisión simple (4 bytes).
* `double`: Número de punto flotante con precisión doble (8 bytes).

3. **Booleano**:
boolean: Representa un valor lógico, que puede ser true o false.

4. **Carácter**:
char: Almacena un solo carácter, como una letra o un símbolo, utilizando 2 bytes (Unicode).

### Definición de variables

Para definir una variable en Java, es necesario indicar el tipo de dato previamente. Cada instrucción
 debe terminar con un punto y coma (`;`). La sintaxis general es:

 ```pseudocode
tipo nombreVariable = valor;
 ```
 por ejemolo:

 ```java
char letra = 'a';  // Se usan comillas simples para char
byte años = 23;
int numero = 2004;
boolean cumpleaños = false;
float kilogramos = 0.5f; // Para float se pone 'f' al final, si no Java lo toma como double
double litros = 1.5;
 ```

 ### Variables de referencia

Las variables de referencia almacenan direcciones de memoria que apuntan a objetos. Estas variables 
son instancias de clases y, por lo tanto, tienen métodos asociados.

**Ejemplo: String**
Los `String` son cadenas de texto. Para declararlos, se puede usar la siguiente sintaxis:

```java
String texto = new String("Hello World");
```
La palabra `new` indica que estamos creando una instancia de la clase `String`. Sin embargo, declarar un 
`String` de esta manera es redundante. Afortunadamente hay una forma más simplificada que es:

```java
String texto = "Hello World";
```
Este tipo de declaración se llama *String literal* , y los `String` literales cuentan con varios métodos 
útiles que se pueden utilizar.

---

## Arrays
Los arrays son un tipo de dato que almacena varios elementos del mismo tipo. Tienen una dimensión 
fija, lo que significa que no se pueden agregar o eliminar elementos después de su creación.

### Características de los arrays:

* Tienen una longitud fija.
* Todos los elementos deben ser del mismo tipo.
* Son objetos, por lo que tienen métodos asociados.

### Definición de un array
La sintaxis para definir un array es la siguiente:

```pseudocode
tipo[] nombreArray = new tipo[cantidad];
```

por ejemplo, para crear un array de 5 elementos de tipo `int`:


```java
public class ArraysExample {
    public static void main(String[] args) {
        int[] numeros = new int[5];    
        System.out.println(numeros); // Salida: [I@372f7a8d]
    }
}
```

Al crear un array, en realidad estamos creando un objeto (por lo tanto, tiene métodos). Por eso, al 
imprimir `numeros`, obtenemos la dirección de memoria. Para imprimir el contenido del array, debemos 
usar el método `Arrays.toString(nombreArray)` de la clase Arrays. Para ello, es necesario importar 
el paquete `java.util.Arrays`:

```java
import java.util.Arrays;

public class ArraysExample {
    public static void main(String[] args) {
        int[] numeros = new int[5];
        System.out.println(Arrays.toString(numeros)); // Salida: [0, 0, 0, 0, 0]
    }
}
```

Por defecto, cuando no se definen los elementos del array:

* Para números, Java llena el array con ceros.
* Para String, llena el array con cadenas vacías.
* Para boolean, llena el array con false.

Para definir los elementos del array, se puede hacer lo siguiente:

```java
import java.util.Arrays;

public class ArraysExample {
    public static void main(String[] args) {
        int[] numbers = new int[5];  
        numbers[0] = 5; // 5 es asignado a la posición 0
        numbers[4] = 7; // 7 es asignado a la posición 4 
        System.out.println(Arrays.toString(numbers)); // Salida: [5, 0, 0, 0, 7]
    }
}
```

Una forma más sencilla de definir un array es directamente con los valores:

```java
import java.util.Arrays;

public class ArraysExample {
    public static void main(String[] args) {
        int[] numbers = {0, 1, 2, 3, 4};  
        numbers[4] = 7; // También podemos modificar elementos      
        System.out.println(Arrays.toString(numbers)); // Salida: [0, 1, 2, 3, 7]
    }
}
```

### Algunos métodos útilies de Arrays.

```java
import java.util.Arrays;

public class ArraysExample {
    public static void main(String[] args) {
        int[] numbers = {0, 1, 2, 3, 4};  
        System.out.println(numbers.length); // Salida: 5
        Arrays.sort(numbers); // Ordena los elementos 
        System.out.println(Arrays.toString(numbers)); // Salida: [0, 1, 2, 3, 4]
    }
}
```
---

## Arrays multidimensionales

En Java, los arrays pueden tener múltiples dimensiones. Los corchetes `[]`  indican las dimensiones 
del array. Si queremos tener más de una dimensión, basta con agregar más corchetes. Por ejemplo:

```java
public class MultiDimensionalArrays {
    public static void main(String[] args) {
        int[][] numbers = { {0, 1}, {2, 3} };  
        System.out.println(Arrays.toString(numbers)); // Salida: [[I@372f7a8d],[I@6avcfac0]]
        
        // Para imprimir arrays multidimensionales correctamente:
        System.out.println(Arrays.deepToString(numbers)); // Salida: [[0, 1], [2, 3]]
    }
}
```

Si no conocemos todos los elementos del array pero sabemos su longitud, podemos hacer lo siguiente:

```java
public class MultiDimensionalArrays {
    public static void main(String[] args) {
        int[][] numbers = new int[3][2]; // Array creado: [[0, 0], [0, 0], [0, 0]]
        numbers[0][0] = 5; // Array modificado: [[5, 0], [0, 0], [0, 0]]
        
        // Para arrays de 3 dimensiones:
        int[][][] numeros = new int[3][2][2];
    }
}
```

---

## Constantes
Las constantes son variables que no se pueden modificar una vez definidas. Se utiliza la palabra clave
 final antes de definir la variable. Por ejemplo:

 ```java
public class Main {
    public static void main(String[] args) {
        final String empresa = "Hola Mundo";
    }
}
 ```

 ---

 ## Operadores aritméticos

```java
 public class Main {
    public static void main(String[] args) {
        int a = 2 + 2; // 4
        int b = 2 - 2; // 0
        int c = 3 * 3; // 9
        int d = 10 / 3; // 3 (el resultado entero es tres, ya que dividimos entre int)
        int e = 10 % 3; // 1 (el resto de la división, % es el módulo)
        float f = 10f / 3f; // 3.3333333
        double g = 10.0 / 3.0; // 3.3333333333333335
        
        int x = 5;
        ++x; // Incrementa el valor de x a 6
        x++; // También incrementa el valor de x a 6
    }
}
```
La diferencia entre `++x `y `x++` radica en cuándo se incrementa el valor:

`++x`: Incrementa el valor de x antes de usarlo en la expresión.
`x++`: Incrementa el valor de x después de usarlo en la expresión.

```java
int x = 5;
int y = ++x; // Incrementa primero x, luego asigna su valor a y.
System.out.println("x = " + x); // x = 6
System.out.println("y = " + y); // y = 6
```

---

## Casting: Conversión de tipos

Para realizar operaciones con dos o más variables numéricas de distintos tipos, es necesario convertir 
las variables hasta que sean del mismo tipo.

1. **Conversión implícita**
Válido para convertir un tipo de dato pequeño a uno más grande.
```java
public class Main {
    public static void main(String[] args) {
        byte a = 1;
        int b = 15;
        int c = a + b; // Java convierte automáticamente 'a' de byte a int
    }
}
```

2. **conversión explícita**
```java
public class Main {
    public static void main(String[] args) {
        int x = 15;
        double y = 15.015;
        
        // Error
        int z = x + y; // No se puede pasar un dato grande (double) a uno pequeño (int)
        
        // Opción 1
        int z = (int) (x + y);  // Se transforma todo el resultado (x + y) a int
        
        // Opción 2
        int z = x + (int) y; // Se transforma 'y' a int, luego se realiza la suma
    }
}
```

3. **Convertir String a dato numperico**
```java
public class Main {
    public static void main(String[] args) {
        String j = "1.1";
        int k = 5;
        
        // Error
        double l = j + k; // Se está operando un String con un int ("1.1" + 5)
        
        // Solución
        double l = Double.parseDouble(j) + k; // Ahora j es un double
    }
}
```
---

## Clase Math

La clase `Math` proporciona métodos útiles para realizar operaciones matemáticas. Estos métodos están 
sobrecargados, lo que significa que se pueden usar con diferentes tipos de datos.

* `Math.abs()` : Devuelve el valor absoluto.
* `Math.ceil()`: Redondea hacia arriba.
* `Math.floor()` : Redondea hacia abajo.
* `Math.max()` : Recibe dos números y devuelve el mayor.
* `Math.min()` : Recibe dos números y devuelve el menor.
* `Math.round()` : Redondea al número más cercano.
* `Math.random()` : Devuelve un número aleatorio entre 0 y 1.

```java
public class Main {
    public static void main(String[] args) {
        System.out.println(Math.abs(-15)); // Salida: 15
        System.out.println(Math.ceil(10.01)); // Salida: 11
        System.out.println(Math.floor(10.999)); // Salida: 10
        System.out.println(Math.max(12, 25)); // Salida: 25
        System.out.println(Math.min(12, 25)); // Salida: 12
        System.out.println(Math.round(15.5)); // Salida: 16
        System.out.println(Math.random()); // Salida: 0.3559593296024
        
        // Si queremos un número aleatorio entero entre 0 y 100
        System.out.println((int) (Math.random() * 100)); // Salida: 0 al 99
        System.out.println(Math.round(Math.random() * 100)); // Salida: 0 al 100
    }
}
```

---

## Formato de números
Para formatear números como porcentajes o monedas, se usa la clase `NumberFormat`. Esta clase es 
abstracta, lo que significa que no se puede instanciar directamente usando `new`.

1. Porcentaje
```java
import java.text.NumberFormat;

public class Main {
    public static void main(String[] args) {
        NumberFormat porcentaje = NumberFormat.getPercentInstance();
        System.out.println(porcentaje.format(0.15)); // Salida: 15%
    }   
}
```

2. Moneda
Usa la configuración regional (locale) del sistema operativo para designar la moneda.

```java
import java.text.NumberFormat;

public class Main {
    public static void main(String[] args) {
        NumberFormat numberFormat = NumberFormat.getCurrencyInstance();
        String result = numberFormat.format(1099);
        System.out.println(result); // Salida: $1.099 (en CLP, dependiendo de la región)
    }   
}
```
Para fijar la moneda independientemente de la región del usuario, se puede usar la clase `Locale`:

```java
import java.text.NumberFormat;
import java.util.Locale;

public class Main {
    public static void main(String[] args) {
        Locale locale = new Locale("es", "CL"); // Fijar la moneda en CLP
        NumberFormat numberFormat = NumberFormat.getCurrencyInstance(locale);
        String result = numberFormat.format(1099);
        System.out.println(result); // Salida: $1.099 (en CLP)
    }   
}
```

---

## Clase Scanner

La clase Scanner se utiliza para leer la entrada de la consola. Por convención, al crear una instancia 
de una clase en Java, se utiliza el nombre de la clase en minúscula para la variable.

```java
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String valor = scanner.next();  // Leer un valor del usuario
        System.out.println(valor);  // Mostrar el valor ingresado
        scanner.close();  // Cerrar el scanner para liberar los recursos
    }
}
```

* `.nextLine()`: Evualpua cada palabra separadapor espacios como un token.
* `.next`: toma el primer token.

...