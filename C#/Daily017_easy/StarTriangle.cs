/**
 * STAR TRIANGLE
 *
 * challenge #17 (easy)
 * http://www.reddit.com/r/dailyprogrammer/comments/qheeu/342012_challenge_17_easy/
 *
 * sarthak7u@gmail.com
 */

using System;
public class StarTriangle
{
    static void Main(string[] args)
    {
        Console.Write("Enter size of the Traingle : ");
        int size = Convert.ToInt32(Console.ReadLine());

        for (int i = 0; i < size; i++)
        {
            for (int j = 0 ; j < Math.Pow(2,i); j++)
            {
                Console.Write("*");
            }
            Console.Write("\n");
        }
    }
}
