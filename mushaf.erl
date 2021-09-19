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
  {ok, File} = file:read_file("data/db/mushaf.db"),
  Huruf = re:split(File, "\r\n<<>>"),
  unicode(Huruf).

unicode([])->
  ok;
unicode(X)->
  [Head|Tail] = X,
  io:format("~p~n", [Head]),
  unicode(Tail).

