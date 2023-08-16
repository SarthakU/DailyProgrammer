(*
   COUNT VOTES 
   Challenge #25 (easy)
   https://www.reddit.com/r/dailyprogrammer/comments/qxuug/3152012_challenge_25_easy/

   sarthak7u@gmail.com
*)

let rec countVotesAux lst v1 v2 =
  match lst with
  | hd :: tl ->
    countVotesAux tl (if hd == 'A' then v1 + 1 else v1) (if hd == 'B' then v2 + 1 else v2)
  | [] -> [ v1; v2 ]
;;

let countVotes lst = countVotesAux lst 0 0

let () =
  let votes = [ 'A'; 'A'; 'B'; 'A'; 'B'; 'B'; 'A'; 'B' ] in
  let count = countVotes votes in
  match count with
  | [ a; b ] when a > b -> print_endline "Winner -> A"
  | [ a; b ] when a < b -> print_endline "Winner -> B"
  | _ -> print_endline "Its a Tie!"
;;
