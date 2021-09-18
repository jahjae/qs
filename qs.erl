-module(qs).
-export([surah/1, surah/2, message/3]).

page(X)->
  Mid = spawn(core, mushaf, []),
  spawn(qs, message, [Mid, X]).

message(Mid, X)->
  Sid ! {self(), page, X},
  receive
    {page, X}->
      io:format("Page ~p~n", [X])
  end.