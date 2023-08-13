(*
   PRIME BELOW N
   Challenge #20 (easy)
   https://www.reddit.com/r/dailyprogrammer/comments/qnkro/382012_challenge_20_easy/

   sarthak7u@gmail.com
*)

let rec isPrime n acc =
  match acc with
  | [] -> true
  | hd :: tl when n mod hd == 0 -> false
  | hd :: tl -> isPrime n tl
;;

let rec primes n acc mx =
  match n with
  | 2 -> primes (n + 1) [ 2 ] mx
  | n when n > mx -> acc
  | _ -> primes (n + 1) (acc @ if isPrime n acc then [ n ] else []) mx
;;

let getPrimesBelowN n = primes 2 [] n

let () =
  let p = getPrimesBelowN 2000 in
  p
  |> List.iter (fun x ->
    print_int x;
    print_newline ())
;;
