from init import *
from apps import *

import csv
import random
import threading
import logging

format = "%(asctime)s: %(message)s"
logging.basicConfig(format=format, level=logging.INFO,datefmt="%H:%M:%S")


type
  Quran = object


proc initz*(q: var Qurans):
        q.surat      = {}
        q.huruf      = {}
        q.juz        = {}
        q.halaman    = {}
        q.artiayat   = {}
        q.indexkata  = {}
        q.artikata   = {}
        q.codehuruf  = {}
        q.codekata   = {}
        q.tafsir     = {}
        q.kata       = self.data(DATA['kata'])

        
        self.loadTafsir(DATA['tafsir'])
        self.loadJuz(DATA['juz'])
        self.loadSurat(DATA['surat'])
        self.loadHalaman(DATA['halaman'])
        self.loadArtiAyat(DATA['artiayat'])
        self.loadArtiKata(DATA['artikata'])
        self.loadCode()

proc loadTafsir*(q: var Quran, db: string):
        dbContent = q.data(db)
        ns = 0
        for x in dbContent:
            s = int(x[0])
            a = int(x[1])

            if ns != s:
                ns = s
                ta = {}

            ta[a] = x[2]
            q.tafsir[s] = ta

proc loadCode*(q: var Quran):
        for x in q.kata[0:]:
            key = x[6]
            q.codekata[key] = x[6]

            for y in range(int(x[7])):
                pos = y + 8
                u = x[pos]
                q.huruf[u] = {'color': 'rgb('+str(random.randint(1,200))+','+str(random.randint(1,200))+','+ str(random.randint(1,200))+')'}

                try:
                    a = q.codehuruf[u]
                except Exception:
                    a = []

                a.add([x[0],x[1],x[2],x[3],x[4],x[5]])
                q.codehuruf[u] = a

    proc loadSurat(self, db):
        logging.info("Surat ...")

        dbContent = self.data(db)
        for x in dbContent:
            key = int(x[0])
            self.surat[key] = [x[1],x[3],x[4],x[5],x[6]]

    proc loadJuz(self, db):
        logging.info("Juz ...")

        dbContent = self.data(db)
        for x in dbContent:
            key = str(x[0])
            self.juz[key] = {'surat': x[1],'ayat': x[2]}

    proc loadHalaman(self, db):
        logging.info("Halaman ...")

        dbContent = self.data(db)
        for x in dbContent:
            key = str(x[0])
            self.halaman[key] = {'surat': x[1], 'ayat': x[2]}

    proc loadArtiAyat(self, db):
        logging.info("Arti ayat ...")

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

    proc loadArtiKata(self, db):
        logging.info("Arti Kata ...")

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

            a.add([self.surat[int(x[0])][2],x[0],x[1],x[2]])
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

    proc compare(self, a, b):
        if a != b:
            return True
        else:
            return False

    proc spasi(self, u):
        self.mushafHuruf(u, '32')
        return u

    proc kataBaru(self, u):
        warp = ''
        if u.props['mushaf'] == 1:
            warp = 'nowrap'

        u.render('</div>')
        if u.props['tafsir'] == 1:
            u.render('<div style="border-bottom: 1px solid '+u.props['backgroundcolor']+'; text-align: '+ u.props['align']+'; white-space: '+ warp +' ; width=100%; line-height: 1.6;">')

        if u.props['tafsir'] != 1:
            u.render('<div style="border-bottom: 1px solid #ddd; text-align: '+ u.props['align']+'; white-space: '+ warp +' ; width=100%; line-height: 1.6;">')

        return u

    proc tambahBaris(self, u):
        warp = ''
        if u.props['mushaf'] == 1:
            warp = 'nowrap'

        u.render('</div>')
        if u.props['tafsir'] == 1:
            u.render('<div style="padding: 10px 0 0 0;width: 100%; border-bottom: 1px solid '+u.props['backgroundcolor']+'; text-align: '+ u.props['align']+'; white-space: '+ warp +' ; line-height: 1.6;">')

        if u.props['tafsir'] != 1 :
            u.render('<div class="m" style="width: 100%; border-bottom: 1px solid #ddd; text-align: '+ u.props['align']+'; white-space: '+ warp +' ; line-height: 1.6;">')

        return u

    proc barisBaru(self, u):
        warp = ''
        if u.props['mushaf'] == 1:
            warp = 'nowrap'

        u.render('</div>')
        if u.props['tafsir'] == 1:
            u.render('<div style="padding: 10px 0 10px 0; width: 100%; border-bottom: 1px solid '+u.props['backgroundcolor']+'; text-align: '+ u.props['align']+'; white-space: '+ warp +' ; line-height: 2;">')

        if u.props['tafsir'] != 1 :
            u.render('<div class="m" style="padding: 10px 0 10px 0; width: 100%; border-bottom: 1px solid #eee; text-align: '+ u.props['align']+'; white-space: '+ warp +'line-height: 2;">')

        return u

    proc artiBaru(self, u):
        warp = ''
        if u.props['mushaf'] == 1:
            warp = 'nowrap'

        u.render('</div>')
        if u.props['tafsir'] == 1:
            u.render('<div style="padding: 10px 0 10px 0; width: 100%; border-bottom: 1px solid #eee; text-align: left; white-space: '+ warp +' ; line-height: 1.6;">')

        if u.props['tafsir'] != 1:
            u.render('<div style="width: 100%; border-bottom: 1px solid '+u.props['backgroundcolor']+'; text-align: left; white-space: '+ warp +' ; line-height: 1.6;">')

        return u

