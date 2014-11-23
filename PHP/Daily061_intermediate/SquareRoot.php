<?php 	
/** 
 * SQUARE ROOT
 *
 * challenge #61 (intermediate)
 * http://www.reddit.com/r/dailyprogrammer/comments/uo14v/662012_challenge_61_intermediate/
 *
 * sarthak7u@gmail.com
 */
function squareroot($num)
{
	$low = 0;
	$high = $num;
	$curr = ($low + $high)/2;
	while (($curr*$curr) - $num > 0.000001 || $num - ($curr*$curr) > 0.000001)
	{
		$curr = ($high + $low) / 2;
		if (($curr*$curr) > $num)
		{
			$high = $curr;
		}
		else if (($curr*$curr) < $num)
		{
			$low = $curr;
		}
	}
	return $curr;
}
echo "Find Squareroot of :";
$num = fgets(STDIN);
echo squareroot($num);
?>