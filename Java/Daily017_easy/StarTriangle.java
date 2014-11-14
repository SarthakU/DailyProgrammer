/** 
 * STAR TRIANGLE
 *
 * challenge #17 (easy)
 * http://www.reddit.com/r/dailyprogrammer/comments/qheeu/342012_challenge_17_easy/
 *
 * sarthak7u@gmail.com
 */

import java.util.Scanner;

public class StarTriangle
{ 
	public static void main(String[] args) 
	{
		Scanner key = new Scanner(System.in);
		System.out.print("Enter size of triangle : ");
		int size = key.nextInt();
		int numberOfStars = 1;
		for (int i = 0; i < size; i++)
		{
			for (int j = 0; j < numberOfStars; j++ )
			{
				System.out.print("*"); 	
			} 
			numberOfStars *= 2;
			System.out.print("\n");
		}
	}	
}