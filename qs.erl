-module(qs).
-export([start/0, message/1]).

start()->
  Sid = spawn(core, mushaf, []),
  spawn(qs, message, [Sid]).

message(Sid)->
  Sid ! {self(), page},
  receive
    {page}->
      io:format("Done ~n")
  end.