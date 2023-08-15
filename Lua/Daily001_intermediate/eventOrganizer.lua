--
-- event organizer 
-- challenge #1 (intermediate)
-- https://www.reddit.com/r/dailyprogrammer/comments/pihtx/intermediate_challenge_1/ 
--
--
-- sarthak7u@gmail.com
--

local events = {}

local function printTitle(str)
  print("--------------------")
  io.write("|- ")
  print(str)
  print("--------------------")
end

local function addEvent()
  printTitle("Add new Event")
  io.write("Title of new Event: ")
  local title = io.read()

  io.write("Hour of day: ")
  local hour = io.read()

  events[hour] = title
end

local function viewEvents()
  printTitle("Scheduled Events")

  for key, val in pairs(events) do
    print(key, val)
  end
end

local function deleteEvent()
  io.write("Enter Hour to delete: ")
  local hour = io.read()

  events[hour] = nil
end

local function menu()
  printTitle("Menu")
  print("")
  print("1. View events")
  print("2. Add event")
  print("3. Delete event")

  local opt = io.read()

  if opt == "1" then
    viewEvents()
  elseif opt == "2" then
    addEvent()
  elseif opt == "3" then
    deleteEvent()
  else
    printTitle("Bye")
    return "quit"
  end
end


while true do
  local m = menu()

  if m == "quit" then
    break
  end
end
