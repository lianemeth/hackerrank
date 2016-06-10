-module(erlang_exercises).
-compile(export_all).

% Those are not hackerrank exercises, they are part of http://erlang.org/course/exercises.html

p1_ex1(N)->
	receive
		{From, I} when I < N ->
			From ! {self(), I+1},
			io:fwrite("p1 call p2 \n"),
			p1_ex1(N);
		{From, _} ->
			io:fwrite("terminate p1 \n"),
			From ! {self(), terminate}
	end.

p2_ex1()->
	receive
		{Pid1, start} ->
			io:fwrite("start p2 \n"),
			Pid1 ! {self(), 0},
			p2_ex1();
		{_, terminate} ->
			io:fwrite("teminate p2 \n");
		{From, I} ->
			io:fwrite("p2 call p1 \n"),
			From ! {self(), I},
			p2_ex1()
	end.


ex_1(N) ->
	Pid1 = spawn(erlang_exercises, p1_ex1, [N]),
	Pid2 = spawn(erlang_exercises, p2_ex1, []),
	Pid2 ! {Pid1, start}.
