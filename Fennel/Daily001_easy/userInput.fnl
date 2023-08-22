; 
;  user input 
;  challenge #1 (easy)
;  https://www.reddit.com/r/dailyprogrammer/comments/pih8x/easy_challenge_1/ 
; 
; 
;  sarthak7u@gmail.com
; 

(print "Your Name :")
(local name (.. (io.stdin:read "*l")))

(print "Your Age :")
(local age (.. (io.stdin:read "*l")))
  
(print "Your Username :")
(local uname (.. (io.stdin:read "*l")))

(print (.. "your name is: " name ", you are " age" years old, and your username is "uname))


  
