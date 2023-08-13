(*
   STRING INTERSECTION 
   Challenge #16 (easy)
   https://www.reddit.com/r/dailyprogrammer/comments/q8aom/2272012_challenge_16_easy/

   sarthak7u@gmail.com
*)

let () =
  let s1 = "Daily Programmer" in
  let s2 = "aeiou " in
  let s3 = s1 |> String.map (fun x -> if String.contains s2 x then Char.chr 0 else x) in
  print_string s3
;;
