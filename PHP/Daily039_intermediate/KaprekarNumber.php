<?php 
/** 
 * KAPREKAR NUMBER
 * 
 * challenge #39 (intermediate)
 * http://www.reddit.com/r/dailyprogrammer/comments/s6be0/4122012_challenge_39_intermediate/
 *
 * sarthak7u@gmail.com
 */

$number = substr(fgets(STDIN), 0,-2);
$squaredNum = (string)((int) $number * (int) $number);

// number of digits in input number
$n = strlen($number);

// m is number of digits from left to be selected 
$m = $n;
if (strlen((string) $squaredNum) != 2 * $n)
{
	$m = $n-1;
}
$leftPart = (int) substr($squaredNum, 0, $m);
$rightPart = (int) substr($squaredNum, $m);

if ((int) $number == $leftPart + $rightPart)
{
	echo "{$number} is a Kaprekar Number";
}
else
{
	echo "{$number} is not a Kaprekar Number";
}
?>