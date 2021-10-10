from init import *

import csv
import random
import threading

class Q:
    def __init__(self):
        self.surat      = {}
        self.huruf      = {}
        self.juz        = {}
        self.halaman    = {}
        self.artiayat   = {}
        self.indexkata  = {}
        self.artikata   = {}
        self.codehuruf  = {}
        self.codekata   = {}
        self.tafsir     = {}
        self.kata       = self.data(DATA['kata'])

        self.loadTafsir(DATA['tafsir'])
        self.loadJuz(DATA['juz'])
        self.loadSurat(DATA['surat'])
        self.loadHalaman(DATA['halaman'])
        self.loadArtiAyat(DATA['artiayat'])
        self.loadArtiKata(DATA['artikata'])
        self.loadCode()

    def loadTafsir(self, db):
        dbContent = self.data(db)
        ns = 0
        for x in dbContent:
            s = int(x[0])
            a = int(x[1])

#           new tafsir
            if ns != s:
                ns = s
                ta = {}

            ta[a] = x[2]
            self.tafsir[s] = ta

    def loadCode(self):
        for x in self.kata[0:]:
            key = x[6]
            self.codekata[key] = x[6]


            for y in range(int(x[7])):
                pos = y + 8
                u = x[pos]
                self.huruf[u] = {'color': 'rgb('+str(random.randint(1,200))+','+str(random.randint(1,200))+','+ str(random.randint(1,200))+')'}

                try:
                    a = self.codehuruf[u]
                except Exception:
                    a = []

                a.append([x[0],x[1],x[2],x[3],x[4],x[5]])
                self.codehuruf[u] = a

    def loadSurat(self, db):
        dbContent = self.data(db)
        for x in dbContent:
            key = int(x[0])
            self.surat[key] = [x[1],x[3],x[4],x[5],x[6]]

    def loadJuz(self, db):
        dbContent = self.data(db)
        for x in dbContent:
            key = str(x[0])
            self.juz[key] = {'surat': x[1],'ayat': x[2]}

    def loadHalaman(self, db):
        dbContent = self.data(db)
        for x in dbContent:
            key = str(x[0])
            self.halaman[key] = {'surat': x[1], 'ayat': x[2]}

    def loadArtiAyat(self, db):
        dbContent = self.data(db)
        ns = 0
        for x in dbContent:
            s = int(x[0])
            a = int(x[1])
            if ns != s:
                ns = s
                ta = {}

            ta[a] = x[2]
            self.artiayat[s] = ta

    def loadArtiKata(self, db):
        dbContent = self.data(db)

        ns = 0
        na = 0
        for x in dbContent:
            # Index Kata
            u = x[4]

            try:
                a = self.indexkata[u]
            except Exception:
                a = []

            a.append([self.surat[int(x[0])][2],x[0],x[1],x[2]])
            self.indexkata[u] = a


            # Arti Kata
            s = int(x[0])
            a = int(x[1])
            k = int(x[3])

            if ns != s:
                ns = s
                ta = {}
                tk = {}

            if na != a:
                na = a
                tk = {}

            tk[k] = x[4]
            ta[a] = tk
            self.artikata[s] = ta

    def compare(self, a, b):
        if a != b:
            return True
        else:
            return False

    def spasi(self, u):
        self.mushafHuruf(u, '32')
        return u

    def kataBaru(self, u):
        warp = ''
        if u.props['mushaf'] == 1:
            warp = 'nowrap'

        u.render('</div>')
        if u.props['tafsir'] == 1:
            u.render('<div style="border-bottom: 1px solid '+u.props['backgroundcolor']+'; text-align: '+ u.props['align']+'; white-space: '+ warp +' ; width=100%; line-height: 0.5;">')

        if u.props['tafsir'] != 1:
            u.render('<div style="border-bottom: 1px solid #ddd; text-align: '+ u.props['align']+'; white-space: '+ warp +' ; width=100%; line-height: 0.5;">')

        return u

    def tambahBaris(self, u):
        warp = ''
        if u.props['mushaf'] == 1:
            warp = 'nowrap'

        u.render('</div>')
        if u.props['tafsir'] == 1:
            u.render('<div style="padding: 10px 0 0 0;width: 100%; border-bottom: 1px solid '+u.props['backgroundcolor']+'; text-align: '+ u.props['align']+'; white-space: '+ warp +' ; line-height: 1.2;">')

        if u.props['tafsir'] != 1 :
            u.render('<div class="m" style="width: 100%; border-bottom: 1px solid #ddd; text-align: '+ u.props['align']+'; white-space: '+ warp +' ; line-height: 1.2;">')

        return u

    def barisBaru(self, u):
        warp = ''
        if u.props['mushaf'] == 1:
            warp = 'nowrap'

        u.render('</div>')
        if u.props['tafsir'] == 1:
            u.render('<div style="padding: 10px 0 10px 0;width: 100%; border-bottom: 1px solid '+u.props['backgroundcolor']+'; text-align: '+ u.props['align']+'; white-space: '+ warp +' ; line-height: 1.2;">')

        if u.props['tafsir'] != 1 :
            u.render('<div class="m" style="width: 100%; border-bottom: 1px solid #eee; text-align: '+ u.props['align']+'; white-space: '+ warp +' ; line-height: 1.2;">')

        return u

    def artiBaru(self, u):
        warp = ''
        if u.props['mushaf'] == 1:
            warp = 'nowrap'

        u.render('</div>')
        if u.props['tafsir'] == 1:
            u.render('<div style="padding: 10px 0 10px 0; width: 100%; border-bottom: 1px solid #eee; text-align: left; white-space: '+ warp +' ; line-height: 1.2;">')

        if u.props['tafsir'] != 1:
            u.render('<div style="width: 100%; border-bottom: 1px solid '+u.props['backgroundcolor']+'; text-align: left; white-space: '+ warp +' ; line-height: 1.2;">')

        return u


    def artiAyat(self, u, surat, ayat):
        s = int(surat)
        a = int(ayat)
        result = ''
        try:
            result = self.artiayat[s][a]

        except KeyError:
            result = ''

        u.render('<a style="font-color: '+u.props['fontcolor']+'; font-size:' + TSIZET[u.props['fontsize']] + ';">')
        u.render('['+surat+':'+ayat+ '] '+result+ '</a>')
        return u

    def artiKata(self, u, surat, ayat, kata):
        s = int(surat)
        a = int(ayat)
        k = int(kata)

        result = ''
        try:
            result = self.artikata[s][a][k]

        except KeyError:
            result = ''

        u.render('<a style="font-color: '+u.props['fontcolor']+'; font-size:' + TSIZET[u.props['fontsize']] + ';">')
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
        rows = []
        file = open(db)
        dbContent = csv.reader(file)
        next(dbContent)

        for row in dbContent:
            rows.append(row)

        return rows

    def mushafKata(self, u, halaman, ayat, kata):
        if u.props['mushaf'] == 1:
            u.props['arabicfontsize'] = 0

        if len(halaman) == 1:
            font = 'QCF_P00' + halaman

        if len(halaman) == 2:
            font = 'QCF_P0' + halaman

        if len(halaman) == 3:
            font = 'QCF_P' + halaman

        if ayat == '0':
            font = 'QCF_BSML'

        u.render('<a style="font-size: '+ ASIZET[u.props['arabicfontsize']] + '; font-family: ' + font + ';color: '+ u.props['arabicfontcolor'] +';">')
        u.render(chr(int(kata)))
        u.render('</a>')
        return u

    def mushafHuruf(self, u, huruf):
        u.render('<a class="a" style="line-height: 1.5; text-align: '+ u.props['align']+';font-family: '+ FONTS[u.props['arabicfont']]+ ';font-size: '+ ASIZET[u.props['arabicfontsize']] + '; color: '+ u.props['arabicfontcolor'] +';">' +chr(int(huruf))+ '</a>')

        return u
