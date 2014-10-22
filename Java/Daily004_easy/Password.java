/** 
 * PASSWORD GENERATOR
 *
 * challenge #4 (easy)
 * http://www.reddit.com/r/dailyprogrammer/comments/pm6oj/2122012_challenge_4_easy/
 *
 * sarthak7u@gmail.com
 */

import java.util.Random;

class Password
{
	public static void main(String[] args) 
	{	
		//declares array of alphabets
		char[] alphabet = "abcdefghijklmnopqrstuvwxyz".toCharArray();		

		//creates object to be used for random number generation
		Random gen = new Random();
		
		//randomly selects length of password between 8 and 12
		int passwordLength = gen.nextInt(4) + 8;

		String password = "";
		for (int i = 0; i < passwordLength; i++ )
		{
			password += alphabet[gen.nextInt(25)];
		}
		System.out.println(password);
			
	}	
}