(*
   CENTURY AND LEAP YEAR
   Challenge #27 (easy)
   https://www.reddit.com/r/dailyprogrammer/comments/r0r3h/3172012_challenge_27_easy/

   sarthak7u@gmail.com
*)

let isLeapYear year =
  match year with
  | y when y mod 400 == 0 -> true
  | y when y mod 100 == 0 -> false
  | y when y mod 4 == 0 -> true
  | _ -> false
;;

let getCentury year = ((year - 1) / 100) + 1

let () =
  let year = 2000 in
  print_string "Century: ";
  print_int (getCentury year);
  print_newline ();
  print_string "Leap Year: ";
  print_string (Bool.to_string (isLeapYear year));
  print_newline ()
;;
