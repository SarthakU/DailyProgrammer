// INTEREST CALCULATOR
//
// challenge #2 (easy)
// http://www.reddit.com/r/dailyprogrammer/comments/pjbj8/easy_challenge_2/
//
// sarthak7u@gmail.com
//

fn main() {
    // simple interest
    println!("{}",simple_interest(100.0, 5.0, 10.0));

    // comppund interest
    println!("{}",compound_interest(100.0, 5.0, 10.0));
}

fn simple_interest(principal: f64, rate: f64, time: f64) -> f64 {
  return principal * rate * time / 100.0;
}

fn compound_interest(principal: f64, rate: f64, time: f64) -> f64 {
  return principal * (1.0 + rate / 100.0).powf(time) - principal;
}
