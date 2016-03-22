-module(list_filter).
-export([main/0, filter_list/2]).

filter_list(List, Limit)->
	lists:reverse(filter_list(List, Limit, [])).
filter_list([], _, AccList)-> AccList;
filter_list([H|T], Limit, AccList) when H < Limit ->
	filter_list(T, Limit, [H|AccList]);
filter_list([_|T], Limit, AccList)->
	filter_list(T, Limit, AccList).

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
	Output = filter_list(X, H),
	print_output(Output).
