import java.util.Scanner;

public class InterestCalculator
{
	public static void main(String[] args) 
	{
		Scanner key = new Scanner(System.in);

		System.out.print("Enter the Principle amount: ");
		double principle = key.nextDouble();

		System.out.print("Enter the interest rate: ");
		double rate = key.nextDouble();

		System.out.print("Enter the time period: ");
		double timePeriod = key.nextDouble();

		Interest object = new Interest();
		System.out.println(object.simpleInterest(principle, rate, timePeriod));

	}
}
class Interest
{
	double simpleInterest(double principle, double rate, double timePeriod)
	{
		return principle * rate * timePeriod;
	}
}