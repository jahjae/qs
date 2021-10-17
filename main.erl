-module(main).
-export([start/0, qs/1]).

start()->
    Sid = spawn(mushaf, qs, []),
    spawn(main, qs, [Sid]).

qs(Sid)->
    Sid ! {ayat, self(), '1'},
    receive
        {ayat, X}->
            io:format("ayat ~p~n",[X])
    end.