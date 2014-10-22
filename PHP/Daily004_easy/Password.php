<?php
/** 
 * PASSWORD GENERATOR
 *
 * challenge #4 (easy)
 * http://www.reddit.com/r/dailyprogrammer/comments/pm6oj/2122012_challenge_4_easy/
 *
 * sarthak7u@gmail.com
 */

//stores alphabets
$alphabet = range('a', 'z');

//randomly selects length for password
$passwordLength = rand(8,12);

$password = "";

for ($i = 0; $i < $passwordLength; $i++) 
{ 
	$temp = $alphabet[rand(0,25)];
	$password = $password.$temp;
}

echo $password;

?>