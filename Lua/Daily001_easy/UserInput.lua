-- USER INPUT 
--
-- challenge #1 (easy)
-- https://www.reddit.com/r/dailyprogrammer/comments/pih8x/easy_challenge_1/ 
--
--
-- sarthak7u@gmail.com
--

print("What is your Name?")
local name = io.read()

print("What is your age?")
local age = io.read()

print("What is your username?")
local uname = io.read()

local output = "your name is " .. name .. ", you are " .. age .. " years old, and your username is " .. uname

print(output)

local f = io.open('output.txt', 'w')
if f then
  io.output(f)
  io.write(output)
  io.close(f)
end
