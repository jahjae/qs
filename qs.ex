defmodule Quran do
  def page(x) do
    pid = spawn(Mushaf, :read, [])
    spawn(Quran, :read, [pid, :page, x])

  end
  def sura(x) do
    sid = spawn(Mushaf, :read, [])
    spawn(Quran, :read, [sid,:sura, x])

  end
  def read(i, s, x) do
    send(i, {self(), s, x})
    receive do
      {:page, x} -> IO.puts(x)
      {:sura, x} -> IO.puts(x)

    end
  end
end
