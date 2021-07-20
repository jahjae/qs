-module(qs).
-export([load/0, run/0]).


run()->
    spawn(qs, load).
    

load()->
    ok.
    

