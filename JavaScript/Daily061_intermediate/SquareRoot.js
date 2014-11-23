/** 
 * SQUARE ROOT
 *
 * challenge #61 (intermediate)
 * http://www.reddit.com/r/dailyprogrammer/comments/uo14v/662012_challenge_61_intermediate/
 *
 * sarthak7u@gmail.com
 */
function sqrt(num)
{	
	var low = 0;
    var high = num;
    var curr = (high + low) / 2;
    while ((curr*curr) - num > 0.00001 || num - (curr*curr) > 0.00001)
    {
    	curr = (high+low)/2;
    	if (curr*curr > num)
        {
        	high = curr;
		}
        else if (curr*curr < num)
        {
        	low = curr;
		}
    }
	return curr;
}