import java.util.Scanner;
public class Positive
{
    public static void main(String[] args) 
    {
        int n;
        Scanner s = new Scanner(System.in);
        System.out.print("Input:");
        n = s.nextInt();
        if(n > 0)
        {
            System.out.println(" Positive");
        }
        else if(n < 0)
        {
            System.out.println("Negative");
        }
        else
        {
            System.out.println("zero ");
        }
    }
}
