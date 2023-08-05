(*
  Caesar Cipher
  Challenge #3 (easy)
  https://www.reddit.com/r/dailyprogrammer/comments/pkw2m/2112012_challenge_3_easy/

  sarthak7u@gmail.com
*)


let rotateCharForward chr key =
  let i = Char.code chr in
  match i with
    | i when i >= 65 && i <= 90 -> Char.chr (((i - 65 + key ) mod 26) + 65)
    | i when i >= 97 && i <= 122 -> Char.chr (((i - 97 + key) mod 26) + 97)
    | _ -> chr

let rotateCharBackward chr key =
  let i = Char.code chr in
  match i with
    | i when i >= 65 && i <= 90 -> Char.chr (if i - 65 - key < 0 then i + 26 - key else i - key)
    | i when i >= 97 && i <= 122 -> Char.chr (if i - 97 - key < 0 then i + 26 - key else i - key)
    | _ -> chr

let encrypt str key =
  str
    |> String.map (fun x -> rotateCharForward x key)
    |> String.iter (fun x -> print_char x)

let decrypt str key =
  str
    |> String.map (fun x -> rotateCharBackward x key )
    |> String.iter (fun x -> print_char x)

let main () = 
  encrypt "helloA" 12;
  print_newline ();
  decrypt "tqxxaM" 12;
  print_newline ()

let () = main()
