-module(mushaf).
-export([read/0, load/0, unicode/1]).

read()->
  receive
    {Cid, halaman, X} -> Cid ! {halaman, X};
    {Cid, juz, X} ->  Cid ! {juz, X};
    {Cid, surat, X} ->  Cid ! {surat, X};
    {Cid, ayat, X} ->  Cid ! {ayat, X}
  end.

load()->
  File = file:open("data/db/mushaf.db",[read]),
  io:format("~w~n", [File]),
  unicode(File).

unicode([])->
  ok;
unicode(X)->
  [Head|Tail] = X,
  io:format("~p", [Head]),
  unicode(Tail).

