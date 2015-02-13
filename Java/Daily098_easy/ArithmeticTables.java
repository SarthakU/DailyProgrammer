/**
 * ARITHMETIC TABLES
 *
 * challenge #98 (easy)
 * http://www.reddit.com/r/dailyprogrammer/comments/zx8vw/9152012_challenge_98_easy_arithmetic_tables/
 *
 * sarthak7u@gmail.com
 */

class ArithmeticTables
{
    static void print_tables(int num, String operator)
    {
        // check if operator valid
        String[] valid_operators = {"+", "-", "*", "/"};
        for (int i = 0; i < 4; i++)
        {
            // if operator is present break
            if (valid_operators[i] == operator)
            {
                break;
            }

            // operator invalid, give error message and exit
            if (i == 3)
            {
                System.out.print("Operator is invalid!");
                return;
            }
        }

        // store nums from 0 to n
        int[] nums = new int[num + 1];
        for (int i = 0; i <= num; i++)
        {
            nums[i] = i;
        }

        // print first row
        System.out.print(" " +  operator + " ");
        System.out.print(" |  ");
        for (int i = 0; i <= num; i++)
        {
            System.out.print(nums[i]+ " ");
        }

        // print the divider
        System.out.print("\n-----------------\n");

        // print the rest of the table
        for (int i = 0; i <= num; i++)
        {
            System.out.print(" " +  i + " ");
            System.out.print(" |  ");
            for (int j = 0; j <= num; j++)
            {
                switch (operator)
                {
                    case "+":
                        System.out.print(i + j + " ");
                        break;
                    case "-":
                        System.out.print(i - j + " ");
                        break;
                    case "*":
                        System.out.print(i * j + " ");
                        break;
                    case "/":
                        System.out.print(i / j + " ");
                        break;
                }
            }
            System.out.print("\n");
        }

    }
}
