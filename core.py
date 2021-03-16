
from init import *
import os

def Index(q, u, index):
    u.props['menu'] = 0

    if u.props['mode'] == 0:
        u.props['page'] = u.props['page'] + 1
        u.props['index'] = u.props['page']

    if u.props['mode'] == 1:
        u.props['page'] = u.props['page'] + 1
        u.props['index'] = u.props['page']

    if u.props['mode'] == 2:
        u.props['juz'] = u.props['juz'] + 1
        u.props['index'] = u.props['juz']

    if u.props['mode'] == 3:
        u.props['surat'] = u.props['surat'] + 1
        u.props['index'] = u.props['surat']


    os.environ['INDEX'] = str(u.props['index'])
    noPage = str(u.props['index'])
    exec(ADDRESS['/']+'(q, u, noPage)')

def Search(q,  u, index):
    u.render('<header><a href="/menu">'+'>'+'</a></header>')

    u.render('<div>')
    u.render('<table style="padding: 10px ;width: 100%;"><tr><td>')

    u.props['arabicfontsize'] = '50px'
    u.props['arabicfont'] = 'Scheherazade'

    for x in range(82):
        q.barisBaru(u)
        u.render('<a style="font-size: '+u.props['arabicfontsize']+ '; text-decoration: none; font-family: '+ u.props['arabicfont']+';" href="/select/">' +chr(CHAR[x])+ '</a>')

    u.render('</td></tr></table></div>')


def Info(qdata, u, index):
    u.render('<header><a href="/menu">'+'>'+'</a></header>')

    u.render('<p style="font-size:' + u.props['fontsize'] + ';"> <a href="/mushaf">MUSHAF</a>: '+ MUSHAFT[u.props['mushaf']]+'</p>')
    u.render('<p style="font-size:' + u.props['fontsize'] + ';"> <a href="/pertama">FIRST WORD</a>: '+ LOGICALT[u.props['firstword']] +'</p>')
    u.render('<p style="font-size:' + u.props['fontsize'] + ';"> <a href="/mode">MODE</a>: '+ MODET[u.props['mode']] +'</p>')
    u.render('<p style="font-size:' + u.props['fontsize'] + ';"> <a href="/index">INDEX</a>: '+ str(u.props['index'])+'</p>')
    u.render('<p style="font-size:' + u.props['fontsize'] + ';"> <a href="/view">VIEW</a>: '+ VIEWT[u.props['view']] +'</p>')
    u.render('<p style="font-size:' + u.props['fontsize'] + ';"> <a href="/translation">TRANSLATION</a>: '+ LOGICALT[u.props['tafsir']] +'</p>')
    u.render('<p style="font-size:' + u.props['fontsize'] + ';"> <a href="/kata">WORD BY WORD</a>: '+ LOGICALT[u.props['word']] +'</p>')
    u.render('<p style="font-size:' + u.props['fontsize'] + ';"> <a href="/theme">THEME</a>: '+ THEMET[u.props['theme']]+'</p>')
    u.render('<p style="font-size:' + u.props['fontsize'] + ';"> PAGE: '+ str(u.props['page']) +' / 604</p>')
    u.render('<p style="font-size:' + u.props['fontsize'] + ';"> JUZ: '+ str(u.props['juz']) +' / 30</p>')
    u.render('<p style="font-size:' + u.props['fontsize'] + ';"> SURA: '+ str(u.props['surat'])+' / 114 - ' +str(qdata.surat[u.props['surat']][1]) + ' ' + qdata.surat[u.props['surat']][0]+'</p>')
    u.render('<p style="font-size:' + u.props['fontsize'] + ';"> <a href="/search">SEARCH</a></p>')

def Menu(qdata, u, index):
    os.environ['INDEX'] = str(u.props['index'])

    if u.props['menu'] == 1:
        u.props['menu'] = 0

        noPage = str(u.props['index'])
        exec(ADDRESS['/']+'(qdata, u, noPage)')
    else:
        u.props['menu'] = 1
        Info(qdata, u, index)


def Mode(qdata, u, index):
    u.props['menu'] = 0
    if u.props['mode'] == len(MODET)-1:
        u.props['mode'] = 0
    else:
        u.props['mode'] = u.props['mode'] + 1

    if u.props['mode'] == 1:
        u.props['mode'] = 2

    u.props['selected'] = MODET[u.props['mode']]
    if u.props['mode'] == 0:
            u.props['index'] = u.props['page']

    if u.props['mode'] == 2:
            u.props['index'] = u.props['juz']

    if u.props['mode'] == 3:
            u.props['index'] = u.props['surat']

    os.environ['MODE'] = str(u.props['mode'])
    os.environ['INDEX'] = str(u.props['index'])

    noPage = str(u.props['index'])
    exec(ADDRESS['/']+'(qdata, u, noPage)')

