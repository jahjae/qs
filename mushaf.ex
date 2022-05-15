defmodule Mushaf do
  def quran() do
    receive do
      {:surat, cid, args1} ->
        send cid, {:surat, args1}
      {:ayat, cid, args1, args2} ->
        send cid, {:ayat, args1, args2}
    end
  end

  def quranAyat() do

  end

  def quranKata() do

  end

  def quranHuruf() do

  end

  def daily() do

  end

  def index() do

  end

  def goto() do

  end

  def search() do
  end

  def info() do

  end

  def menu() do

  end

  def mode() do

  end

  def mode() do

  end

  def theme() do

  end

  def fontsize() do

  end

  def fontname() do

  end

  def arabic() do

  end

  def pertama() do

  end

  def view() do

  end

  def quran() do

  end

  def translation() do

  end

  def word() do

  end

  def mushaf() do

  end
end
