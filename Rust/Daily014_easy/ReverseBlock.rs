/** 
 * Reverse Block 
 *
 * challenge #14 (easy)
 * http://www.reddit.com/r/dailyprogrammer/comments/pkw2m/2112012_challenge_3_easy/ 
 *
 * sarthak7u@gmail.com
 */

fn reverse_block(arr: &mut Vec<usize>) -> &Vec<usize> {
    for idx in 0..arr.len() {
        if idx % 2 == 1 {
            let temp = arr[idx];
            arr[idx] = arr[idx - 1];
            arr[idx - 1] = temp;
        }
    }
    return arr;
}

fn main() {
    let mut input = vec![12, 24, 32, 44, 55, 66];
    reverse_block(&mut input);
    println!("{:?}", input);
}
