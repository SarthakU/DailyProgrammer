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

class GuessTheNumber
{
    static void play()
    {
        // setup objects
        Random rand = new Random();
        Scanner key = new Scanner(System.in);

        // get the number
        int secret_num =  rand.nextInt(100);

        int max_guesses = 10;

        // setup the game
        System.out.print("\nWelcome to the game!\n");
        System.out.print("~~~~~~~~~~~~~~~~~~~~\n");
        System.out.print("I have already picked a number between 1 and 100.\n");
        System.out.print("You have 8 guesses.\n");
        System.out.print("Please make a guess. Type \"exit\" to quit.\n");

        // start the game
        int user_guess;
        int guess_count = 0;
        while ("pigs" != "fly")
        {
            guess_count ++;
            System.out.print("\n~~~~~~~~~~~~~~~~~~~~\n\n");

            // check if out of guesses
            if (guess_count == max_guesses)
            {
                System.out.print("Sorry! you are out of gusses\n");
                System.out.print("My number was : " + secret_num + "\n");
                break;
            }

            // ask for guess
            System.out.print("Your guess: ");
            String user_input = key.next();

            // compare guess with secret number
            if (!user_input.equals("exit"))
            {
                // check if usr input is a number
                try
                {
                    user_guess = Integer.parseInt(user_input);
                }
                catch(NumberFormatException e)
                {
                    System.out.print("Invalid choice, try again!\n");
                    continue;
                }

                if (user_guess > secret_num)
                {
                    System.out.print("Wrong! That number is above my number.\n");
                }
                else if (user_guess < secret_num)
                {
                    System.out.print("Wrong! That number is below my number.\n");
                }
                else
                {
                    System.out.print("Correct. You win!\n");
                    break;
                }
            }
            else
            {
                System.out.print("Thanks for playing");
                break;
            }
        }
    }
}
