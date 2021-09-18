-module(qs).
-export([start/0, message/1]).

start()->
  Sid = spawn(core, mushaf, []).
  spawn(qs, display, [Sid])

message(Sid)->
  Sid ! {self(), page},
  receive
  end.