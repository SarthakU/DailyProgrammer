/** 
 * Sum Square 
 *
 * challenge #34 (easy)
 * https://www.reddit.com/r/dailyprogrammer/comments/rmmn8/3312012_challenge_34_easy/t 
 *
 * sarthak7u@gmail.com
 */

import 'dart:math';


sumSquare(num1, num2, num3) {
  var a1 = max<num>(num2, num1);
  if (a1 == num1) {
    return pow(a1, 2) + pow(max(num2, num3), 2);
  } else {
    return pow(a1, 2) + pow(max(num1, num3), 2);
  }
}

void main() {
  // print(sumSquare(4,2,3));
}
