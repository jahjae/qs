-module(core).
-export([mushaf/0, start/0]).

start()->
    ok.

mushaf()->
    receive
        {Cid, juz}->
            Cid ! {juz};
        {Cid, page}->
            Cid ! {page};
        {Cid, ayah}->
            Cid ! {ayah};
        {Cid, word}->
            Cid ! {word}
    end.