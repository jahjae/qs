-module(qs).
-export([page/1, message/2]).

page(X)->
  Sid = spawn(mushaf, open, []),
  spawn(qs, message, [Sid, X]).

message(Sid, X)->
  Sid ! {self(), page, X},
  receive
    {page, X}->
      io:format("Page ~p~n", [X])
  end.