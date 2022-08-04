class Mushaf
  def page q, u
    row = {}
    row = q.page[604]
    row.each do |x, v|
      u.p v
    end
  end

  def daily 
    ayat = {}
    ayat = q.surat[1][1]
    ayat.each do |k,v|
      u.p v
    end
  end

  def surah q, u
    ayat = {}
    ayat = q.surah[114]
    ayat.each do |x, v|
      u.p "QS 114:#{x}"
      u.p v
    end
  end

  def juz q, u
    surah = {}
    surah = q.juz[30]
    surah.each do |x|
      u.p x
    end
  end
end

