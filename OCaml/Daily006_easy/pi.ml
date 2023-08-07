(*
  PI
  #6 (easy)
  https://www.reddit.com/r/dailyprogrammer/comments/pp53w/2142012_challenge_6_easy/

  sarthak7u@gmail.com
*)

(* Does not calculate 30 digits *)
let rec calculate_pi_madhava (num:float) acc =
  let nth (n:float) = ((1. *. Float.pow (-1.) num) /. ((2. *. n) +. 1.)) in

  match num with 
    | -1. -> acc
    | _ -> calculate_pi_madhava (num -. 1. ) (acc +. nth (num) )


let () = 
  let pi = calculate_pi_madhava (500000000.) 0. in

  print_float (pi *. 4.);




