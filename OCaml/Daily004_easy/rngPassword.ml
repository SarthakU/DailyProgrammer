(*
  Random Password 
  Challenge #4 (easy)
  https://www.reddit.com/r/dailyprogrammer/comments/pm6oj/2122012_challenge_4_easy/

  sarthak7u@gmail.com
*)

let getSpecial () =
  let special = ['#';'@';'!';'$';'%';'^';'&';'*';'(';')';'-';'=';'+';'_'] in 
  let r = Random.int(List.length(special)) in 
  List.nth special r 

let getRandomChar () =
  Random.self_init ();

  let flag = Random.int 125 in
  let char_int = Random.int 26 in

  match flag with 
    | f when f > 50 && f <=100 -> Char.chr (char_int + 65)
    | f when f <= 50 -> Char.chr (char_int + 97)
    | _ -> getSpecial()

let getRandomString len =
  let char_seq = List.init len (fun x -> '0')
    |> List.map (fun x -> getRandomChar())
  in

  String.of_seq(List.to_seq(char_seq))

let () =
  print_endline "Enter length for your required password: ";
  let len = read_int() in 
  let pass = getRandomString(len) in
  print_endline pass

