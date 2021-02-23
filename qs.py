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
        self.huruf      = self.data(DATA['huruf'])
        self.tafsir     = self.data(DATA['tafsir'])
        self.surat      = {}
        self.juz        = {}
        self.halaman    = {}
        self.artiayat   = {}
        self.artikata   = {}
        self.loadJuz(DATA['juz'])
        self.loadSurat(DATA['surat'])
        self.loadHalaman(DATA['halaman'])
        self.loadArtiAyat(DATA['artiayat'])
        self.loadArtiKata(DATA['artikata'])

    def loadSurat(self, db):
        file = open(db)
        dbContent = csv.reader(file)
        next(dbContent)

        for x in dbContent:
            key = str(x[0])
            self.surat[key] = {'ayat': x[1], 'bahasa': x[4], 'wahyu': x[6],}

    def loadJuz(self, db):
        file = open(db)
        dbContent = csv.reader(file)
        next(dbContent)

        for x in dbContent:
            key = str(x[0])
            self.juz[key] = {'surat': x[1], 'ayat': x[2],}

    def loadHalaman(self, db):
        file = open(db)
        dbContent = csv.reader(file)
        next(dbContent)

        for x in dbContent:
            key = str(x[0])
            self.halaman[key] = {'surat': x[1], 'ayat': x[2]}

    def loadArtiAyat(self, db):
        file = open(db)
        dbContent = csv.reader(file)
        next(dbContent)

        for x in dbContent:
            key = 'S' + str(x[0]) + 'A' + str(x[1])
            self.artiayat[key] = x[2]

    def loadArtiKata(self, db):
        file = open(db)
        dbContent = csv.reader(file)
        next(dbContent)

        for x in dbContent:
            key = 'S' + str(x[0]) + 'A' + str(x[1]) + 'K' + str(x[3])
            self.artikata[key] = x[4]

    def compare(self, a, b):
        if a != b:
            return True
        else:
            return False

    def spasiBaru(self, u):
        u.render(' ')
        return u

    def kataBaru(self, u):
        u.render(' ')
        return u

    def barisBaru(self, u):
        warp = ''
        if u.props['medina']:
            warp = 'nowrap'

        u.render('</td></tr>')

        if u.props['tafsir']:
            u.render('<tr><td style="border-bottom: 1px solid #fff; text-align: '+ u.props['align']+'; white-space: '+ warp +' ; width=100%; padding: 5px; line-height: 1.2;">')

        if not u.props['tafsir']:
            u.render('<tr><td style="border-bottom: 1px solid #ddd; text-align: '+ u.props['align']+'; white-space: '+ warp +' ; width=100%; padding: 5px; line-height: 1.2;">')

        return u

    def artiBaru(self, u):
        warp = ''
        if u.props['medina']:
            warp = 'nowrap'

        u.render('</td></tr>')
        if u.props['tafsir']:
            u.render('<tr><td style=" border-bottom: 1px solid #ddd; text-align: left; white-space: '+ warp +' ; width=100%; padding: 5px; line-height: 1.2;">')

        if not u.props['tafsir']:
            u.render('<tr><td style=" border-bottom: 1px solid #fff; text-align: left; white-space: '+ warp +' ; width=100%; padding: 5px; line-height: 1.2;">')

        return u


    def artiAyat(self, u, surat, ayat):
        key = 'S' + str(surat) + 'A' + str(ayat)
        try:
            result = self.artiayat[key]

        except KeyError:
            result = ''

        u.render('<a style="font-size:' + u.props['tafsirfontsize'] + ';">')
        u.render('[')
        u.render(surat)
        u.render(':')
        u.render(ayat)
        u.render('] ')
        u.render(result)
        u.render('</a>')
        return u

    def artiKata(self, u, surat, ayat, kata):
        key = 'S' + str(surat) + 'A' + str(ayat) + 'K' + str(kata)

        try:
            result = self.artikata[key]

        except KeyError:
            result = ''

        u.render('<a style="font-size:' + u.props['tafsirfontsize'] + ';">')
        u.render(result)
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
