require 'init.rb'

class Uo
    def initialize
        @stage = {}
        @component = []
        @artikata = []
        @props = {
                'mode'              : 0,        #0: Pages, 1:Row 2: Juz, 3: Sura, 4: Ayat
                'view'              : 0,        #0: Show All, 1: Hide All, 2, firstword
                'color'             : True,
                'backgroundcolor'   : '',
                'arabic'            : True,
                'tafsir'            : 1,
                'translation'       : True,
                'word'              : 1,
                'tajweed'           : False,
                'random'            : False,
                'print'             : 0,        # True: Mushaf Madina, False: Mushaf Usmani
                'mushaf'            : 0,
                'perayat'           : 0,
                'firstword'         : 1,
                'firstwordcolor'    : '',
                'align'             : 'right',
                'arabicfont'        : 'Scheherazade',
                'arabicfontcolor'   : '',
                'arabicfontsize'    : 1,
                'font'              : 'Harmattan',
                'fontcolor'         : '',
                'fontsize'          : 0,
                'index'             : '1',
                'page'              : 1,
                'row'               : 1,
                'juz'               : 1,
                'surat'             : 1,
                'ayat'              : 1,
                'kata'              : 1,
                'title'             : 'Al Quran',
                'theme'             : 0,
                'menu'              : 0,
                'selected'          : '',
                'search'            : 0,
                'text'              : 0,
                'highlight'         : {},
                'match'             : 0,
                'hubo'              : 0,
            }

    def render text
        @component.append(text)
    end

    def style xobj, xstyle
        sty = "<style> #{xobj} {"
        for x in xstyle do
            sty = sty + x +': '+xstyle[x]+';'
        end
        sty = sty + '}</style>'
        render sty
    end

    def p xobj
        render '<p>'+xobj+'</p>'
    end

    def header xobj
        render '<header>'+xobj+'</header>'
    end

    def div xobj
        render '<div>'+xobj+'</div>'
    end

    def line xobj
        render '<line>'+xobj+'</line>'
    end
 
    def svg xobj
        render '<svg>'+xobj+'</svg>'
    end

    def highlight xobj
        xstyle = { 'color': '#000000'}
        self.style(xobj, xstyle)

        xstyle = { 'color': '#0000ff' }
        self.style(xobj + ':hover', xstyle)
    end

