(*
  Compound interest calculator
  Challenge #2 (easy)
  https://www.reddit.com/r/dailyprogrammer/comments/pjbj8/easy_challenge_2/

  sarthak7u@gmail.com
*)

let compound_interest p r n t =
  p *. Float.pow (1.0 +. (r /. n)) (n *. t)

let main () = 
  (* let f = compound_interest 10000.0 0.06 12.0 20.0 in *)
  let f = compound_interest 10000.0 0.07 12.0 25.0 in

  print_float f;
  print_newline ()

let () = main()
