import os

class C:
    def __init__(self):
        self.component = []
        self.artikata = []
        self.props = {
                'mode'              : 0,        #0: Pages, 1:Row 2: Juz, 3: Sura, 4: Ayat
                'view'              : 0,        #0: Show All, 1: Hide All, 2, firstword
                'çolor'             : True,
                'backgroundcolor'   : '#fffffff',
                'arabic'            : True,
                'tafsir'            : 1,
                'translation'       : True,
                'word'              : 1,
                'tajweed'           : False,
                'random'            : False,
                'print'             : 0, # True: Mushaf Madina, False: Mushaf Usmani
                'mushaf'            : 0,
                'firstword'         : 1,
                'firstwordcolor'    : '#ff0000',
                'align'             : 'right',
                'arabicfont'        : 'Scheherazade',
                'arabicfontcolor'   : '#000000',
                'arabicfontsize'    : '50px',
                'font'              : 'Harmattan',
                'fontcolor'         : '#000000',
                'fontsize'          : '20px',
                'index'             : '1',
                'page'              : 1,
                'row'               : 1,
                'juz'               : 1,
                'surat'             : 1,
                'ayat'              : 1,
                'kata'              : 1,
                'title'             : 'QURAN',
                'thema'             : 0,
            }

    def render(self, text):
        self.component.append(text)

    def rect(self):
        pass

    def circle(self):
        pass

    def ellipse(self):
        pass

    def line(self):
        pass

    def polygon(self):
        pass

    def polyline(self):
        pass

    def path(self):
        pass

    def text(self):
        pass

    def stroge(self):
        pass
