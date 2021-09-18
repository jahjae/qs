-module(core).
-export([mushaf/0, load/0]).

load()->
    ok.

mushaf()->
    receive
        {Cid, surah, X, 0} ->
            Cid ! {surah, X, 0};
        {Cid, surah, X, Y} ->
            Cid ! {surah, X, Y}
    end.