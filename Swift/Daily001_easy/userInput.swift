/** 
 * User Input 
 *
 * challenge #1 (easy)
 * https://www.reddit.com/r/dailyprogrammer/comments/pih8x/easy_challenge_1/ 
 *
 * sarthak7u@gmail.com
 */

func getField(_ label: String) -> String? {
    print("Your \(label):", terminator: " ")
    let f = readLine()
    return f
}

let name = getField("Name")
let age = getField("Age")
let uname = getField("Username")


if (name != nil && age != nil && uname != nil) {
    print("your name is \(name!), you are \(age!) years old, and your username is \(uname!)")
} else {
    print("Bad Request")
}


