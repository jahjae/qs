defmodule Mushaf do
  def read() do
    receive do
      {cid, :halaman, x} -> send(cid, {:halaman, x})
      {cid, :juz, x} -> send(cid, {:juz, x})
      {cid, :surat, x} -> send(cid, {:surat, x})
      {cid, :ayat, x} -> send(cid, {:ayat, x})
    end

  end

  def load() do
    huruf = File.read!("data/db/mushaf.db") |> String.split("\r\n")
    unicode(huruf)
  end

  def unicode([]) do
    :ok
  end

  def unicode(x) do
    [first | next] = x
    IO.puts(first)
    unicode(next)
  end

end
