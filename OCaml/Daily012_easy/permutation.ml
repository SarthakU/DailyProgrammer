(*
   STRING PERMUTATIONS
   Challenge #12 (easy)
   https://www.reddit.com/r/dailyprogrammer/comments/pxs2x/2202012_challenge_12_easy/

   sarthak7u@gmail.com
*)

let printer l =
  l
  |> List.iter (fun x ->
    print_string x;
    print_string " ")
;;

let printer2 l =
  l
  |> List.iter (fun x ->
    printer x;
    print_newline ())
;;

let rotate (l : string list) =
  match l with
  | [ x ] -> [ x ]
  | hd :: tl -> tl @ [ hd ]
  | [] -> []
;;

let rec roatateN l n =
  match n with
  | 0 -> l
  | x -> roatateN (rotate l) (n - 1)
;;

let rec permutations_aux (l : string list) =
  match l with
  | [] -> []
  | [ x ] -> [ [ x ] ]
  | hd :: tl ->
    List.mapi
      (fun idx x ->
        List.flatten (List.map (fun x -> [ hd ] @ x) (permutations_aux (roatateN tl idx))))
      tl
;;

let permutations (l : string list) =
  l |> List.mapi (fun idx x -> List.flatten (permutations_aux (roatateN l idx)))
;;

let () =
  let s = [ "a"; "b"; "c"; "d" ] in
  printer2 (permutations s)
;;
