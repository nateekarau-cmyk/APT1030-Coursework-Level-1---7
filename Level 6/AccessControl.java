/* The Java program performs the same task. 
If the user is not a Doctor, an exception is thrown. 
The try-catch block handles the error and displays the message. */

import java. util.Scanner;

public class AccessControl {

    static void checkAccess(String role) throws Exception{

        if(!role.equals("Doctor")){
            throw new Exception("Access Denied");
        }
        else{
            System.out.println("Access Granted");
        }
    }

    public static void main(String[] args){

        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter role: ");
        String role = scanner.nextLine();

        try{
            checkAccess(role);
        }
        catch(Exception e){
            System.out.println(e.getMessage());
        }
        scanner.close();
    }
}