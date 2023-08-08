(*
  99 Beers 
  Challenge #8 (easy)
  https://www.reddit.com/r/dailyprogrammer/comments/pserp/2162012_challenge_8_easy/

  sarthak7u@gmail.com
*)

let print_beer how_many =
  let _how_many = Int.to_string how_many in
  print_endline (_how_many ^ " bottles of beer on the wall, " ^ _how_many ^ " bottles of beer" );
  print_endline ("Take one down and pass it around, " ^ (Int.to_string (how_many - 1)) ^ " bottles of beer on the wall" );
  print_newline ()

let rec beers how_many =
  match how_many with
    | 0 -> print_endline "No more bottles of beer on the wall, no more bottles of beer\nGo to the store and buy some more, 99 bottles of beer on the wall"
    | _ -> print_beer how_many; beers (how_many - 1)

let () =
  beers 99

