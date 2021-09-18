-module(core).
-export([mushaf/0, start/0]).

start()->
    ok.

mushaf()->
    receive
        {Cid, surah, X, 0} ->
            Cid ! {surah, X};
        {Cid, surah, X, Y} ->
            Cid ! {surah, X, Y}
    end.