from PIL import ImageDraw
from PIL import ImageFont
from PIL import Image

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
                'title'             : 'AL QURAN',
                'theme'             : 0,
                'menu'              : 0,\
                'selected'          : '',
                'search'            : 0,
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
        sty = '@font-face { font-family: "QCF_BSML"; src: url("./data/fonts/QCF_BSML.TTF"); '
        for x in range(604):
            a = str(1000 + x)
            n = 'QCF_P' + a[1:2]
            sty = sty + 'font-family: "QCF_P'+n+'"; '
            sty = sty + 'src: url("./data/fonts/'+n+'.ttf"); '

        sty = sty + '}'
        self.render(sty)

    def imagePage(self):
        self.image = Image.new('RGB', (480, 640), (256,255,255))
        self.content = ImageDraw.Draw(self.image)

    def fillPage(self, x, xtext):
        unicode_font = ImageFont.truetype("arial.ttf", 10, encoding="unic")
        self.content.text((200 * x, 200 * x), xtext, font=unicode_font, fill=(0,0,0))
