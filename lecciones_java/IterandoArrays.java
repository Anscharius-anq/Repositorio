public class IterandoArrays {
  
    public static void main(String[] args) {

        int resultado = suma(new int[] { 1, 2, 3, 4, 5 });
        System.out.println(resultado);

    }

    static int suma(int[] numeros) {
        int resultado = 0;
        for (int numero : numeros) {
            resultado += numero;
        }
        return resultado;
    }
}
  
