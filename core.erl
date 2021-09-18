-module(core).
-export([mushaf/0]).

mushaf()->
    receive
        {Cid, page}->
            Cid ! {page},
    end.