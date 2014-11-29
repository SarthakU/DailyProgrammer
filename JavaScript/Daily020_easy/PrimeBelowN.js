/** 
 * SQUARE ROOT
 *
 * challenge #20 (easy)
 * http://www.reddit.com/r/dailyprogrammer/comments/qnkro/382012_challenge_20_easy/
 *
 * sarthak7u@gmail.com
 */
function prime(n)
{
	if (n == 1)
	{
		return false;
	}
	else if (n == 2)
	{
		return true;
	}
	else
	{
		for (var i = 3; i < n; i+=2)
		{
			if (n % i == 0)
			{
				return false;
			}
		}
	}
	return true;
}
function main()
{
	// case needed for challenge
	NUM = 200; 

	for (var i = 2; i < 200; i++)
	{
		if (prime(i))
		{
			console.log(i);
		}
	}
}
main()