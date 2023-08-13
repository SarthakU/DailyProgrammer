(*
   TEXT PHONE NUMBER 
   Challenge #18 (easy)
   https://www.reddit.com/r/dailyprogrammer/comments/qit0h/352012_challenge_18_easy/

   sarthak7u@gmail.com
*)

let getT9 num =
  match num with
  | num when num > 7.4 -> 9
  | num when num > 6.4 -> 8
  | num when num > 5. -> 7
  | num when num > 4. -> 6
  | num when num > 3. -> 5
  | num when num > 2. -> 4
  | num when num > 1. -> 3
  | _ -> 2
;;

let () =
  let alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" in
  let phone = "1-800-COMCAST" in
  let phone_arr = Array.of_list (String.split_on_char '-' phone) in
  let com = phone_arr.(2) in
  print_string phone_arr.(0);
  print_string "-";
  print_string phone_arr.(1);
  print_string "-";
  List.of_seq (String.to_seq com)
  |> List.map (fun x -> Float.of_int (String.index alphabets x + 1))
  |> List.iter (fun x -> print_int (getT9 (x /. 3.)));
  print_newline ()
;;
