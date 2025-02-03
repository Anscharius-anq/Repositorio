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
    * `static`: Significa que el método pertenece a la clase en lugar de a una instancia de la clase. Por lo tanto, no es necesario crear un objeto de la clase para ejecutar este método.
    * `void`: Indica que el método no retorna ningún valor.
* `System.out.println("Hello, World!")`:
Esta instrucción se utiliza para imprimir texto en la consola. System.out es el flujo de salida estándar (la consola), y println es un método que imprime el texto y mueve el cursor a la siguiente línea.
Cada vez que escribas código en Java, el contenido principal estará dentro de las llaves { } del método main.