defmodule Qs do
	def start do
		x = IO.gets "Surat : "
		y = IO.gets "Ayat  : "
    	sid = spawn Mushaf, :quran, []
    	spawn Qs, :mushaf, [sid, x, y]
  	end

  	def mushaf(sid, x, y) do
		send sid, {:ayat, self(), x, y}
    	receive do
      		{:ayat, arg1, _arg2} ->
				IO.puts "QS #{arg1}"
		end
    end
end
