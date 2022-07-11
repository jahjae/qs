require_relative 'init.rb'

class Quran
  attr_accessor :halaman, :juz, :surat, :kata, :huruf, :codehuruf, :artiayat, :artikata, :indexkata, :codekata, :tafsir
 
  def initialize
        @surat      = {}
        @huruf      = {}
        @juz        = {}
        @halaman    = {}
        @artiayat   = {}
        @indexkata  = {}
        @artikata   = {}
        @codehuruf  = {}
        @codekata   = {}
        @tafsir     = {}
        @kata       = data DATA[:kata]

        
        loadTafsir DATA[:tafsir]
        loadJuz DATA[:juz]
        loadSurat DATA[:surat]
        loadHalaman DATA[:halaman]
        loadArtiAyat DATA[:artiayat]
        loadArtiKata DATA[:artikata]
        loadCode
    end

    def loadTafsir db
        dbContent = data db
        ns = 0
        ta = {}
        dbContent.each do |x|
          s = x[0].to_i
          a = x[1].to_i
          
          if ns != s
            ns = s
            ta = {}
          end
          ta[a] = x[2]
          @tafsir[s] = ta
        end
    end

    def loadCode

      a = Array.new
      @kata.each do |x|
            key = x[6]
            @codekata[key] = x[6]
            l = x[7].to_i

            l.times do |y|
                pos = y + 8
                u = x[pos]
                @huruf[u] = {'color': "rgb(#{rand 200},#{rand 200}, #{rand 200})"}

                begin
                    a = @codehuruf[u]
                rescue
                  a = Array.new
                end
                a = [x[0],x[1],x[2],x[3],x[4],x[5]]
                @codehuruf[u] = a
            end
        end
    end

    def loadSurat db
        dbContent = data db
        @surat = Hash.new
        dbContent.each do |x|
          key = x[0].to_i
          @surat[key] = [x[1],x[3],x[4],x[5],x[6]]
        end
    end

    def loadJuz db
        dbContent = data db
        @juz = {} 
        dbContent.each do |x|
            @juz[x[0].to_s] = {surat: x[1], ayat: x[2]}
        end
    end

    def loadHalaman db
        dbContent = data db
        dbContent.each do |x|
            @halaman[x[0].to_s] = {surat: x[1], ayat: x[2]}
        end
    end

    def loadArtiAyat db
        dbContent = data db
        ns = 0
        ta = {}        
        dbContent.each do |x|
          s = x[0].to_i
          a = x[1].to_i
            if ns != s
                ns = s
                ta = {}
            end
            ta[a] = x[2]
            @artiayat[s] = ta
        end

    end

    def loadArtiKata db
        dbContent = data db

        a = []
        
        ns = 0
        na = 0

        ta = {}
        tk = {}

        dbContent.each do |x|
            # Index Kata
            u = x[4]

            begin
              a = @indexkata[u].to_a
            rescue
              a = []
            end
  
            a = [@surat[x[0][2]],x[0],x[1],x[2]]
            @indexkata[u] = a

            # Arti Kata
            s = x[0].to_i
            a = x[1].to_i
            k = x[3].to_i

            if ns != s
                ns = s
                ta = {}
                tk = {}
            end

            if na != a
                na = a
                tk = {}
            end
        
            tk[k] = x[4]
            ta[a] = tk
            @artikata[s] = ta
        end
    end

    def compare a, b
        return a != b
    end

    def spasi u
        mushafHuruf u, '32'
        return u
    end

    def kataBaru u
        warp = ''
        if u.props[:mushaf]
            warp = 'nowrap'
        end
        
        u.render('</div>')
        if u.props[:tafsir]
            u.render('<div style="border-bottom: 1px solid '+u.props[:backgroundcolor]+'; text-align: '+ u.props[:align]+'; white-space: '+ warp +' ; width=100%; line-height: 1.6;">')
        else
            u.render('<div style="border-bottom: 1px solid #ddd; text-align: '+ u.props['align']+'; white-space: '+ warp +' ; width=100%; line-height: 1.6;">')
        end
        return u
    end

    def tambahBaris u
        warp = ''
        if u.props[:mushaf]
            warp = 'nowrap'
        end
        
        u.render('</div>')
        if u.props[:tafsir]
            u.render('<div style="padding: 10px 0 0 0;width: 100%; border-bottom: 1px solid '+u.props[:backgroundcolor]+'; text-align: '+ u.props[:align]+'; white-space: '+ warp +' ; line-height: 1.6;">')

        else
            u.render('<div class="m" style="width: 100%; border-bottom: 1px solid #ddd; text-align: '+ u.props['align']+'; white-space: '+ warp +' ; line-height: 1.6;">')
        end
        return u
    end

    def barisBaru u
        warp = ''
        if u.props[:mushaf]
            warp = 'nowrap'
        end
        
        u.render('</div>')
        if u.props[:tafsir]
            u.render('<div style="padding: 10px 0 10px 0; width: 100%; border-bottom: 1px solid '+u.props[:backgroundcolor]+'; text-align: '+ u.props[:align]+'; white-space: '+ warp +' ; line-height: 2;">')
        else
            u.render('<div class="m" style="padding: 10px 0 10px 0; width: 100%; border-bottom: 1px solid #eee; text-align: '+ u.props[:align]+'; white-space: '+ warp +'line-height: 2;">')
        end
        return u
    end

    def artiBaru u
      warp = ''
      if u.props[:mushaf]
        warp = 'nowrap'
      end
      
      u.render('</div>')
      if u.props[:tafsir]
        u.render "<div style='padding: 10px 0 10px 0; width: 100%; border-bottom: 1px solid #eee; text-align: left; white-space: #{warp}; line-height: 1.6;'>"
      else
        u.render "<div style='width: 100%; border-bottom: 1px solid #{u.props['backgroundcolor']}; text-align: left; white-space: #{warp}; line-height: 1.6;'>"
      end
      return u
    end

    def artiAyat u, surat, ayat
        s = int(surat)
        a = int(ayat)
        result = ''
    
        begin
            result = @artiayat[s][a]
    
        rescue
            result = ''
        end

        u.render('<a style="font-color: '+u.props['fontcolor']+'; font-size:' + TSIZET[u.props['fontsize']] + ';">')
        u.render('['+surat+':'+ayat+ '] '+result+ '</a>')
        return u
    end

    def artiKata u, surat, ayat, kata
        s = int(surat)
        a = int(ayat)
        k = int(kata)

        result = ''
        begin
            result = @artikata[s][a][k]

        rescue
            result = ''
        end
        u.render "<a style='font-color: #{u.props['fontcolor']}; font-size: #{TSIZET[u.props['fontsize']]};'>"
        u.render result
        u.render "</a>"

        return u
    end

    def periksaHuruf qBase, a, b, c, d
      qBase.each do |x|
            if x[0] == a
                if x[1] == b
                    if x[2] == c
                        if x[3] == d
                            return x[4]
                        end
                    end
                end
            end
        end
    end

    def data db
        rows = []
        file = File.open db, 'r'
        dbContent = file.readlines
      
        dbContent.each do |row|
          rows.append row.split ","
        end
        return rows
    end

    def mushafKata u, halaman, ayat, kata
    
      if u.props[:mushaf]
            u.props[:arabicfontsize] = 0
        end

      if halaman.lenght == 1
            font = 'QCF_P00' + halaman
        end
        if halaman.lenght == 2
            font = 'QCF_P0' + halaman
        end
        if halaman.lenght == 3
            font = 'QCF_P' + halaman
        end
        if ayat == '0'
            font = 'QCF_BSML'
        end

        u.render "<a style='font-size: #{ASIZET[u.props[:arabicfontsize]]} ; font-family: #{font} ;color: #{u.props[:arabicfontcolor]} ;'>"
        u.render kata.chr
        u.render "</a>"
        return u
    end

    def mushafHuruf u, huruf
      x = []

      x[0] = huruf.to_i
      s = x.pack 'U*'
  
      u.render "#{s}"
      return u
    end
end
