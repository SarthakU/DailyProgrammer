--
-- user input
-- challenge #1 (easy)
-- https://www.reddit.com/r/dailyprogrammer/comments/pih8x/easy_challenge_1/
--
--
-- sarthak7u@gmail.com
--

main = do
    putStrLn "What is your Name?"
    name <- getLine

    putStrLn "What is your Age?"
    age <- getLine

    putStrLn "What is your User Name?"
    uname <- getLine

    let out = "Your Name is " ++ name ++ ", you are " ++ age ++ " years old, anzd your username is " ++ uname
    putStrLn out

    let fileName = "out.txt"
    writeFile fileName out
