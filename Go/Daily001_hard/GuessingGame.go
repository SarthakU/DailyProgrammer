/**
 * USER INPUT
 *
 * challenge #1 (hard)
 * https://www.reddit.com/r/dailyprogrammer/comments/pii6j/difficult_challenge_1/
 *
 * sarthak7u@gmail.com
 */

package main

import (
	"fmt"
	"math/rand"
	"strings"
)

func main() {
	try(100, 1)
}

func try(max, min int) {
	var judgement, direction string
	guess := rand.Intn(max - min) + min

	fmt.Printf("My Guess is %d\n", guess)
	fmt.Println("Is it correct? (y/n)")
	fmt.Scanln(&judgement)

	if strings.ToLower(judgement) == "y" {
		fmt.Println("Guessed it!")
	} else if strings.ToLower(judgement) == "n" {
		fmt.Println("Oops!")
		fmt.Println("Is it higher or lower? (h/l)")
		fmt.Scanln(&direction)

		if strings.ToLower(direction) == "h" {
      try(max, guess)
		} else if strings.ToLower(direction) == "l" {
      try(guess, min)
		} else {
			fmt.Println("I dont understand, please answer in `h` or `l`")
			fmt.Println("Restarting!")
			try(max, min)
		}
	} else {
		fmt.Println("I dont understand, please answer in `y` or `n`")
		fmt.Println("Restarting!")
		try(max, min)
	}
}
