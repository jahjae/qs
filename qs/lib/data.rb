require_relative 'init.rb'

class Quran
  attr_accessor :code, :page, :juz, :surah, :huruf
 
  def initialize
    @code = getData DB[:mushaf]

    @page = {}
    @juz = {}      
    @surah = {}
    @huruf = {}

    loadSurah
    loadPage
    loadJuz
  end

  def loadPage
    @code.each do | p |
      p = p[0].to_i
      r = p[1].to_i
      s = p[3].to_i
      
      a = p[4].to_i
      k = p[5].to_i

      l = p[7].to_i + 7

      begin
        @page[p][r][k] = @surah[s][a][k]
      rescue
        begin
          @page[p][r] = {}
          @page[p][r][k] = @surah[s][a][k]
        rescue
            @page[p] = {}
            @page[p][r] = {}
            @page[p][r][k] = @surah[s][a][k]
        end
      end
    end
  end

  def loadJuz
    @code.each do | j |
      j = j[2].to_i
      s = j[3].to_i

      a = j[4].to_i

      begin
        @juz[j][s][a] = @surah[s][a]
      rescue
        begin
          @juz[j][s] = {}
          @juz[j][s][a] = @surah[s][a]
        rescue
          @juz[j] = {}
          @juz[j][s] = {}
          @juz[j][s][a] = @surah[s][a]
        end
      end

    end
  end

  def loadSurah
    @code.each do | s |
      s = s[3].to_i
      a = s[4].to_i

      k = s[5].to_i
      l = s[7].to_i + 7

      kata = s[8..l]

      begin 
        @surah[s][a][k] = kata
      rescue
        begin
          @surah[s][a] = {}
          @surah[s][a][k] = kata
        rescue
          @surah[s] ={}
          @surah[s][a] = {}
          @surah[s][a][k] = kata
        end
      end
    end
  end

  def getData db
    rows = []
    file = File.open db

    dbContent = file.readlines
    file.close
  
    dbContent.each do |row|
      rows.append row.split ","
    end
    return rows
  end
end
