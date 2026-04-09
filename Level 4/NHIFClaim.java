import java.util.Scanner;

class Patient {

    String name;
    String policyNumber;

    Patient(String name, String policyNumber){
        this.name = name;
        this.policyNumber = policyNumber;
    }

    double calculateClaim(double amount){
        return amount - (amount * 0.10);
    }
}

public class NHIFClaim {

    public static void main(String[] args){

        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter patient name: ");
        String name = scanner.nextLine();

        System.out.print("Enter policy number: ");
        String policy = scanner.nextLine();

        System.out.print("Enter claim amount: ");
        double amount = scanner.nextDouble();

        Patient patient1 = new Patient(name, policy);

        double finalClaim = patient1.calculateClaim(amount);

        System.out.println("Patient Name: " + patient1.name);
        System.out.println("Policy Number: " + patient1.policyNumber);
        System.out.println("Final Claim Amount: " + finalClaim);
        scanner.close();
    }
}