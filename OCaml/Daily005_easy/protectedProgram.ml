(*
  Password Protected File
  #5 (easy)
  https://www.reddit.com/r/dailyprogrammer/comments/pnhyn/2122012_challenge_5_easy/

  sarthak7u@gmail.com
*)

let rec read_file ic (prev: string list) =
  let _line = input_line (ic) in

  try 
    match _line with 
      | l -> read_file ic [l] @ prev
  with 
    | End_of_file -> prev


let getPasswords () =
  let ic = open_in "./config" in 
  let users = read_file ic [] in
  users

let () =
  print_endline "Enter the Password";
  let user_input = read_line() in 

  let passwords = getPasswords () in

  let result = List.mem user_input passwords in 

  match result with 
    | true -> print_endline "Correct Password"
    | false -> print_endline "Incorrect Password"


