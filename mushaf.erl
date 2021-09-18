-module(mushaf).
-export([open/0]).

open()->
    receive
        {Cid, page, X} ->
            Cid ! {page, X}
    end.