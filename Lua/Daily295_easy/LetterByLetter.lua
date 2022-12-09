-- Letter By Letter
--
-- challenge #295 (easy)
-- https://www.reddit.com/r/dailyprogrammer/comments/5hy8sm/20161212_challenge_295_easy_letter_by_letter/
--
--
-- sarthak7u@gmail.com
--

local function letterByLetter(source, target)
  local ln = string.len(source)
  for i = 1, ln do
    print(string.sub(target, 0, i) .. string.sub(source, i + 1))
  end
end

-- letterByLetter('floor', 'brake')

-- letterByLetter('wood', 'book')

-- local source = 'a fall to the floor'
-- local target = 'braking the door in'
-- letterByLetter('a fall to the floor', 'braking the door in')
