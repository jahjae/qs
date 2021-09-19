-module(qs).
-export([page/1, sura/1,read/3]).

page(X)->
  Sid = spawn(mushaf, read, []),
  spawn(qs, read, [Sid, halaman, X]).

sura(X)->
  Sid = spawn(mushaf, read, []),
  spawn(qs, read, [Sid, surat, X]).

read(I, S, X)->
  I ! {self(), S, X},
  receive
    {halaman, X}->
      io:format("Halaman ~p~n", [X]);
    {juz, X}->
      io:format("Juz ~p~n", [X]);
    {surat, X}->
      io:format("Sura ~p~n", [X])
  end.