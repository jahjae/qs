-module(qs).
-export([surah/1, surah/2, message/3]).

surah(X)->
  Sid = spawn(core, mushaf, []),
  spawn(qs, message, [Sid, X,0]).
  
surah(X, Y)->
  Sid = spawn(core, mushaf, []),
  spawn(qs, message, [Sid, X,Y]).

message(Sid, X, Y)->
  Sid ! {self(), surah, X, Y},
  receive
    {surah, X}->
      io:format("Surah ~p", [X]);
    {ayah, X, Y}->
      io:format("QS ~p:~p", [X, Y])
  end.