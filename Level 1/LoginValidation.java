import java.util.Scanner;

public class LoginValidation {
    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter username: ");
        String username = scanner.nextLine();

        System.out.print("Enter password: ");
        String password = scanner.nextLine();

        if(username.equals("adminKE") && password.equals("254Secure")){
            System.out.println("Access Granted");
        } else {
            System.out.println("Invalid Credentials");
        }

            scanner.close();
    }
}