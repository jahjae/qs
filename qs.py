#
#   Designed by Ismail Umar
#   Quran Class
#

from init import *
import csv

class Ui:
    def __init__(self):
        self.Kata       = self.bacaData(QURANDATA['MU'])
        self.Terjemahan = self.bacaData(QURANDATA['TR'])
        self.Juz        = self.bacaData(QURANDATA['JU'])
        self.Halaman    = self.bacaData(QURANDATA['PA'])
        self.Huruf      = self.bacaData(QURANDATA['DB'])
        self.Tafsir     = self.bacaData(QURANDATA['TA'])
        self.Warna      = COLOR['BLACK']


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
        array.append(a)
        for x in juz:
            array.append('<a>'+ x[0]+ '</a>')

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

    def barisBaru(self, Kata, size, align, line):
        Kata.append('</td></tr>')
        Kata.append('<tr><td style="text-align: '+ align +'; padding: 5px; font-size: '+ size +'; line-height: '+ line +';">')
        return Kata

    def artiAyat(self, array, Artinya, surat, ayat):
        for arti in Artinya:
            if arti[0] == surat:
                if arti[1] == ayat:
                    array.append('<a>')
                    array.append('[')
                    array.append(surat)
                    array.append(':')
                    array.append(ayat)
                    array.append('] ')
                    array.append(arti[2])
                    array.append('</a>')
                    return array


    def periksaHuruf(self, qBase, a, b, c, d):
        for x in qBase:
            if x[0] == a:
                if x[1] == b:
                    if x[2] == c:
                        if x[3] == d:
                            return x[4]

    def bacaData(self, db):
        file = open(db)
        dbContent = csv.reader(file)
        next(dbContent)
        return dbContent


    def mushafKata(self, array, huruf, surat, ayat, halaman):

        if len(halaman) == 1:
            font = 'QCF_P00' + halaman

        if len(halaman) == 2:
            font = 'QCF_P0' + halaman

        if len(halaman) == 3:
            font = 'QCF_P' + halaman

        if ayat == '0':
            font = 'QCF_BSML'

        array.append('<a style="font-family: ' + font + '; color: ' + self.Warna + ';">')
        array.append(chr(int(huruf)))
        array.append('</a>')
        return array


    def mushafHuruf(self, array, huruf):
        array.append('<a style="font-family: Scheherazade;">')
        array.append(chr(int(huruf)))
        array.append('</a>')
        return array

    def nomorSurat(self, Kata, listSurat, index):
        namaSurat = ''
        for surat in listSurat:
            if surat[0] == index:
                namaSurat = surat[2]

        Kata.append(namaSurat)
        return Kata

    def nomorAyat(self, Kata, Ayat):
        num = ''
        for x in Ayat:
            num = num + chr(int(PAGES[int(x)]))

        Kata.append('<a style="font-family: Scheherazade, serif;">')
        Kata.append(' ' + chr(1757) + num)
        Kata.append('</a>')
        return Kata
