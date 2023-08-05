(*
  List Itersection 
  Challenge #22 (easy)
  https://www.reddit.com/r/dailyprogrammer/comments/qr0hg/3102012_challenge_22_easy/

  sarthak7u@gmail.com
*)

let rec merge_uniq l1 l2 =
  match l1 with
    | [] ->  l2 
    | h::t -> if List.mem h l2 then merge_uniq t l2 else merge_uniq t (h::l2)

let main () =
  let arr1 = ["a"; "b"; "2";"3"; "z"] in
  let arr2 = ["c"; "3"; "b"; "u"; "a"] in 

  let result = merge_uniq arr1 arr2 in 

  result
    |> List.iter (fun x -> print_endline x)


let () = main()
