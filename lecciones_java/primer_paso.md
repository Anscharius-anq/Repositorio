# Primeros pasos en Java.
---
## Sintaxis de java con hola mundo

```java
public class HelloWorld {
    public static void main(String[] args) {
        System.out.println("Hello, World!"); // Salida: "Hello, World!"
    }
}
```
Java está fuertemente orientado a objetos, lo que significa que es necesario crear una clase al 
inicio. Si no lo hacemos, el archivo no se ejecutará. Aunque en algunas versiones modernas de Java
es posible escribir programas más simples, el enfoque principal sigue siendo la programación
orientada a objetos.

* **public name class:** En java todo las aplicaciones comienzan por class name y esa clase 
debe coincidir con en el nombre del archivo, en este ejemplo class HelloWorld hace referencia al
archivo HelloWorld.java. al principio dice *public* esto quiere decir que el archivo es publico osea
que otros archivos pueden acceder a él.
* **public static void:**

    * **public** indica que el método es accesible desde cualquier otra parte del programa.

    * **static** significa que el método pertenece a la clase en lugar de a una instancia de la 
    clase. Por eso, no necesitas crear un objeto de la clase para ejecutar el método main.

    * **void** indica que el método no retorna ningún valor.rna nada.luego *static* significa que
     es un método de la clase, en este caso es *Main*.

* **main():** Es el nombre del método. Es el punto de entrada al programa y debe ser definido de
esta manera para que la JVM (Java Virtual Machine) lo ejecute cuando se inicie el programa

* **System.out.println("Hello, World!")**: Esta instrucción se utiliza para imprimir texto en la 
consola. System.out es el flujo de salida estándar (la consola), y println es un método que imprime
 el texto y mueve el cursor a la siguiente línea.

Cada vez que se escriba código en Java, se hará dentro de las llaves { } del método main.

---

## Variables y tipos de datos

### Variables primitivas.

Las variables primitivas almacenan valores basicos.

#### 1.- Números enteros.
Para almacenar números, se recomienda utilizar el tipo adecuado según las necesidades de precisión 
y espacio en memoria:

* **byte:** Número entero pequeño, con un rango de -128 a 127, ocupa menos espacio en memoria (1byte).
* **short:** Número entero de tamaño intermedio, con un rango de -32,768 a 32,767 (2 bytes).
* **int:** Número entero, con un rango de -2,147,483,648 a 2,147,483,647 (4 bytes).
* **long:** Número entero grande, con un rango de -9,223,372,036,854,775,808 a
 9,223,372,036,854,775,807 (8 bytes).

#### 2.- Números decimales.
Para números decimales
* **float:** Número de punto flotante con precisión simple (4 bytes).
* **double:** Número de punto flotante con precisión doble (8 bytes).

#### 3.- Booleano.
* **boolean:** Representa un valor lógico, que puede ser true o false.

#### 4.- Carácter.
* **char:** Almacena un solo carácter, como una letra o un símbolo, utilizando 2 bytes (Unicode).

#### *Definir variable*

para definir una variable requiere indicar el tipo de dato previamente y para finalizar la 
instrucción se indica con (\;), se utiliza la siguiente sintaxis:
```pseudocode
type variableName = value;
tipo nombreVariable = valor;
```
por ejemplo:
```java

char letra = 'a'  // se usa comillas simples para char
byte años = 23;
int numero = 2004;
boolean cumpleaños = False;
float kilogramos = 0.5f; // para float se pone f al final, si no java lo toma como double
double litros = 1.5
```

### Variables de referencia 

Las variables de referencia almacenan direcciones de memoria que apuntan a objetos. por lo tanto
estas variables como son instancias de clases tienen métodos.

* **String:** son las cadena de texto, para declararlas se usa la siguiente sintaxis:

```java
    String texto = new String("Hello World")
```

la palabra *new* ya no está diciendo que se trata de una instancia de clase. Sin embargo, declarar
un string de esta manera es redundante puesto que vamos a declarar varios string en el código, un forma 
mas simplificada es:
```java
    String texto = "Hello World"
```
Este tipo de String cuando no usamos new String() se le llama *String literal*, estos cuentan con
varios métodos que se pueden utilizarse.

---

## Arrays

Los arrays son un tipo de dato que almacena varios elementos del mismo tipo de dato tiene y de 
dimensión fija. no se pude agregar o eliminar elementos de un array

**características**
* 
*
*



para definir una array se puede usar la siguiente sintaxis:
```pseudocode
tipo[] nombreArray = new tipo[cantidad]
```
por ejemplo: un array de de 5 elementos de enteros.

