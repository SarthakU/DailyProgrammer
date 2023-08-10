(*
  DAY OF WEEK 
  #11 (easy)
  https://www.reddit.com/r/dailyprogrammer/comments/pwons/2192012_challenge_11_easy/ 

  sarthak7u@gmail.com
*)

type simpleTime = { day : int; month : int; year : int }

let isFuture a b =
  if a.year > b.year then true
  else if a.year == b.year then
    if a.month > b.month then true
    else if a.month == b.month then true
    else false
  else false

let rec getDays curr (target : simpleTime) =
  let current = Unix.gmtime curr in
  let day_of_month = current.tm_mday in
  let year = current.tm_year + 1900 in
  let month = current.tm_mon + 1 in
  let day = current.tm_mday in
  let isF = isFuture { month; year; day } in

  match (month, year) with
  | x, y when y == target.year && x == target.month -> day_of_month - target.day
  | _ when isF target == true ->
      day_of_month
      + getDays (curr -. Int.to_float (day_of_month * 24 * 60 * 60)) target
  | _ when isF target == false ->
      day_of_month
      + getDays (curr +. Int.to_float (day_of_month * 24 * 60 * 60)) target
  | _ -> 0

let () =
  let tim = { day = 26; month = 10; year = 1981 } in
  let curr = Unix.time () in

  let dayDiff = getDays curr tim + 1 in

  let t = Unix.gmtime (curr -. Int.to_float (dayDiff * 24 * 60 * 60)) in
  let days =
    [
      "Monday";
      "Tuesday";
      "Wednesday";
      "Thursday";
      "Friday";
      "Saturday";
      "Sunday";
    ]
  in
  print_endline (List.nth days t.tm_wday)

