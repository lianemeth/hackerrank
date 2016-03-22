-module(list_rep).
-export([main/0, read_input/1, repeat_list/2]).

repeat_list(X, 0) -> X;
repeat_list([], _)-> [];
repeat_list([H|T], S) ->
	Repeated = [H || _ <- lists:seq(1,S)],
	Repeated ++ repeat_list(T, S).

read_input() ->
	lists:reverse(read_input([])).
read_input(List)->
	case io:get_line("") of
		eof ->
			List;
		N ->
			{IntN, _} = string:to_integer(N),
			read_input([IntN | List])
	end.

print_output([]) -> ok;
print_output([H|T]) ->
	io:format("~p\n",[H]),
	print_output(T).

main() ->
	L = read_input(),
	[H|X] = L,
	Output = repeat_list(X, H),
	print_output(Output).