def quranHuruf(q, u, index):
    u.props['mode'] = int(os.environ.get('MODE'))
    u.props['view'] = int(os.environ.get('VIEW'))
    u.props['mushaf'] = int(os.environ.get('MUSHAF'))
    u.props['word'] = int(os.environ.get('WORD'))
    u.props['tafsir'] = int(os.environ.get('TAFSIR'))
    u.props['print'] = int(os.environ.get('PRINT'))
    u.props['firstword'] = int(os.environ.get('FIRSTWORD'))
    u.props['index'] = int(os.environ.get('INDEX'))

    u.props['backgroundcolor'] = os.environ.get('BACKGROUNDCOLOR')
    u.props['firstwordcolor'] = os.environ.get('FIRSTWORDCOLOR')
    u.props['fontcolor'] = os.environ.get('FONTCOLOR')
    u.props['align'] = 'right'

    u.style('body',{'background-color': u.props['backgroundcolor']})
    u.render('<header><a href="/menu">'+'>'+'</a>'+' '+u.props['selected'].upper()+' '+str(u.props['index'])+'</header>')


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

    u.render('<div>')
    u.render('<table style="padding: 10px ;width: 100%;"><tr><td>')
    q.barisBaru(u)
    reset = True

    for x in quran[0:]:

        u.props['arabicfontcolor'] = os.environ.get('ARABICFONTCOLOR')

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
                u.props['arabicfontcolor'] = u.props['backgroundcolor']

            # first word
            if u.props['firstword'] == 1 and x[5] == '1':
                u.props['arabicfontcolor'] = u.props['firstwordcolor']

            # non ayat
            if x[4] == '0':
                u.props['arabicfontcolor'] = os.environ.get('ARABICFONTCOLOR')

            # Black
            if u.props['print'] != 1:
                if x[7] == '1758' or  x[7] == '1769':
                    u.props['arabicfontcolor'] = '#bdb76b'

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
                    u.props['arabicfontcolor'] = os.environ.get('ARABICFONTCOLOR')

                # component, unicode huruf
                q.mushafHuruf(u, x[7])

    if u.props['mushaf'] != 1:
        if u.props['tafsir'] and ayatSebelum  != '0':
            q.artiBaru(u)
            q.artiAyat(u, suratSebelum, ayatSebelum)

    u.render('</td></tr></table></div>')
    return u

def Theme(qdata, u, index):
    u.props['menu'] = 0
    if u.props['theme'] == len(COLOR)-1:
        u.props['theme'] = 0
    else:
        u.props['theme'] = u.props['theme'] + 1

    x = u.props['theme']

    os.environ['BACKGROUNDCOLOR'] = COLOR[x][0]
    os.environ['FIRSTWORDCOLOR'] = COLOR[x][1]
    os.environ['ARABICFONTCOLOR'] = COLOR[x][2]
    os.environ['FONTCOLOR'] = COLOR[x][3]

    os.environ['THEME'] = str(u.props['theme'])
    os.environ['INDEX'] = str(u.props['index'])

    u.props['backgroundcolor'] = os.environ['BACKGROUNDCOLOR']

    noPage = str(u.props['index'])
    exec(ADDRESS['/']+'(qdata, u, noPage)')


def View(qdata, u, index):
    u.props['menu'] = 0
    if u.props['view'] == len(VIEWT)-1:
        u.props['view'] = 0
    else:
        u.props['view'] = u.props['view'] + 1

    os.environ['VIEW'] = str(u.props['view'])
    os.environ['INDEX'] = str(u.props['index'])

    noPage = str(u.props['index'])
    exec(ADDRESS['/']+'(qdata, u, noPage)')

def Pertama(qdata, u, index):
    u.props['menu'] = 0
    if u.props['firstword'] == 1:
        u.props['firstword'] = 0
    else:
        u.props['firstword'] = 1

    os.environ['FIRSTWORD'] = str(u.props['firstword'])
    os.environ['INDEX'] = str(u.props['index'])

    noPage = str(u.props['index'])
    exec(ADDRESS['/']+'(qdata, u, noPage)')


def Quran(qdata, u, index):
    u.props['menu'] = 0
    if u.props['print'] == 1:
        u.props['print'] = 0
    else:
        u.props['print'] = 1

    os.environ['PRINT'] = str(u.props['print'])
    os.environ['INDEX'] = str(u.props['index'])

    noPage = str(u.props['index'])
    exec(ADDRESS['/']+'(qdata, u, noPage)')


def Translation(qdata, u, index):
    u.props['menu'] = 0
    if u.props['tafsir'] == 1:
        u.props['tafsir'] = 0
    else:
        u.props['tafsir'] = 1

    os.environ['TAFSIR'] = str(u.props['tafsir'])
    os.environ['INDEX'] = str(u.props['index'])

    noPage = str(u.props['index'])
    exec(ADDRESS['/']+'(qdata, u, noPage)')


def Kata(qdata, u, index):
    u.props['menu'] = 0
    if u.props['word'] == 1:
        u.props['word'] = 0
    else:
        u.props['word'] = 1

    os.environ['WORD'] = str(u.props['word'])
    os.environ['INDEX'] = str(u.props['index'])

    noPage = str(u.props['index'])
    exec(ADDRESS['/']+'(qdata, u, noPage)')


def Mushaf(qdata, u, index):
    u.props['menu'] = 0
    if u.props['mushaf'] == 1:
        u.props['mushaf'] = 0
    else:
        u.props['mushaf'] = 1

    os.environ['MUSHAF'] = str(u.props['mushaf'])
    os.environ['INDEX'] = str(u.props['index'])

    noPage = str(u.props['index'])
    exec(ADDRESS['/']+'(qdata, u, noPage)')
