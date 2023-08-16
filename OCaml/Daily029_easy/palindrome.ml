(*
   PALINDROME
   Challenge #29 (easy)
   https://www.reddit.com/r/dailyprogrammer/comments/r8a70/3222012_challenge_29_easy/

   sarthak7u@gmail.com
*)

let rec isPalindromeAux str fIndex lIndex =
  match fIndex, lIndex with
  | f, l when f == l -> true
  | f, l when f > l -> true
  | _ ->
    String.get str fIndex == String.get str lIndex
    && isPalindromeAux str (fIndex + 1) (lIndex - 1)
;;

let isPalindrome str = isPalindromeAux str 0 (String.length str - 1)

let () =
  let isPal = isPalindrome "hannah" in
  print_string (Bool.to_string isPal)
;;

