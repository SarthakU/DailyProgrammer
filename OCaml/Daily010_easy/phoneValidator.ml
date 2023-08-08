(*
  Phone Validator 
  #6 (easy)
  https://www.reddit.com/r/dailyprogrammer/comments/pv98f/2182012_challenge_10_easy/

  sarthak7u@gmail.com
*)

let rec all_numeric nums =
  match String.length nums with
    | 0 -> true
    | 1 -> Char.code (String.get nums 0) >= 48 && Char.code (String.get nums 0) < 58
    | _ -> all_numeric (String.sub nums 0 1) && all_numeric(String.sub nums 1 (String.length (nums) - 1))

let strip_special query =
  query
    |> String.map (fun x -> if (x == '-' || x == '.' || x == '(' || x == ')' || x == ' ') then (Char.chr 0) else x)

let check_special_chars query =
  match query with
    | s when String.get query 3 == '-' -> String.get s 7 == '-'
    | s when String.get query 3 == '.' -> String.get s 7 == '.'
    | s when String.get query 0 == '(' -> String.get s 4 == ')' && ((String.get s 5 == ' ' && String.get s 10 == '-') || (String.get s 9 == '-')) 
    | _ -> false

let validate query =
  let ln = String.length query in
  match ln with
    | 10 -> all_numeric query  
    | n when n <= 14 && n > 11 -> check_special_chars query && all_numeric (strip_special query);
    | _ -> false

let () =
  print_endline ( Bool.to_string (validate "(1234)") ^ " false");
  print_endline ( Bool.to_string (validate "1234567899") ^ " true");
  print_endline ( Bool.to_string (validate "123-456-7899") ^ " true");
  print_endline ( Bool.to_string (validate "(123)4567-899") ^ " true" );
  print_endline ( Bool.to_string (validate "(123) 4567-899") ^ " true" );
  print_endline ( Bool.to_string (validate "(123)  4567-899") ^ " false" );
  print_endline ( Bool.to_string (validate "(123 4567-899") ^ " false" );
  print_endline ( Bool.to_string (validate "(123) a567-899") ^ " false" );
  print_endline ( Bool.to_string (validate "123-45-6789") ^ " false" );
  print_endline ( Bool.to_string (validate "123:4567890") ^ " false" );
  print_endline ( Bool.to_string (validate "123/456-7890") ^ " false" );
  
