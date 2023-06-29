-module(qs).
-export([main/1,formula/3]).

main(_)->
  formula(add, 12, 14).

formula(add, A, B)->
  io.format("",A + B).
