-module(main).
-export([start/0, qs/1]).

start()->
    Sid = spawn(mushaf, qs, []),
    spawn(main, qs, [Sid]).

qs(Sid)->
    Sid ! {ayat, self()},
    receive
        {ayat}->
            io:format("ayat")
    end.