(*
   REMOVE SINGLE DUPLICATE 
   Challenge #28 (easy)
   https://www.reddit.com/r/dailyprogrammer/comments/r59kk/3202012_challenge_28_easy/

   sarthak7u@gmail.com
*)

let rec dedupeAux arr hsh prev =
  match arr with
  | [] -> prev, 0
  | hd :: tl ->
    (try prev @ tl, Hashtbl.find hsh hd with
     | e ->
       Hashtbl.add hsh hd hd;
       dedupeAux tl hsh (prev @ [ hd ]))
;;

let dedupe arr = dedupeAux arr (Hashtbl.create (List.length arr)) []

let () =
  let f = [ 1; 2; 3; 4; 33; 5; 3; 52 ] in
  let r = dedupe f in
  match r with
  | x, y ->
    print_int y;
    print_newline ();
    List.iter
      (fun i ->
        print_int i;
        print_string " ")
      x;
    print_newline ()
;;
