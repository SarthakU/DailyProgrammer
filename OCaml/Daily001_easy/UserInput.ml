(*
  user Input 
  Challenge #1 (easy)
  https://www.reddit.com/r/dailyprogrammer/comments/pih8x/easy_challenge_1/ 


  sarthak7u@gmail.com
*)


let main () =
  print_endline "What is your name?";
  let name = read_line () in
  
  print_endline "What is your age?";

  let age = read_line () in

  print_endline "What is your uname?";
  let uname = read_line () in

  let output = "Your name is " ^ name ^ ", your age is " ^ age ^ ", and your username is " ^ uname in 
  print_endline output;
  
  let oc = open_out "output.txt" in
  Printf.fprintf oc "%s" output;
  close_out oc

let () = main ()

