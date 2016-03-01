-module(pairs).
-export([main/0, pairs/2]).

pairs([], _) -> 0;
pairs(A, K) -> 
	pairs(sets:from_list(A),A, K, 0).
pairs(SetA, [H|T], K, C) ->
	IsElement = sets:is_element(K+H, SetA),
	if IsElement -> pairs(SetA, T, K, C+1);
	true -> pairs(SetA, T, K, C)
end;
pairs(_, [], _, C) -> C.

split(String, Token) ->
	lists:map(fun(X) -> {Int, _} = string:to_integer(X),
				Int end,
		string:tokens(String, Token)).

read_input() ->
	string:strip(io:get_line(""), right, 10).

main() ->
	[_, K] = split(read_input()," "),
	A = split(read_input(), " "),
	Res = pairs(A, K),
	io:format("~p~n", [Res]).