```java
public class arrays {
    public static void main(String[] args) {
        int[] numeros = new int[5];    
        System.out.println(numeros) // salida: [I@372f7a8d]
    }
}
```
al crear un array en realidad estamos creando un objeto(por lo tanto, tiene métodos), por eso al
imprimir *numeros* se se obtiene como salida la dirección de memoria. para imprimir el contenido
del array hace falta utilizar el método de la clase Arrays: *Arrays.toString(nombreArray)*, para 
ello hace falta previamente importar un paquete de java *(import java.util.Arrays;)* pero al 
escribir el método java lo importa automáticamente.

```java
import java.util.Arrays;

public class arrays {
    public static void main(String[] args) {
        int[] numeros = new int[5];

        System.out.println(Arrays.toString(numeros)) // salida: [0, 0, 0, 0, 0]
    }
}
```
por defecto al no definir los elementos del array, en el caso de numeros java llena de ceros en el
conjunto, para Strings llena de cadenas vacias y para boolean llena de false. Para definir los 
elementos se realiza lo siguiente: 

```java
import java.util.Arrays;

public class arrays {
    public static void main(String[] args) {
        int[] numbers = new int[5];        
        numbers[0] = 5; // 5 es asignado a la posición 0
        numbers[4] = 7; // 7 es asignado a la posición 4 

        System.out.println(Arrays.toString(numbers)); // salida [5, 0, 0, 0, 7]

```

Evidentemente esto es una forma muy lente de definir arrays, afortunadamente existe una forma más
sencilla de hacerlo:

```java
import java.util.Arrays;

public class arrays {
    public static void main(String[] args) {
        int[] numbers = {0, 1, 2, 3, 4};  
        numbers[4] = 7; // tambien podemos usar esto      


        System.out.println(Arrays.toString(numbers)); // salida [5, 1, 2, 3, 7]
    }
}
```

 Adicionalmente se muestra algunos métodos de array:

```java
import java.util.Arrays;

public class arrays {
    public static void main(String[] args) {

        int[] numbers = {0, 1, 2, 3, 4};  

        System.out.println(numeros.length); // salida: 5
        Arrays.sort(numbers); // ordena los elementos 
        System.out.println(Arrays.toString(numbers));
    }
}
```

---

## Múltiples dimensiones

al definir el tipo de array ( int[ ] ), se encuentra los corchete, pues estos indican las dimensiones
del array, si queremos tener  más de una dimensión basta con agregar mas corchetes por ejemplo
( int[ ][ ] ) y luego se va definiendo el array y subsarray.

```java
public class arrays {
    public static void main(String[] args) {

        int[][] numbers = { {0, 1}, {2, 3} };  
        System.out.println(Arrays.toString(numbers)); // Salida: [[I@372f7a8d],[I@6avcfac0]]

        // para imprimir arrays en este caso:
        Sistem.out.println(Arrays.deepToString(numbers)); // Salida: [[0, 1], [2, 3]]
```
si no sabemos todos lo elementos del array pero sabemos que longitud tendrá usamos esto:

```java
public class arrays {
    public static void main(String[] args) {

        int[][] numbers = new int[3][2]; // Array creado: [[0, 0], [0, 0], [0, 0]]
        numbers[0][0] = 5; // Array modificado: [[5, 0], [0, 0], [0, 0]]

        // Si queremos arrays de 3 dimensiones:
        int[][][] numeros = new int[3][2][2];
```
___

## Constantes

Las constantes son variables que no se pueden modificar una vez definidos (al hacerlos java arroja
error). Se utiliza la palabra *final* antes de definir la variable, por ejemplo:

```java
public class Main {
    public static void main(String[] args[[0, 0], [0, 0], [0, 0]]) {
        final String empresa = "hola mundo";
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

        int d = 10 / 3; // 3 (el resultado entero es tres puesto que dividimos int)
        int e = 10 % 3; // 1 (el resto de la division, % es el módulo)
        float f = 10f / 3f; // 3.3333333
        double  g = 10.0 / 3.0; // 3.3333333333333335

        int x  = 5;
        ++x; // aumenta el valor de x a 6

        
        int x  = 5;
        ++x; // aumenta el valor de x a 6

    }
}
```

para aumentar en 1 un numeros se podria hacer lo sigruiente:

```java
public class Main {
    public static void main(String[] args) {
        int x  = 5;
        ++x; // aumenta el valor de x a 6

        // o también

        int x  = 5;
        x++; // aumenta el valor de x a 6

    }
}
```
la diferencia de esta en que *++variable* incrementa el valor de la variable antes de usarlo en la
expresion:

```java
int x = 5;
int y = ++x; // Incrementa primero x, luego asigna su valor a y.
System.out.println("x = " + x); // x = 6
System.out.println("y = " + y); // y = 6

```
y *variable++*  ...

---

## Casting: Conversion de tipos

Para realizar operaciones con dos o más variables numéricos de distintos tipos, es necesario convertir
las variables hasta que sean del mismo tipo. Las tranformaciones se pueden realizar con tipos válidos 
entre si.

