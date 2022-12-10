/** 
 * GUESS THE NUMBER
 *
 * challenge #115 (easy)
 * https://www.reddit.com/r/dailyprogrammer/comments/15ul7q/122013_challenge_115_easy_guessthatnumber_game/
 *
 * sarthak7u@gmail.com
 */

package main

import (
	"fmt"
	"math/rand"
)

func randInt(min, max int) int {
	return min + rand.Intn(max-min)
}

func main() {
	fmt.Println("Guess the number!")
	answer := randInt(1, 100)
	fmt.Println(answer)

	for {
		var guess int
		fmt.Scanln(&guess)
		if guess == answer {
			fmt.Println("That's Correct")
			break
		} else if guess > answer {
			fmt.Println("Wrong guess. Too High! ")
		} else if guess < answer {

			fmt.Println("Wrong guess. Too Low! ")
		}
	}
}
