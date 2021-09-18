-module(core).
-export([mushaf/0]).

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