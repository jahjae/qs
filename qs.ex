defmodule Quran do
  def page(x) do
    sid = spawn(Mushaf, read, {})
    spawn(Quran, read, {sid})

  end
  def read(sid) do
    send(sid, {self(), :page, x})
    receive do
      {:page, x} -> x

    end
  end
end
