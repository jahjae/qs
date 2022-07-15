


type 
  Ui* = object

proc init*(u: var Ui) =
        u.stage = {}
        u.component = []
        u.artikata = []
        uf.props = {
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

proc render*(u: var Ui, text: string):
        u.component.append(text)

proc style(u: var Ui, xobj: string, xstyle):
        sty = "<style>",xobj," {"
        for x in xstyle:
            sty = sty + x +': '+xstyle[x]+';'

        sty = sty + '}</style>'
        u.render(sty)

proc p*(u: var Ui, xobj: string):
        sty = '<p>'+xobj+'</p>'
        u.render(sty)

proc header*(self, xobj):
        sty = '<header>'+xobj+'</header>'
        u.render sty

proc div*(self, xobj):
        sty = '<div>'+xobj+'</div>'
        self.render(sty)

proc line*(u: var Ui, xobj: string):
        sty = '<line>'+xobj+'</line>'
        u.render(sty)`

proc highlight*(self, xobj):
        xstyle = { 'color': '#000000'}
        u.style(xobj, xstyle)

        xstyle = { 'color': '#0000ff' }
        u.style(xobj + ':hover', xstyle)
