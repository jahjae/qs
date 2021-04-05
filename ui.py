
import os
import init

class C:
    def __init__(self):
        self.component = []
        self.artikata = []
        self.props = {
                'mode'              : 0,        #0: Pages, 1:Row 2: Juz, 3: Sura, 4: Ayat
                'view'              : 0,        #0: Show All, 1: Hide All, 2, firstword
                'çolor'             : True,
                'backgroundcolor'   : '',
                'arabic'            : True,
                'tafsir'            : 1,
                'translation'       : True,
                'word'              : 1,
                'tajweed'           : False,
                'random'            : False,
                'print'             : 0,        # True: Mushaf Madina, False: Mushaf Usmani
                'mushaf'            : 0,
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
            }

    def render(self, text):
        self.component.append(text)

    def style(self, xobj, xstype):
        sty = '<style>'+xobj+'{'
        for x in xstype:
            sty = sty + x +': '+xstype[x]+';'

        sty = sty + '}</style>'
        self.render(sty)

    def fonts(self):
        sty = '<style> @font-face { font-family: QCF_BSML; src: url(/data/fonts/QCF_BSML.TTF)  format("truetype");} '
        for x in range(605):
            a = str(1000 + x)
            n = 'QCF_P' + a[1:4]
            sty = sty + '@font-face { font-family: '+n+'; '
            sty = sty + 'src: url(/data/fonts/'+n+'.ttf) format("truetype"); } '

        sty = sty + ' </style>'
        self.render(sty)
