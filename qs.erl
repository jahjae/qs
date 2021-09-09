-module(qs).
-export([start/0, message/1, display/2]).

start()->
  Sid = spawn(qs, mushaf, []).
  spawn(qs, display, [Sid])

mushaf(Sid)->
  receive
    { Cid, Format, Number }->
      Cid ! {display, [Format, Number]}
  end

display(Format, Number)->
  ok.
