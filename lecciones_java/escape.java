public class escape {
    public static void main(String[] args) {
        /* escapes:
         *  \" comillas 
         *  \\ backslash
         *  \n nueva linea
         *  \t tabulación
         */


        String texto_1 = "c:\\Hola \"Mundo\">"; 
        String texto_2 = "Hola \nMundo";
        String texto_3 = "Hola \tMundo";

        System.out.println(texto_1);
        System.out.println(texto_2);
        System.out.println(texto_3);

    }
}
