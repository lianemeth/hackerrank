-module(solution).
-export([main/0]).

hello_world(0) -> ok;
hello_world(N) when N > 0 ->
	io:format("Hello World\n"),
	hello_world(N-1).

main() ->
	{ok, [N]} = io:fread("", "~d"),
    hello_world(N).
