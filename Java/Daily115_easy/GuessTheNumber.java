/** 
 * GUESS THE NUMBER
 *
 * challenge #115 (easy)
 * http://www.reddit.com/r/dailyprogrammer/comments/15ul7q/122013_challenge_115_easy_guessthatnumber_game/
 *
 * sarthak7u@gmail.com
 */

import java.util.Scanner;
import java.util.Random;
public class GuessTheNumber
{
	public static void main(String[] args) 
	{
		// Generates a random number initially
		Random rand = new Random();
		int comGuess = rand.nextInt(101);

		// Welcomes user to game and takes first guess
		Scanner key = new Scanner(System.in);
		System.out.println("Welcome to guess-that-numbers game! I have already picked a number in [1, 100]. Please make a guess.");
		int guess = key.nextInt();

		// variable to count no. of guesses
		int guesses = 1;

		// keeps looping till user guesses the correct number
		while (true)
		{	
			if (guess > comGuess)
			{
				 System.out.println("Wrong! That number is above my number.");
			}
			else if (guess < comGuess)
			{
				System.out.println("Wrong! That number is below my number.");
			}	
			else
			{
				System.out.println("Correct! That is my number, you guessed it in " + guesses +", you win!!!");
				break;
			}
			guess = key.nextInt();
			guesses ++;
		}
		

	}	
}