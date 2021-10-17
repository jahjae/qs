-module(mushaf).
-export([qs/0]).

qs()->
    receive
        {surat, Cid, X}->
            Cid ! {surat, X};
        {ayat, Cid, X}->
            Cid ! {surat, X}
    end.

