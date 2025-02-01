import java.util.Scanner;

public class SwitchCaseBreak {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int comando = 0;

        while (!(comando == 3)) {
            System.out.println("1. Calculadora \n2. Hackear la NASA \n3. Salir");
            System.out.println();
            comando = scanner.nextInt();

            terminar: switch (comando) {
                case (1):
                    System.out.println("Ingresa dos números para la suma");
                    System.out.println("> Ingresa el primer número:");
                    int primerNumero = scanner.nextInt();
                    System.out.println("Ingresa el segundo número:");
                    int segundoNumero = scanner.nextInt();
                    System.out.println("> Resultado: " + (primerNumero + segundoNumero));
                    
                    break;

                case (2):
                    System.out.println("#");
                    System.out.println("##");
                    System.out.println("###");
                    System.out.println("####");
                    
                    break;
                case(3):
                System.out.println("fin del programa");
                scanner.close();
                break terminar;

                    
            }
        }
    }     
}