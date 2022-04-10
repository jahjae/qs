
import os
import init            

class C:
    def __init__(self):
        self.stage = {}
        self.component = []
        self.artikata = []
        self.props = {
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

    def render(self, text):
        self.component.append(text)

    def style(self, xobj, xstyle):
        sty = '<style>'+xobj+' {'
        for x in xstyle:
            sty = sty + x +': '+xstyle[x]+';'

        sty = sty + '}</style>'
        self.render(sty)

    def p(self, xobj):
        sty = '<p>'+xobj+'</p>'
        self.render(sty)

    def header(self, xobj):
        sty = '<header>'+xobj+'</header>'
        self.render(sty)

    def div(self, xobj):
        sty = '<div>'+xobj+'</div>'
        self.render(sty)

    def line(self, xobj):
        sty = '<line>'+xobj+'</line>'
        self.render(sty)
 
    def svg(self, x, y, xobj):
        sty = '<svg>'+xobj+'</svg>'
        self.render(sty)

    def highlight(self, xobj):
        xstyle = { 'color': '#000000'}
        self.style(xobj, xstyle)

        xstyle = { 'color': '#0000ff' }
        self.style(xobj + ':hover', xstyle)
