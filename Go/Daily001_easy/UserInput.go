/** 
 * USER INPUT 
 *
 * challenge #1 (easy)
 * https://www.reddit.com/r/dailyprogrammer/comments/pih8x/easy_challenge_1/ 
 *
 * sarthak7u@gmail.com
 */

package main

import "fmt"

func main() {

	var name, age, uname string

	fmt.Print("Enter you name: ")
	fmt.Scanln(&name)
	fmt.Print("Enter you age: ")
	fmt.Scanln(&age)
	fmt.Print("Enter you uname: ")
	fmt.Scanln(&uname)

	fmt.Println("your name is " + name + ", you are " + age + " years old, and your username is " + uname)
}
