(*
   DIVIDE DUPLICATE STRINGS
   Challenge #26 (easy)
   https://www.reddit.com/r/dailyprogrammer/comments/qzil1/3162012_challenge_26_easy/

   sarthak7u@gmail.com
*)

let rec returnDuplicatesAux str str1 str2 idx =
  match str, str1 with
  | s, _ when String.length s == idx -> [ str1; str2 ]
  | "", _ -> [ str1; str2 ]
  | s, "" when String.length str > 0 ->
    returnDuplicatesAux str (str1 ^ String.make 1 (String.get str idx)) str2 (idx + 1)
  | s, s1 when String.get s idx == String.get s1 (String.length s1 - 1) ->
    returnDuplicatesAux str str1 (str2 ^ String.make 1 (String.get str idx)) (idx + 1)
  | s, s1 ->
    returnDuplicatesAux str (str1 ^ String.make 1 (String.get str idx)) str2 (idx + 1)
;;

let returnDuplicates str = returnDuplicatesAux str "" "" 0

let () =
  let strs = returnDuplicates "flabby aapples" in
  List.iter (fun str -> print_endline str) strs
;;
