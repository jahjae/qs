defmodule Mushaf do


  def read() do
    receive do
      {cid, :page, x} -> send(cid, {:page, x})
      {cid, :sura, x} -> send(cid, {:sura, x})
    end

  end

  def load() do
    kode = File.read!("data/db/mushaf.db") |> String.split("\r\n")
    unicode(kode)
  end

  def unicode([]) do
    :ok
  end
  def unicode(x) do
    [head | tail] = x
    IO.puts(head)
    unicode(tail)
  end

end
