-module(mushaf).
-export([read/0, load/0]).

read()->
  receive
    {Cid, halaman, x} -> Cid ! {:halaman, x}
    {Cid, juz, x} ->  Cid ! {:juz, x}
    {Cid, surat, x} ->  Cid ! {:surat, x}
    {Cid, ayat, x} ->  Cid ! {:ayat, x}
  end.

load()->
  Huruf = File.read!("data/db/mushaf.db") |> String.split("\r\n")
  unicode(Huruf).

unicode([])->
  ok,
unicode(x)->
    [First | Next] = x
    IO.puts(First)
    unicode(Next).


