<?php 
/** 
 * NUMBER RIGHE TRIANGLE
 *
 * challenge #35 (easy)
 * http://www.reddit.com/r/dailyprogrammer/comments/rr4y2/432012_challenge_35_easy/
 *
 * sarthak7u@gmail.com
 */

$input = fgets(STDIN);
$triangleList = [];
for ($i = 1; $i <= $input; $i++)
{ 
	array_push($triangleList, $i);
}
$edgeSize = 1;
$index = -1;
while (TRUE) 
{
	if ($index + $edgeSize > $input) 
	{
		break;
	}
	for ($i = 0; $i <= $edgeSize; $i++)
	{
		$index ++;
		if ($index >= count($triangleList))
		{
			break;
		}
		echo $triangleList[$index]." ";
	}
	echo "\n";
	$edgeSize ++;
}
?>