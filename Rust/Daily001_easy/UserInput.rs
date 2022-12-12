//
// INTEREST CALCULATOR
// challenge #2 (easy)
// http://www.reddit.com/r/dailyprogrammer/comments/pjbj8/easy_challenge_2/
//
// sarthak7u@gmail.com
//

fn main() {
    let stdin = std::io::stdin();
    let mut name = String::new();
    let mut age = String::new();
    let mut uname = String::new();

    println!("Enter your name:");
    stdin.read_line(&mut name).unwrap();
    println!("Enter your age:");
    stdin.read_line(&mut age).unwrap();
    println!("Enter your user name:");
    stdin.read_line(&mut uname).unwrap();

    // remove new line chars
    name.pop();
    age.pop();
    uname.pop();

    println!(
        "your name is {}, you are {} years old, and your username is {}",
        name, age, uname
    );
}
