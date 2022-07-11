require_relative 'init.rb'

class Ui
  attr_accessor :props, :component
  def initialize
        @stage = {}
        @component = []
        @artikata = []
        @props = {
                mode: 0,        #0: Pages, 1:Row 2: Juz, 3: Sura, 4: Ayat
                view: 0,        #0: Show All, 1: Hide All, 2, firstword
                color: TRUE,
                backgroundcolor: '',
                arabic: TRUE,
                tafsir: 1,
                translation: TRUE,
                word: 1,
                tajweed: FALSE,
                random: FALSE,
                print: 0,        # TRUE: Mushaf Madina, FALSE: Mushaf Usmani
                mushaf: 0,
                perayat: 0,
                firstword: 1,
                firstwordcolor: '',
                align: 'right',
                arabicfont: 'Scheherazade',
                arabicfontcolor: '',
                arabicfontsize: 1,
                font: 'Harmattan',
                fontcolor: '',
                fontsize: 0,
                index: '1',
                page: 1,
                row: 1,
                juz: 1,
                surat: 1,
                ayat: 1,
                kata: 1,
                title: 'Al Quran',
                theme: 0,
                menu: 0,
                selected: 0,
                search: 0,
                text: 0,
                highlight: {},
                match: 0,
                hubo: 0 }
    end

    def props= x
      @props = x
    end

    def render text
        @component.append text 
    end

    def style xobj, xstyle
        sty = "<style> #{xobj} {"
        
        xstyle.each do |k, v|
            sty = sty + " #{k}: #{v};"
        end
        
        sty = sty + "}</style>"
        render sty
    end

    def p xobj
        render "<p>#{xobj}</p>"
    end

    def header xobj
        render "<header>#{xobj}</header>"
    end

    def div xobj
        render "<div>#{xobj}</div>"
    end

    def line xobj
        render "<line>#{xobj}</line>"
    end
 
    def svg xobj
        render "<svg>#{xobj}</svg>"
    end

    def highlight xobj
        xstyle = { 'color': '#000000'}
        self.style xobj, xstyle

        xstyle = { 'color': '#0000ff' }
        style xobj + ':hover', xstyle
    end
end
