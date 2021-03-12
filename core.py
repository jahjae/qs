
from init import *
import os

def View(qdata, u, index):
    if u.props['view'] == 2:
        u.props['view'] = 0
    else:
        u.props['view'] = u.props['view'] + 1

    os.environ['VIEW'] = str(u.props['view'])

def Pertama(qdata, u, index):
    if u.props['firstword'] == 1:
        u.props['firstword'] = 0
    else:
        u.props['firstword'] = 1

    os.environ['FIRSTWORD'] = str(u.props['firstword'])


def Quran(qdata, u, index):
    if u.props['print'] == 1:
        u.props['print'] = 0
    else:
        u.props['print'] = 1

    os.environ['PRINT'] = str(u.props['print'])

def Tafsir(qdata, u, index):
    if u.props['tafsir'] == 1:
        u.props['tafsir'] = 0
    else:
        u.props['tafsir'] = 1

    os.environ['TAFSIR'] = str(u.props['tafsir'])

def Kata(qdata, u, index):
    if u.props['word'] == 1:
        u.props['word'] = 0
    else:
        u.props['word'] = 1

    os.environ['WORD'] = str(u.props['word'])

def Mushaf(qdata, u, index):
    if u.props['mushaf'] == 1:
        u.props['mushaf'] = 0
    else:
        u.props['mushaf'] = 1

    os.environ['MUSHAF'] = str(u.props['mushaf'])

def Halaman(qdata, u, index):
    os.environ['MODE'] = '0'

def Juz(qdata, u, index):
    os.environ['MODE'] = '2'

def Surat(qdata, u, index):
    os.environ['MODE'] = '3'

def Info(qdata, u, index):
    u.render('<p style="font-size:' + u.props['fontsize'] + ';"> MUSHAF: '+ LOGICAL[u.props['mushaf']] +'</p>')
    u.render('<p style="font-size:' + u.props['fontsize'] + ';"> FIRST WORD: '+ LOGICAL[u.props['firstword']] +'</p>')
    u.render('<p style="font-size:' + u.props['fontsize'] + ';"> MODE: '+ MODE[u.props['mode']] +'</p>')
    u.render('<p style="font-size:' + u.props['fontsize'] + ';"> VIEW: '+ VIEW[u.props['view']] +'</p>')
    u.render('<p style="font-size:' + u.props['fontsize'] + ';"> TAFSIR: '+ LOGICAL[u.props['tafsir']] +'</p>')
    u.render('<p style="font-size:' + u.props['fontsize'] + ';"> WORD BY WORD: '+ LOGICAL[u.props['word']] +'</p>')
    u.render('<p style="font-size:' + u.props['fontsize'] + ';"> JUZ: '+ str(u.props['juz']) +'</p>')
    u.render('<p style="font-size:' + u.props['fontsize'] + ';"> SURA: '+ str(qdata.surat[u.props['surat']][1]) + '</p>')
    u.render('<p style="font-size:' + u.props['fontsize'] + ';"> PAGE: '+ str(u.props['page']) +'</p>')


def quranHuruf(qdata, u, index):
    q = qdata
    u.props['mode'] = int(os.environ.get('MODE'))
    u.props['view'] = int(os.environ.get('VIEW'))
    u.props['mushaf'] = int(os.environ.get('MUSHAF'))
    u.props['word'] = int(os.environ.get('WORD'))
    u.props['tafsir'] = int(os.environ.get('TAFSIR'))
    u.props['print'] = int(os.environ.get('PRINT'))
    u.props['firstword'] = int(os.environ.get('FIRSTWORD'))

    u.props['align'] = 'right'

    quran = q.huruf
    if u.props['print']:
        u.props['mushaf'] = 1
        u.props['mode'] = 0
        u.props['view'] = 0
        quran = q.kata

    if u.props['mushaf'] == 1:
        u.props['align'] = 'center'
        u.props['tafsir'] = 0

    if u.props['view'] == 1:
        u.props['firstword'] = 0

    u.render('<table style="width: 100%;"><tr><td>')
    q.barisBaru(u)
    reset = True


    for x in quran[1:]:

        u.props['arabicfontcolor'] = '#000000'

        if x[u.props['mode']] == index:
            u.props['juz'] = int(x[2])
            u.props['surat'] = int(x[3])
            u.props['page'] = int(x[0])

            if reset:
                reset = False
                halamanSebelum = x[0]
                barisSebelum = x[1]
                juzSebelum = x[2]
                suratSebelum = x[3]
                ayatSebelum = x[4]
                kataSebelum = x[5]

            halamanBerikut = q.compare(x[0], halamanSebelum)
            barisBerikut = q.compare(x[1], barisSebelum)
            juzBerikut = q.compare(x[2], juzSebelum)
            suratBerikut = q.compare(x[3], suratSebelum)
            ayatBerikut = q.compare(x[4], ayatSebelum)
            kataBerikut = q.compare(x[5], kataSebelum)

            if barisBerikut:
                if u.props['mushaf'] == 1:
                    q.barisBaru(u)

                if u.props['mushaf'] != 1:
                    if x[4] == '0':
                        q.barisBaru(u)

                barisSebelum = x[1]

            if halamanBerikut:
                halamanSebelum = x[0]

            if ayatBerikut:
                #q.nomorAyat(u, ayatSebelum)

                if u.props['mushaf'] != 1:
                    if u.props['tafsir'] == 1 and ayatSebelum  != '0':
                        q.artiBaru(u)
                        q.artiAyat(u, suratSebelum, ayatSebelum)
                        q.barisBaru(u)

                    q.barisBaru(u)

                ayatSebelum = x[4]
                kataSebelum = '0'


            if suratBerikut:
                suratSebelum = x[3]
                ayatSebelum = '0'
                kataSebelum = '0'

#           adding space before next word
            if kataBerikut:
                q.spasiBaru(u)

                if u.props['mushaf'] != 1:
                    if u.props['word'] == 1 and ayatSebelum != '0' and kataSebelum != '0':
                        if u.props['tafsir'] == 1:
                            q.kataBaru(u)
                            q.artiKata(u, suratSebelum, ayatSebelum, kataSebelum)
                            q.kataBaru(u)

                        q.barisBaru(u)

                kataSebelum = x[5]

            # show or hide
            if u.props['view']  != 0:
                u.props['arabicfontcolor'] = '#ffffff'

            # first word
            if u.props['firstword'] == 1 and x[5] == '1':
                u.props['arabicfontcolor'] = u.props['firstwordcolor']

            # non ayat
            if x[4] == '0':
                u.props['arabicfontcolor'] = '#000000'

            # Black
            if u.props['print'] != 1:
                if x[7] == '1758' or  x[7] == '1769':
                    u.props['arabicfontcolor'] = '#000000'

            # use font QCF
            if u.props['print'] == 1:
                # component, halaman, ayat, unicode kata
                q.mushafKata(u, x[0], x[4], x[6])

#           use font Scheherazade and Harmattan for Numberd
            if u.props['print'] != 1:
                u.props['arabicfontsize'] = '50px'
                u.props['arabicfont'] = 'Scheherazade'
                if x[7] in PAGES:
                    u.props['arabicfont'] = 'Harmattan'
                    u.props['arabicfontsize'] = '30px'
                    u.props['arabicfontcolor'] = '#000000'

                # component, unicode huruf
                q.mushafHuruf(u, x[7])

    if u.props['mushaf'] != 1:
        if u.props['tafsir'] and ayatSebelum  != '0':
            q.artiBaru(u)
            q.artiAyat(u, suratSebelum, ayatSebelum)

    u.render('</td></tr></table>')
    return u
