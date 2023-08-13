(*
   LEFT/RIGHT JUSTIFICATION 
   Challenge #15 (easy)
   https://www.reddit.com/r/dailyprogrammer/comments/q4c34/2242012_challenge_15_easy/

   sarthak7u@gmail.com
*)

let read_file filename =
  let file = open_in filename in
  let rec read_lines acc =
    try
      let line = input_line file in
      read_lines (line :: acc)
    with
    | End_of_file -> List.rev acc
  in
  let lines = read_lines [] in
  close_in file;
  lines
;;

let write_file filename contents =
  let file = open_out filename in
  contents |> List.iter (fun x -> Printf.fprintf file "%s\n" x)
;;

let rec right_justify conents cols =
  match conents with
  | [] -> []
  | hd :: tl ->
    [ String.make (cols - String.length hd) (Char.chr 32) ^ hd ] @ right_justify tl cols
;;

let rec left_justify contents =
  match contents with
  | [] -> []
  | hd :: tl -> [ String.trim hd ] @ left_justify tl
;;

let () =
  let f = read_file "test.txt" in
  let rf = right_justify f 80 in
  let lf = left_justify f in
  write_file "test.txt" rf;
  write_file "test.txt" lf
;;
