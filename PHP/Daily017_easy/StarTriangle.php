<?php 
/** 
 * STAR TRIANGLE
 *
 * challenge #17 (easy)
 * http://www.reddit.com/r/dailyprogrammer/comments/qheeu/342012_challenge_17_easy/
 *
 * sarthak7u@gmail.com
 */
 
echo "Enter size of triangle : ";
$size = substr(fgets(STDIN), 0,-1);
$numberOfStars = 1;
for ($i = 0; $i < (int) $size; $i++)
{
	for ($j = 0; $j < $numberOfStars; $j++ )
	{
		echo "*";
	}
	$numberOfStars *= 2;
	echo "\n";
}
?>