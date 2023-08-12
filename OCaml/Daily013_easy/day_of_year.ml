(*
   DAY OF YEAR 
   Challenge #13 (easy)
   https://www.reddit.com/r/dailyprogrammer/comments/pzo4w/2212012_challenge_13_easy/

   sarthak7u@gmail.com
*)

let days = [| 31; 28; 31; 30; 31; 30; 31; 31; 30; 31; 30; 31 |]

let is_leap_year year =
  match year with
  | y when y mod 400 == 0 -> true
  | y when y mod 100 == 0 -> false
  | y when y mod 4 == 0 -> true
  | _ -> false
;;

let caculate_days year month day =
  let rec calculate_days_aux month day acc =
    match month with
    | m when m > 1 -> acc + calculate_days_aux (month - 1) day days.(m - 1)
    | m when m == 1 -> acc + day
    | _ -> acc
  in
  if is_leap_year year && month > 2
  then 1 + calculate_days_aux month day 0
  else calculate_days_aux month day 0
;;

let () =
  print_int (caculate_days 2020 3 31);
  print_newline ()
;;
