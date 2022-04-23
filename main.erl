-module(main).
-export([start/0, call/1]).

start()->
    Sid = spawn(mushaf, qs, []),
    spawn(main, call, [Sid]).

call(Sid)->
    Sid ! {ayat, self()},
    receive
        {ayat}->
            io:format("ayat")
    end.