1. *Conversión implícita*
 Válido para convertitr tipo de dato pequeño a uno más grande.

```java 
 public class Main {
    public static void main(String[] args) {
        byte a = 1;
        int b = 15;
        int c = a + b;
        /*java revisa primero que tipo es "c", de tipo int, luego revisa los demas tipos
        de las variables definidas, y lo transformara a tipo de dato más pequeño a 
        más grande automaticamente, es decir, "a" es byte transformará a int. */
    }
}
```

2. *Conversión explícita*

```java 
 public class Main {
    public static void main(String[] args) {
        int x = 15;
        double y = 15.015

        // Error.
        int z  = x + y; // no se puede pasar "y" un dato grande (double) a uno pequeño (int)

        // opción 1.
        int z  = (int) (x + y);  // se tranforma todo el resultado (x + y)

        // opcion 2.
        int z =   x  + (int) y; //  se transforma "y" luego se realiza la suma (x + y)
    }
}
```

3. *Convertir String a dato numérico*

```java 
 public class Main {
    public static void main(String[] args) {
        String j = "1,1";
        int k = 5;

        // Error
        double l = j + k; // se está operando un string con int ("1,1" + 5)

        // String tiene un mpetodo que puede convertir el tipo de dato
        double l = Double.parseDouble(j) + k; // ahora j es un double
    }
}
```

## Clase Math

aquí se verán algunos métodos importante de la clase math, los métodos de Math estan overloaded,
es decir que se pueden usar distintos tipo de datos en ellos.

* *Math.abs()* devuelve el valor absoluto.
* *Math.ceil()* redondea hacia arriba.
* *Math.floor()* redondea hacia abajo.
* *Math.max()* recibe dos números y devolvera el mayor.
* *Math.min()* recibe dos números y devolvera el menor.
* *Math.roud()* redondea al número más cercano.
* *Math.round()* devuelve un número aleatoriio entre 0 y 1. 
```java
public class Main {
    public static void main(String[] args) {

        System.out.println(Math.abs(-15)); // Salida: 15
        System.out.println(Math.ceil(10.01)); // Salida: 11
        System.out.println(Math.floor(10.999)); // Salida: 10
        System.out.println(Math.max(12, 25))); // Salida: 25
        System.out.println(Math.min(12, 25))); // Salida: 12
        System.out.println(Math.round(15.5))); // Salida: 16
        System.out.println(random); // 0.3559593296024

        // si queremos  numero aleatorio int 0 al 100
        System.out.println((int) (Math.random() * 100)); // 0 al 99
        System.out.println(Math.round(Math.random() * 100)); // 0 al 100
    }
}
```

## formato 

formato a los números par mostrarlos en prcentaje o como tipos de monedas, para ello se usa la clase
*NumberFormat*, esta clase es abstracta, lo que significa que no se puede instancia un objeto usando
new.
1. *porcentaje*
```java
import java.text.NumberFormat;

public class Main {
    public static void main(String[] args) {
        
        NumberFormat porcentaje = NumberFormat.getPercentInstance();
        System.out.println(porcentaje.format(0.15)); 
    }   
}
```



2. *moneda*
Usa la configuración regional (local) de la computadora o del sistema operativo de manera
predeterminada para designar la moneda.
```java
import java.text.NumberFormat;

public class Main {
    public static void main(String[] args) {
        
        NumberFormat numberFormat = NumberFormat.getCurrencyInstance();
        String result = numberFormat.format(1099);

        System.out.println(result); // Salida: $1.099    en CLP
    }   
}
```
El problema es que si se ejecuta el programa la moneda se formatea segun la region del usuario.
para fijar la moneda CLP independientemente de donde se ejecute, usamos la classe*Locale*

```java
import java.text.NumberFormat;

public class Main {
    public static void main(String[] args) {
        
        Locale locale = Locale.forLanguage("es-CL") // para fijar la moneda en CLP 
        NumberFormat numberFormat = NumberFormat.getCurrencyInstance(locale);
        String result = numberFormat.format(1099);

        System.out.println(result); // Salida: $1.099    en CLP
    }   
}
```
## Clase Scanner
Scanner es una clase que se usa para leer la entrada de la consola. Por convención, al crear una 
instancia de una clase en Java, se utiliza la declaración de tipo de la clase seguida del nombre
 de la variable usando el nombre de la clase en minúscula. 
```java
*Scanner scanner = new Scanner(System.in);
```
el valor entreparentesis scanner() indica al Scanner de donde estará leyendo informacion el scanner.
Las instancias de Scanner tiene distintos métodos para poder leer datos de la consola.

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

* *.next()* Evalua cada palabra separadas por espacio con un token y .next() toma al primer token.



