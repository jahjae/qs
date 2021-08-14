-module(ui).
-export([read/1]).

read({huruf, N})->
    {huruf, N};
read({kata, N})->
    {kata, N};
read({halaman, N})->
    {halaman, N};
read({ayat, N})->
    {ayat, N};
read({surat, N})->
    {surat, N};
read({juz, N})->
    {juz, N}.


