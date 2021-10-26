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
		send sid, [:ayar self(), args1, args2]
	end

	def page(args1) do
		args1
	end

	def quran do
		receive do
			{:ayat, args1, args2} ->
				IO.puts args1, args2

			{:surat, args1}
		end

	end
end
