## Events Calendar
##
## challenge #1 (intermediate)
## https://old.reddit.com/r/dailyprogrammer/comments/pihtx/intermediate_challenge_1/ 
## 
## 
## sarthak7u@gmail.com

IO.puts("1. Add New Event")
IO.puts("2. List Events")
IO.puts("3. Exit")

IO.puts("\n")
IO.puts("Enter your choice: ")
choice = String.trim(IO.gets(""))

defmodule MyModule do
  def get_events() do
    events = File.read!("events.txt")
    IO.puts(events)
  end

  def add_event() do
    IO.puts("Enter event name: ")
    name = String.trim(IO.gets(""))
    IO.puts("Enter event date: ")
    date = String.trim(IO.gets(""))
    IO.puts("Enter event location: ")
    location = String.trim(IO.gets(""))

    prevEvents = File.read!("events.txt")
    event = "#{name},#{date},#{location}"

    File.write("events.txt", prevEvents <> "\n"<> event)
  end
end

header = "Event Name,Event Date,Event Location"
f = File.read!("events.txt")

if f == "" do
  File.write("events.txt", header)
end


case choice do
  "1" -> MyModule.add_event()
  "2" -> MyModule.get_events()
  "3" -> IO.puts("Bye!")
  _ -> IO.puts("Invalid choice")
end

