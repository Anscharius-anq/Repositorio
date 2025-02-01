public class str {
    public static void main(String[] args) {
        String text = "Hola Mundo";

        int largo = text.length();
        System.out.println(largo); // 11

        String chao = text.replace("Hola", "Chao");
        System.out.println(chao); // Chao, Mundo
        System.out.println(text); // Hola, Mundo
        // str son inmutables
        // en str cuidado con las mayusculas

        // Métodos

        System.out.println(text.endsWith("undo")); // true
        System.out.println(text.startsWith("Ch")); // false
        System.out.println(text.contains("und")); // True
        // endsWith() la cadena termina con (...)? True False
        // statsWith() la cadena comienza con (...)? True False
        // contains() la cadena contiene (..)? True False

        System.out.println(text.indexOf("Mund")); // 5
        // indexOf() entrega el indice donde comienza el texto

        System.err.println(text.toUpperCase()); // HOLA MUNDO
        System.out.println(text.toLowerCase()); // hola mundo


        String malo = "      Texto malo   ";
         // trim() elimina los espacios del inicio y final. 
        System.out.println(malo); // Salida:       Texto malo
        System.out.println(malo.trim()); // Salida: Texto malo
       


    }
}