(*
  Morse Code Decrypt
  #7 (easy)
  https://www.reddit.com/r/dailyprogrammer/comments/pr2xr/2152012_challenge_7_easy/

  sarthak7u@gmail.com
*)

let get_lookup () = 
  let morse_hash = Hashtbl.create 26 in
  let morse_list = [|"a";"b";"c";"d";"e";"f";"g";"h";"i";"j";"k";"l";"m";"n";"o";"p";"q";"r";"s";"t";"u";"v";"w";"x";"y";"z"|] in
  let morse_code = [|"._";"_...";"_._."; "_.."; "."; ".._.";
  "__."; "...."; ".."; ".___"; "_._"; "._.."; "__"; "_.";
  "___"; ".__."; "__._"; "._."; "..."; "_"; ".._"; "..._";
  ".__"; "_.._"; "_.__"; "__.."|] in

  let i = ref 0 in
  while !i < 26 do
    Hashtbl.add morse_hash morse_code.(!i) morse_list.(!i);
  i := !i + 1
  done;
  morse_hash

let rec decrypt_morse query =
  let l = String.split_on_char ' ' query in
  let hsh = get_lookup() in

  match l with
    | [] -> query
    | [h] -> Hashtbl.find hsh h
    | h::t -> Hashtbl.find hsh h ^ decrypt_morse (String.concat "" t )


let () =
  let decrypted = decrypt_morse(".... .") in
  print_string decrypted;
  print_newline ();

