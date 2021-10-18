defmodule Mushaf do
  def quran() do
    receive do
      {:ayat, cid, x, y} ->
        send cid, {:ayat, x, y}
    end

  end
end
