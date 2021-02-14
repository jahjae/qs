#
#   Designed by Ir. H. Ismail Umar
#   Quran Class
#

from init import *
from ui import *
import csv

class Q:
    def __init__(self):
        self.kata       = self.data(DATA['kata'])
        self.artiayat   = self.data(DATA['artiayat'])
        self.juz        = self.data(DATA['juz'])
        self.halaman    = self.data(DATA['halaman'])
        self.huruf      = self.data(DATA['huruf'])
        self.tafsir     = self.data(DATA['tafsir'])
        self.artikata    = self.data(DATA['artikata'])
        self.warna      = COLOR['BLACK']
        self.size       = '100%'
        self.space      = '1.2'


    def juz(self, array, juz):
        a = '''
        <style>
        .pagination {
          display: inline-block;
        }

        .pagination a {
          color: black;
          float: left;
          padding: 8px 16px;
          text-decoration: none;
          transition: background-color .3s;
        }

        .pagination a.active {
          background-color: #4CAF50;
          color: white;
        }

        .pagination a:hover:not(.active) {background-color: #ddd;}
        </style>
        <div class="pagination" style="position: fixed ;right: 0px; left: 0px; bottom: 0px; height: 75px; background-color: #fff; opacity: 1">
        '''
        array.render(a)
        for x in juz:
            array.render('<a>'+ x[0]+ '</a>')

        array.append('</div>')
        return array

    def page(self):
        return '''
        <div class="sura" style="position: fixed ;right: 0px; left: 0px; bottom: 0px; height: 50px; background-color: #fff; opacity: 1">
        </div>'''

    def compare(self, a, b):
        if a != b:
            return True
        else:
            return False

    def spasiBaru(self, u):
        u.render(' ')
        return u

    def barisBaru(self, u):
        warp = ''
        if u.props['mushaf']:
            warp = 'nowrap'

        u.render('</td></tr>')
        u.render('<tr><td style="border-bottom: 1px solid #eee; text-align: '+ u.props['align']+'; white-space: '+ warp +' ; width=100%; padding: 5px; line-height: '+ self.space +';">')
        return u

    def artiAyat(self, u, surat, ayat):
        for arti in self.arti:
            if arti[0] == surat:
                if arti[1] == ayat:
                    u.render('<a style="font-size: '+ u.props['tafsirfontsize'] + ';>')
                    u.render('[')
                    u.render(surat)
                    u.render(':')
                    u.render(ayat)
                    u.render('] ')
                    u.render(arti[2])
                    u.render('</a>')
                    return u


    def periksaHuruf(self, qBase, a, b, c, d):
        for x in qBase:
            if x[0] == a:
                if x[1] == b:
                    if x[2] == c:
                        if x[3] == d:
                            return x[4]

    def data(self, db):
        file = open(db)
        dbContent = csv.reader(file)
        next(dbContent)
        return dbContent


    def mushafKata(self, array, halaman, ayat, kata):

        if len(halaman) == 1:
            font = 'QCF_P00' + halaman

        if len(halaman) == 2:
            font = 'QCF_P0' + halaman

        if len(halaman) == 3:
            font = 'QCF_P' + halaman

        if ayat == '0':
            font = 'QCF_BSML'

        array.render('<a style="font-family: ' + font + ';">')
        array.render(chr(int(kata)))
        array.render('</a>')
        return array


    def mushafHuruf(self, u, huruf):
        u.render('<a style="text-align: '+ u.props['align']+';font-size: '+ u.props['arabicfontsize'] + ';color: '+ u.props['arabicfontcolor'] +';">' + chr(int(huruf)) + '</a>')
        return u

    def nomorSurat(self, array, listSurat, index):
        namaSurat = ''
        for surat in listSurat:
            if surat[0] == index:
                namaSurat = surat[2]

        array.render(namaSurat)
        return array

    def nomorAyat(self, array, Ayat):
        num = ''
        for x in Ayat:
            num = num + chr(int(PAGES[int(x)]))

        array.render('<a style="font-family: Scheherazade;">')
        array.render(' ' + chr(1757) + num)
        array.render('</a>')
        return array
