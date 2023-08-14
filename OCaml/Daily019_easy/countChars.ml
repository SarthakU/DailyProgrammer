(*
   GUTENBERG ALPHANUMERIC COUNT
   Challenge #19 (easy)
   https://www.reddit.com/r/dailyprogrammer/comments/qlwrc/372012_challenge_19_easy/

   sarthak7u@gmail.com
*)

let isStart str =
  match str with
  | "*** START O" -> true
  | _ -> false
;;

let isEnd str =
  match str with
  | "End of the " -> true
  | _ -> false
;;

let isAlphanumeric chr =
  match chr with
  | 'a' .. 'z' -> true
  | 'A' .. 'z' -> true
  | '1' .. '9' -> true
  | _ -> false
;;

let countAlphanumeric str =
  List.of_seq (String.to_seq str)
  |> List.map (fun x -> if isAlphanumeric x then 1 else 0)
  |> List.fold_left ( + ) 0
;;

let () =
  let count = ref 0 in
  let start = ref false in
  let file = open_in "sherlock.txt" in
  try
    while true do
      let ln = input_line file in
      let sub = if String.length ln >= 11 then String.sub ln 0 11 else "" in
      count := if !start then !count + countAlphanumeric ln else !count;
      start := if (isStart sub || !start) && not (isEnd sub) then true else false
    done
  with
  | e ->
    print_int !count;
    print_newline ()
;;
