(*
  Numberical order of stdin 
  Challenge #9 (easy)
  https://www.reddit.com/r/dailyprogrammer/comments/pu1rf/2172012_challenge_9_easy/


  sarthak7u@gmail.com
*)

let main (): unit  =
  print_endline "Enter all numbers you like comma separated";

  let numbers = read_line() in 
  let splited = String.split_on_char ',' numbers in

   splited
    |> List.map (fun x -> int_of_string x)
    |> List.sort compare 
    |> List.map (fun x -> string_of_int x)
    |> List.iter (fun x -> print_endline x ) 

let () = main()