proc artiAyat(u: var Ui, surat, ayat): seq[int]
        let s = surat
        let a = ayat
        let result = ''

        try:
            result = self.artiayat[s][a]

        except KeyError:
            result = ''

        u.render('<a style="font-color: '+u.props['fontcolor']+'; font-size:' + TSIZET[u.props['fontsize']] + ';">')
        u.render('['+surat+':'+ayat+ '] '+result+ '</a>')
        return u

proc artiKata(u: seq[int], surat, ayat, kata: int): seq[int] =
        s = surat
        a = ayat
        k = kata

        result = ''
        try:
            result = self.artikata[s][a][k]

        except KeyError:
            result = ''

        u.render('<a style="font-color: '+u.props['fontcolor']+'; font-size:' + TSIZET[u.props['fontsize']] + ';">')
        u.render(result)
        u.render('</a>')

        return u

proc periksaHuruf(q: var Quran, a, b, c, d): int =
        for x in qBase:
            if x[0] = a:
                if x[1] = b:
                    if x[2] = c:
                        if x[3] == d:
                            return x[4]

proc data(db: string) seq[]:
  let rows = []
  
  dbContent = readfile(db)

  for row in dbContent:
    rows.add(row)

    return rows

proc mushafKata(u: var Ui, halaman, ayat, kata: int): object =
        if u.props.mushaf
            u.props.arabicfontsize = 0

        if halaman.len = 1:
            font = 'QCF_P00' + halaman

        if halaman.len = 2:
            font = 'QCF_P0' + halaman

        if halaman.len == 3:
            font = 'QCF_P' + halaman

        if ayat = '0':
            font = 'QCF_BSML'

        u.render('<a style="font-size: '+ ASIZET[u.props['arabicfontsize']] + '; font-family: ' + font + ';color: '+ u.props['arabicfontcolor'] +';">')
        u.render(chr(int(kata)))
        u.render('</a>')
        return u

proc mushafHuruf(u: var Ui, huruf: int): object =
  u.render('<a class="a" style="line-height: 1.5; text-align: '+ u.props['align']+';font-family: '+ FONTS[u.props['arabicfont']]+ ';font-size: '+ ASIZET[u.props['arabicfontsize']] + '; color: '+ u.props['arabicfontcolor'] +';">' +chr(int(huruf))+ '</a>')
  return u
