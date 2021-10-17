-module(mushaf).
-export([qs/0]).

qs()->
    receive
        {ayat, Cid, X}->
            Cid ! {surat, X}
    end.

