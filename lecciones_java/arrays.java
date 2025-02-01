import java.util.Arrays;

public class arrays {
    public static void main(String[] args) {
        /* 
        arrays: es un tipo de dato para alamcecna muchos elementos
        del mismo tipo de dato del mismo tipo de dato. tienen dimension fija 
        no se puede agregar  o eliminar elementos de un array


        Al declarar el tipo de elementos requiere agregar []. 

        En new int[5] se indica que hay 5 elementos en el array si no se especifica 
        los elementos por defecto java crea elementos de ceros.

        por defecto :
        - numerico: inicializa  con ceros
        - strings:  stringsv vacio
        - bool: booleans falsos
        */

        int[] numeros = new int[5];

        System.out.println(numeros); // salida: [I@372f7a8d // direccion de memoria
        System.out.println(Arrays.toString(numeros)); // salida: [0, 0, 0, 0, 0]

        // para añadir elementos
        int[] numbers= new int[5];
        numbers[0] = 5;
        numbers[4] = 7;

        System.out.println(Arrays.toString(numbers)); // salida [5, 0, 0, 0, 7]

        System.out.println(numeros.length);
        Arrays.sort(numbers);
        System.out.println(Arrays.toString(numbers));
        

    }
}
