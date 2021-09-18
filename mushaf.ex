defmodule Mushaf do
  def read do
    receive do
      {cid, :page, x} -> send(cid, {:page, x})
      {cid, :sura, x} -> send(cid, {:sura, x})
    end

  end
end
