/** 
 * SQUARE ROOT
 *
 * challenge #61 (intermediate)
 * http://www.reddit.com/r/dailyprogrammer/comments/uo14v/662012_challenge_61_intermediate/
 *
 * sarthak7u@gmail.com
 */
import java.util.Scanner;
public class SquareRoot
{
	public static void main(String[] args) 
	{
		Scanner key = new Scanner(System.in);

		System.out.print("Find Squareroot of :");
		double num = key.nextDouble();

		System.out.println(squareroot(num));
	}
	static double squareroot(double num)
	{
		double high = num;
		double low = 0;
		double curr = (high + low) / 2 ;
		while ((curr*curr) - num > 0.000001 || num - (curr*curr) > 0.000001)
		{
			curr = (high + low) / 2;
			if ((curr*curr) > num)
			{
				high = curr;
			}
			else if ((curr*curr) < num)
			{
				low = curr;
			}
		}
		return curr;
	}
}