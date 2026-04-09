import java.util.Scanner;

public class SaccoRecord {

    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter member name: ");
        String name = scanner.nextLine();

        System.out.print("Enter member ID: ");
        String memberID = scanner.nextLine();

        double totalSavings = 0;

        for(int i = 1; i <= 6; i++){
            System.out.print("Enter contribution for month " + i + ": ");
            double contribution = scanner.nextDouble();
            totalSavings = totalSavings + contribution;
        }

        System.out.println("Member Name: " + name);
        System.out.println("Member ID: " + memberID);
        System.out.println("Total Savings: " + totalSavings);
        scanner.close();
    }
}