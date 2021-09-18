defmodule Quran do
  def page(x) do
    pid = spawn(Mushaf, :read, [])
    spawn(Quran, :read, [pid, :halaman, x])

  end
  def sura(x) do
    sid = spawn(Mushaf, :read, [])
    spawn(Quran, :read, [sid,:surat, x])

  end
  def read(i, s, x) do
    send(i, {self(), s, x})
    receive do
      {:halaman, x} -> IO.puts(x)
      {:juz, x} -> IO.puts(x)
      {:surat, x} -> IO.puts(x)
      {:ayat, x} -> IO.puts(x)
    end
  end
end
