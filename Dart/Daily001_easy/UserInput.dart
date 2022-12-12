/** 
 * USER INPUT 
 *
 * challenge #1 (easy)
 * https://www.reddit.com/r/dailyprogrammer/comments/pih8x/easy_challenge_1/ 
 *
 * sarthak7u@gmail.com
 */

import 'dart:io';

void main() {
  print("What is your name?");
  String? name = stdin.readLineSync();
  print("What is your age?");
  String? age = stdin.readLineSync();
  print("What is your user name?");
  String? uname = stdin.readLineSync();

  print(
      "your name is ${name}, you are ${age} years old, and your username is ${uname}");
}
