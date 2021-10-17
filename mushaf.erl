-module(mushaf).
-export([qs/0]).

qs()->
    receive
        {ayat, Cid}->
            Cid ! {surat},
            qs
    end.

