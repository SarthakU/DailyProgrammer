(*
   LIST HALF AND HALF 
   Challenge #23 (easy)
   https://www.reddit.com/r/dailyprogrammer/comments/quli5/3132012_challenge_23_easy/

   sarthak7u@gmail.com

*)
let rec halfListAux lst1 lst2 =
  let len1 = List.length lst1 in
  let len2 = List.length lst2 in
  match len1, len2, lst1 with
  | l1, l2, _ when l1 == l2 -> [ lst1; lst2 ]
  | l1, l2, _ when abs (l1 - l2) == 1 -> [ lst1; lst2 ]
  | _, _, hd :: tl -> halfListAux tl (lst2 @ [ hd ])
  | _ -> [ lst1; lst2 ]
;;

let halfList lst = halfListAux lst []

let () =
  let lst = [ 1; 2; 3; 4; 5; 6; 7; 8; 9; 10; 11 ] in
  let halved = halfList lst in
  halved
  |> List.iter (fun x ->
    List.iter
      (fun y ->
        print_int y;
        print_string " ")
      x;
    print_newline ())
;;
