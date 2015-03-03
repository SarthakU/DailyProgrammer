/**
 * PASSWORD GENERATOR
 *
 * challenge #4 (easy)
 * http://www.reddit.com/r/dailyprogrammer/comments/pm6oj/2122012_challenge_4_easy/
 *
 * sarthak7u@gmail.com
 */

using System;
public class Password
{
    static void Main(string[] args)
    {
        Random gen = new Random();

        string alphabet = "abcdefghijklmnopqrstuvwxyz";
        int passwordLength = gen.Next(8,12);
        string password = "";

        for (int i = 0; i  < passwordLength; i++)
        {
            password += alphabet[gen.Next(0,25)];
        }
        Console.WriteLine(password);
    }
}
