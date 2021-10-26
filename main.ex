defmodule Qs do
	import Mushaf

	def surat(args1) do
		sid = spawn(Mushaf, quran, [])
		spawn(self(), quran, [sid, arg1])
		send sid, [:surat self(), args1]
	end

	def ayat(args1, args2) do
		sid = spawn Mushaf, quran, []
		spawn self(), quran, [sid, arg1, args2]
		send sid, [:ayat self(), args1, args2]
	end

	def page(args1) do
		sid = spawn Mushaf, quran, []
		spawn self(), quran, [sid, self, arg1]
		send sid, [:page self(), args1]
	end

	def quran(sid, [x]) do
		receive do
			{:ayat, args1, args2} ->
				IO.puts args1, args2

			{:surat, args1}
		end

	end
end
