(*
   BLOCK REVERSE 
   Challenge #14 (easy)
   https://www.reddit.com/r/dailyprogrammer/comments/q2v2k/2232012_challenge_14_easy/

   sarthak7u@gmail.com
*)

let rec reverse_aux list =
  match list with
  | [ x ] -> [ x ]
  | hd :: tl -> reverse_aux tl @ [ hd ]
  | _ -> list
;;

let reverse list = Array.of_list (reverse_aux (Array.to_list list))

let printer arr =
  arr
  |> Array.iter (fun x ->
    print_int x;
    print_string " ")
;;

let () =
  let arr = [| 12; 24; 32; 44; 55; 66; 99 |] in
  let size = 3 in
  let blocks = Array.make (Array.length arr / size) 0 in
  blocks
  |> Array.mapi (fun idx x -> reverse (Array.sub arr (idx * size) size))
  |> Array.iter (fun x -> printer x);
  let diff = Array.length arr - (Array.length blocks * size) in
  if diff > 0
  then printer (Array.sub arr (Array.length arr - diff) diff)
  else print_newline ();
  print_newline ()
;;
