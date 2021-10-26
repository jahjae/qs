defmodule Mushaf do
  def quran() do
    receive do
      {:surat, cid, args1} ->
        send cid, {:surat, args1}
      {:ayat, cid, args1, args2} ->
        send cid, {:ayat, args1, args2}
    end

  end
end
