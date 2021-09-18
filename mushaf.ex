defmodule Mushaf do
  def load do
    File.read('data/mushaf.db')

  end
  def read do
    receive do
      {cid, :page, x} -> send(cid, {:page, x})
      {:juz, x} -> x
      {:sura, x} -> x
      {:ayah, x} -> x
    end

  end
end
