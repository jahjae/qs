
import os
import random
import logging

format = "%(asctime)s: %(message)s"
logging.basicConfig(format=format, level=logging.INFO,datefmt="%H:%M:%S")

def TextFormat(q, u, index):
    u.style('header', {'position': 'sticky', 'top': '0'})
    u.style('a', {'text-decoration': 'none'})
    u.props['menu'] = 0

    u.props['text'] = u.props['text'] + 1

    if u.props['text'] == len(FORMAT):
        u.props['text'] = 0

    os.environ['INDEX'] = str(u.props['index'])
    noPage = str(u.props['index'])
    exec(ADDRESS['/']+'(q, u, noPage)')

def Number(q, u, index):

    u.style('a', {'text-decoration': 'none'})
    u.props['menu'] = 0
    u.header('<a href="/menu">'+'>'+'</a>')
    u.style('p.surat', {'font-size': TSIZET[u.props['fontsize']],
        'text-align': 'left','line-height': '1',})
    u.style('p.ayat', {'font-size': TSIZET[u.props['fontsize']],
        'text-align': 'right', 'line-height': '1',})


    if u.props['mode'] == 4:
        for x in q.surat:
            u.render('<p class="surat"><a href="/'+str(x)+'">'+str(x)+'</a>'+q.surat[x][1]+', '
                    +q.surat[x][0]+', '
                    +q.surat[x][2]+', '
                    +q.surat[x][4]+'</p>')
            u.render('<p class="ayat">')
            # quranAyat(q, u, str(x), str(0))
            u.render('</p>')

    if u.props['mode'] == 3:
        for x in q.surat:
            u.render('<p class="surat"><a href="/'+str(x)+'">'
                    +str(x)+'. </a>'
                    +q.surat[x][1]+', '
                    +q.surat[x][0]+', '
                    +q.surat[x][2]+', '
                    +q.surat[x][4]+'</p>')
            u.render('<p class="ayat">')
            # quranAyat(q, u, str(x), str(0))
            u.render('</p>')


    if u.props['mode'] == 2:
        u.style('p.surat', {'font-size': TSIZET[u.props['fontsize']],
            'text-align': 'left', 'line-height': '1',})
        u.style('p.ayat', {'font-size': TSIZET[u.props['fontsize']],
            'text-align': 'right', 'line-height': '1',})

        for x in q.juz:
            u.render('<p><a href="/'+str(x)+'">'
                    +str(x)+'. </a>'
                    +q.surat[int(q.juz[x]['surat'])][1]
                    +' / '+q.juz[x]['ayat']+'</p>')
            u.render('<p class="ayat">')
            quranAyat(q, u, q.juz[x]['surat'], q.juz[x]['ayat'])
            u.render('</p>')


    if u.props['mode'] == 0:
        for x in q.halaman:
            u.render('<p><a href="/'+str(x)+'">'+str(x)
                    +'. </a>'+q.surat[int(q.halaman[x]['surat'])][1]
                    +' / '+q.halaman[x]['ayat']+'</p>')

def quranAyat(q, u, s, a):
    logging.info('QS '+str(s)+':'+str(a))
    reset = True
    for x in q.kata[0:]:
        if x[3] == str(s):
            if x[4] == str(a):
                u.props['page']     = int(x[0])
                u.props['row']      = int(x[1])
                u.props['juz']      = int(x[2])
                u.props['surat']    = int(x[3])
                u.props['ayat']     = int(x[4])

                if reset:
                    reset = False
                    halamanSebelum = x[0]
                    barisSebelum = x[1]
                    juzSebelum = x[2]
                    suratSebelum = x[3]
                    ayatSebelum = x[4]
                    kataSebelum = x[5]

                u.props['arabicfontcolor'] = os.environ.get('ARABICFONTCOLOR')
                kataBerikut = q.compare(x[5], kataSebelum)

                if kataBerikut:
                    kataSebelum = x[5]
                    q.spasi(u)

                u.props['arabicfont'] = int(os.environ.get('ARABICFONT'))
                u.props['arabicfontsize'] = int(os.environ.get('ARABICFONTSIZE'))

                if u.props['mushaf'] == 1:
                    u.props['arabicfontsize'] = 0

                if u.props['print'] == 1:
                    q.mushafKata(u, x[0], x[4], x[6])

                if u.props['print'] != 1:
                    quranKata(q, u, x)


def quranKata(q, u, x):
    for y in range(int(x[7])):
        pos = y + 8
        pos1 = y + 9
        pos2 = y + 10
        pos3 = y + 11
        pos4 = y + 12

        if u.props['firstword'] == 2:

            # 1619
            if x[pos1] == '1619':
                u.props['arabicfontcolor'] = '#ff0000'
            else:
                # 1614 & 1648
                if x[pos1] == '1614' and x[pos2] == '1648':
                    u.props['arabicfontcolor'] = '#ff0000'
                else:

                    # 1614 & 1575 = A
                    if x[pos1] == '1614' and x[pos2] == '1575':
                        u.props['arabicfontcolor'] = '#ff0000'
                    else:

                        # 1616	1610 = I
                        if x[pos1] == '1616' and x[pos2] == '1610':
                            u.props['arabicfontcolor'] = '#ff0000'
                        else:

                            # 1615	1608 = U
                            if x[pos1] == '1615' and x[pos2] == '1608':
                                u.props['arabicfontcolor'] = '#ff0000'
                            else:
                                u.props['arabicfontcolor'] = os.environ.get('ARABICFONTCOLOR')


        # show or hide
        if u.props['view']  != 0:
            u.props['arabicfontcolor'] = u.props['backgroundcolor']

        # first word
        if u.props['firstword'] == 1 and x[5] == '1':
            u.props['arabicfontcolor'] = u.props['firstwordcolor']

        # non ayat
        if x[4] == '0':
            u.props['arabicfontcolor'] = os.environ.get('ARABICFONTCOLOR')

        # use font for Number
        if x[pos] in PAGES:
            u.props['arabicfontcolor'] = os.environ.get('ARABICFONTCOLOR')

        q.mushafHuruf(u, x[pos])


def quranHuruf(q, u, index):
    u.style('header', {'position': 'sticky', 'top': '0', 'padding': '5px 0 0 0'})
    u.style('p.page', {'position': 'sticky', 'top': '0', 'padding': '10px 0 0 0'})

    u.style('a', {'text-decoration': 'none'})
    u.render('<meta charset="UTF-8" name="viewport" content="width=device-width, initial-scale=1.0">')

    u.props['mode']             = int(os.environ.get('MODE'))
    u.props['view']             = int(os.environ.get('VIEW'))
    u.props['mushaf']           = int(os.environ.get('MUSHAF'))
    u.props['word']             = int(os.environ.get('WORD'))
    u.props['tafsir']           = int(os.environ.get('TAFSIR'))
    u.props['print']            = int(os.environ.get('PRINT'))
    u.props['firstword']        = int(os.environ.get('FIRSTWORD'))
    u.props['index']            = int(os.environ.get('INDEX'))

    u.props['arabicfontsize']   = int(os.environ.get('ARABICFONTSIZE'))
    u.props['fontsize']         = int(os.environ.get('FONTSIZE'))

    u.props['backgroundcolor']  = os.environ.get('BACKGROUNDCOLOR')
    u.props['firstwordcolor']   = os.environ.get('FIRSTWORDCOLOR')
    u.props['fontcolor']        = os.environ.get('FONTCOLOR')
    u.props['align']            = 'right'

    u.style('body',{'background-color': u.props['backgroundcolor']})

    if u.props['mode'] == 3:
        u.render('<header><a href="/menu">'+'>'+'</a>'+' '+MODET[u.props['mode']].upper()+' '+str(u.props['index'])+' / 114 - '+ q.surat[u.props['index']][1] +'</header>')

    if u.props['mode'] != 3:
        if u.props['mode'] == 4:
            u.header('<a href="/menu">'+'>'+'</a>'+' '+q.surat[u.props['surat']][1]+' '+str(u.props['surat'])+':'+str(u.props['ayat']))
        else:
            u.header('<a href="/menu">'+'>'+'</a>'+' '+MODET[u.props['mode']].upper()+' '+str(u.props['index']))


    if u.props['mushaf'] == 1:
        u.props['align'] = 'center'
        u.props['arabicfontsize'] = 0
        u.props['tafsir'] = 0

    if u.props['view'] == 1:
        u.props['firstword'] = 0


    reset = True
    quran = q.kata

    u.render('<div class="m" style="width: 100%;">')
    q.barisBaru(u)
    for x in quran[0:]:

        u.props['arabicfontcolor'] = os.environ.get('ARABICFONTCOLOR')

        modeon = False
        if x[u.props['mode']] == index:
            if u.props['mode'] == 4:
                if x[3] == str(u.props['surat']):
                    modeon = True
                else:
                    modeon = False

            if u.props['mode'] != 4:
                modeon = True


        if modeon:
            u.props['page'] = int(x[0])
            u.props['row'] = int(x[1])
            u.props['juz'] = int(x[2])
            u.props['surat'] = int(x[3])
            u.props['ayat'] = int(x[4])

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


            if ayatBerikut:
                #q.nomorAyat(u, ayatSebelum)

                if u.props['mushaf'] != 1:
                    if u.props['tafsir'] == 1 and ayatSebelum  != '0':
                        q.artiBaru(u)
                        q.artiAyat(u, suratSebelum, ayatSebelum)

                    if not halamanBerikut:
                        q.barisBaru(u)

                if halamanBerikut:
                    halamanSebelum = x[0]
                    q.barisBaru(u)

                    u.style("m", {'align': "center"})

                    u.render('<p class="page"></p>')
                    u.render('<div style="border-bottom: 10px solid #dddddd"></div>')
                    u.render('<p class="page">PAGE: '+halamanSebelum+'</p>')

                ayatSebelum = x[4]
                kataSebelum = '0'

            if suratBerikut:
                suratSebelum = x[3]
                ayatSebelum = '0'
                kataSebelum = '0'

#           adding space before next word
            if kataBerikut:
                q.spasi(u)
                if u.props['mushaf'] != 1:
                    if u.props['word'] == 1 and ayatSebelum != '0' and kataSebelum != '0':
                        if u.props['tafsir'] == 1:
                            q.kataBaru(u)
                            q.artiKata(u, suratSebelum, ayatSebelum, kataSebelum)
                            q.kataBaru(u)

                        q.barisBaru(u)

                kataSebelum = x[5]

            # use font QCF
            if u.props['print'] == 1:
                # component, halaman, ayat, unicode kata
                u.props['arabicfontsize'] = int(os.environ.get('ARABICFONTSIZE'))

                if u.props['mushaf'] == 1:
                    u.props['arabicfontsize'] = 0

                q.mushafKata(u, x[0], x[4], x[6])


            if u.props['print'] != 1:
                q.spasi(u)

                u.props['arabicfont'] = int(os.environ.get('ARABICFONT'))
                u.props['arabicfontsize'] = int(os.environ.get('ARABICFONTSIZE'))

                if u.props['mushaf'] == 1:
                    u.props['arabicfontsize'] = 0

                quranKata(q, u, x)


    if u.props['mushaf'] != 1:
        if u.props['tafsir'] and ayatSebelum  != '0':
            q.artiBaru(u)
            q.artiAyat(u, suratSebelum, ayatSebelum)

    u.render('</div>')
    u.style("m", {'align': "center"})


    u.props['arabicfont'] = int(os.environ.get('ARABICFONT'))
    u.props['arabicfontsize'] = int(os.environ.get('ARABICFONTSIZE'))
    return u


def Daily(q, u, index):
    u.highlight('.d')
    u.style('a', {'text-decoration': 'none'})
    u.props['menu'] = 1

    u.style('a', {'font-size': TSIZET[1],'text-align': 'center','line-height': '1',})
    u.style('p', {'font-size': TSIZET[1],'text-align': 'center','line-height': '1',})
    u.style('body',{'background-color': u.props['backgroundcolor']})

    u.props['arabicfontsize'] = os.environ.get('ARABICFONTSIZE')

    s = random.randint(1, 114)
    a = random.randint(1, int(q.surat[s][0]))

    u.header('<a href="/menu">'+'>'+'</a>')
    u.p('')
    u.render('<div class="m" style="width: 100%; text-align: center; line-height: 1.2">')

    quranAyat(q, u, s, a)

    u.render('<div>')
    u.style("m", {'align': "center"})

    u.props['index'] = s
    u.props['mode'] = 3

    u.props['arabicfont'] = int(os.environ.get('ARABICFONT'))
    u.props['fontsize'] = int(os.environ.get('FONTSIZE'))
    os.environ['MODE'] = str(u.props['mode'])
    os.environ['INDEX'] = str(u.props['index'])

    u.style('p', {'margin': '10px', 'font-size': TSIZET[u.props['fontsize']],
        'text-align': 'center','line-height': '1',})
    u.render('<p>'+q.artiayat[s][a]+'</p>')
    u.style('p', {'font-size': TSIZET[u.props['fontsize']],'text-align': 'center',
        'line-height': '1.6',})
    u.render('<p>'+q.surat[s][1]+' '+str(s)+':'+str(a)+'</p>')
    u.props['arabicfontsize'] = int(os.environ.get('ARABICFONTSIZE'))


def Index(q, u, index):
    logging.info('Indexing ...')
    u.style('a', {'text-decoration': 'none'})
    u.style('p', {'line-height': '0.5'})
    u.props['menu'] = 0

    u.render('<header><a href="/menu">'+'>'+'</a></header>')

    for x in q.indexkata:
        u.p('<a href="/'+str(x)+'">'+str(x).upper()+'. </a>')
        u.p('')
        for y in q.indexkata[x]:
            u.p('QS '+y[1]+':'+y[2])

        u.p('')


def Goto(q, u, index):
    u.style('a', {'text-decoration': 'none'})
    u.props['menu'] = 0

    if u.props['mode'] == 0:
        u.props['page'] = u.props['page'] + 1
        if u.props['page'] == 605:
            u.props['page'] = 1

        u.props['index'] = u.props['page']

    if u.props['mode'] == 1:
        u.props['row'] = u.props['row'] + 1
        if u.props['row'] == q.surat[u.props['surat']][0]:
            u.props['row'] = 1

        u.props['index'] = u.props['row']

    if u.props['mode'] == 2:
        u.props['juz'] = u.props['juz'] + 1
        if u.props['juz'] == 31:
            u.props['juz'] = 1

        u.props['index'] = u.props['juz']

    if u.props['mode'] == 3:
        u.props['surat'] = u.props['surat'] + 1
        if u.props['surat'] == 115:
            u.props['surat'] = 1

        u.props['index'] = u.props['surat']

    if u.props['mode'] == 4:
        u.props['ayat'] = u.props['ayat'] + 1

        if u.props['ayat'] == int(q.surat[u.props['surat']][0]) + 1:
            u.props['ayat'] = 1

            u.props['surat'] = u.props['surat'] + 1
            if u.props['surat'] == 115:
                u.props['surat'] = 1

        u.props['index'] = u.props['ayat']

    os.environ['INDEX'] = str(u.props['index'])

    noPage = str(u.props['index'])
    exec(ADDRESS['/']+'(q, u, noPage)')

def Search(q,  u, index):
    u.style('header', {'position': 'sticky', 'top': '0', 'padding': '5px 0 0 0'})
    u.style('a', {'text-decoration': 'none'})

    u.render('<header><a href="/menu">'+'>'+'</a></header>')
    u.render('<div style="width: 100%;">')

    u.props['arabicfont'] = int(os.environ.get('ARABICFONT'))

    for x in q.huruf:
        q.barisBaru(u)
        u.render('<a class ="d" style="text-align: center; font-size: 50vw; color: '+q.huruf[x]['color']+';font-family: '+ FONTS[u.props['arabicfont']]+';" href="/select/">' +chr(int(x))+ '</a>')

    u.render('</div>')


def Info(q, u, index):
    u.style('header', {'position': 'sticky', 'top': '0', 'padding': '5px 0 0 0'})
    u.style('p', {'font-size': TSIZET[1]})
    u.style('a', {'text-decoration': 'none'})

    u.render('<header><a href="/menu">'+'>'+'</a></header>')

    u.p('<a href="/daily">DAILY</a> > AYAT')

    if u.props['mode'] == 4:
        u.render('<p> <a href="/mode">MODE</a> > ')
        u.render('<a href="/goto">'+MODET[u.props['mode']]+'</a> > '+str(u.props['surat'])+':'+str(u.props['ayat'])+'</p>')

    if u.props['mode'] == 3:
        u.render('<p> <a href="/mode">MODE</a> > ')
        u.render('<a href="/goto">'+MODET[u.props['mode']]+'</a> > <a href="/number">'+str(u.props['index'])+'</a> / 114 - '+q.surat[u.props['index']][1]+'</p>')

    if u.props['mode'] == 2:
        u.render('<p> <a href="/mode">MODE</a> > ')
        u.render('<a href="/goto">'+MODET[u.props['mode']] +'</a> > <a href="/number">'+str(u.props['index'])+'</a> / 30</p>')

    if u.props['mode'] == 1:
        u.render('<p> <a href="/mode">MODE</a> > ')
        u.render('<a href="/goto">'+MODET[u.props['mode']] +'</a> > '+str(u.props['index'])+' / '+u.quran[u.props['surat']][0]+'</p>')

    if u.props['mode'] == 0:
        u.render('<p> <a href="/mode">MODE</a> > ')
        u.render('<a href="/goto">'+MODET[u.props['mode']] +'</a> > <a href="/number">'+str(u.props['index'])+'</a> / 604</p>')

    u.render('<p> <a href="/mushaf">MUSHAF</a>: '               +MUSHAFT[u.props['mushaf']]+'</p>')
    u.render('<p> <a href="/quran">READING</a>: '               +LOGICALT[u.props['print']] +'</p>')
    u.render('<p> <a href="/text">TEXT</a>: '                   +FORMAT[u.props['text']]+'</p>')
    u.render('<p> <a href="/view">VIEW</a>: '                   +VIEWT[u.props['view']] +'</p>')
    u.render('<p> <a href="/pertama">HIGHLIGH</a>: '            +HIGHLIGH[u.props['firstword']] +'</p>')
    u.p('<a href="/word">BY WORD</a>: '                         +LOGICALT[u.props['word']])
    u.render('<p> <a href="/translation">TRANSLATION</a>: '     +LOGICALT[u.props['tafsir']] +' / ')
    u.render('<a href="/fontsize">SIZE</a>: '                   +TSIZET[u.props['fontsize']]+'</p>')
    u.render('<p> <a href="/fontname">FONTS</a>: '              +FONTS[u.props['arabicfont']]+' / ')
    u.render('<a href="/arabicsize">SIZE</a>: '                 +ASIZET[u.props['arabicfontsize']]+'</p>')
    u.p('<a href="/index">INDEX</a>')
    u.p('<a href="/search">DICTIONARY</a>')
    u.p('<a href="/theme">THEME</a>: '                          +THEMET[u.props['theme']])
    u.p('<a href="/match">MATCH</a>: '                          +MATCHT[u.props['match']])
    u.p('<a href="/note">NOTE</a>')

def Menu(q, u, index):
    logging.info('Menu ...')
    u.style('header', {'position': 'sticky', 'top': '0', 'padding': '5px 0 0 0'})
    u.style('a', {'text-decoration': 'none'})

    os.environ['INDEX'] = str(u.props['index'])

    if u.props['menu'] == 1:
        u.props['menu'] = 0

        noPage = str(u.props['index'])
        exec(ADDRESS['/']+'(q, u, noPage)')
    else:
        u.props['menu'] = 1
        Info(q, u, index)

def Match(q, u, index):
    u.style('header', {'position': 'sticky', 'top': '0', 'padding': '5px 0 0 0'})
    u.style('a', {'text-decoration': 'none'})

    u.props['menu'] = 0

    if u.props['match'] == len(MATCHT)-1:
        u.props['match'] = 0
    else:
        u.props['match'] = u.props['match'] + 1

    noPage = str(u.props['index'])
    exec(ADDRESS['/']+'(q, u, noPage)')

def Mode(q, u, index):
    u.style('header', {'position': 'sticky', 'top': '0', 'padding': '5px 0 0 0'})
    u.style('a', {'text-decoration': 'none'})
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

    if u.props['mode'] == 1:
            u.props['index'] = u.props['row']

    if u.props['mode'] == 2:
            u.props['index'] = u.props['juz']

    if u.props['mode'] == 3:
            u.props['index'] = u.props['surat']

    if u.props['mode'] == 4:
            u.props['ayat'] = 1
            u.props['index'] = u.props['ayat']

    os.environ['MODE'] = str(u.props['mode'])
    os.environ['INDEX'] = str(u.props['index'])

    noPage = str(u.props['index'])
    exec(ADDRESS['/']+'(q, u, noPage)')


def Arabicsize(q, u, index):
    u.style('header', {'position': 'sticky', 'top': '0', 'padding': '5px 0 0 0'})
    u.style('a', {'text-decoration': 'none'})
    u.props['menu'] = 0

    u.props['arabicfontsize'] = u.props['arabicfontsize'] + 1

    if u.props['arabicfontsize'] == len(ASIZET):
        u.props['arabicfontsize'] = 1

    os.environ['ARABICFONTSIZE'] = str(u.props['arabicfontsize'])
    os.environ['INDEX'] = str(u.props['index'])

    noPage = str(u.props['index'])
    exec(ADDRESS['/']+'(q, u, noPage)')


def Fontname(q, u, index):
    u.style('header', {'position': 'sticky', 'top': '0', 'padding': '5px 0 0 0'})
    u.style('a', {'text-decoration': 'none'})
    u.props['menu'] = 0

    u.props['arabicfont'] = u.props['arabicfont'] + 1

    if u.props['arabicfont'] == len(FONTS):
        u.props['arabicfont'] = 1

    os.environ['ARABICFONT'] = str(u.props['arabicfont'])
    os.environ['INDEX'] = str(u.props['index'])

    noPage = str(u.props['index'])
    exec(ADDRESS['/']+'(q, u, noPage)')

def Fontsize(q, u, index):
    u.style('header', {'position': 'sticky', 'top': '0', 'padding': '5px 0 0 0'})
    u.style('a', {'text-decoration': 'none'})
    u.props['menu'] = 0

    u.props['fontsize'] = u.props['fontsize'] + 1

    if u.props['fontsize'] == len(TSIZET)+1:
        u.props['fontsize'] = 1

    os.environ['FONTSIZE'] = str(u.props['fontsize'])
    os.environ['INDEX'] = str(u.props['index'])

    noPage = str(u.props['index'])
    exec(ADDRESS['/']+'(q, u, noPage)')

def Theme(qdata, u, index):
    u.style('header', {'position': 'sticky', 'top': '0', 'padding': '5px 0 0 0'})
    u.props['menu'] = 0
    u.style('a', {'text-decoration': 'none'})

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
    u.style('header', {'position': 'sticky', 'top': '0', 'padding': '5px 0 0 0'})
    u.style('a', {'text-decoration': 'none'})
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
    u.style('header', {'position': 'sticky', 'top': '0', 'padding': '5px 0 0 0'})
    u.style('a', {'text-decoration': 'none'})
    u.props['menu'] = 0

    if u.props['firstword'] == len(HIGHLIGH) - 1:
        u.props['firstword'] = 0
    else:
        u.props['firstword'] = u.props['firstword'] + 1

    os.environ['FIRSTWORD'] = str(u.props['firstword'])
    os.environ['INDEX'] = str(u.props['index'])

    noPage = str(u.props['index'])
    exec(ADDRESS['/']+'(qdata, u, noPage)')


def Quran(q, u, index):
    u.style('header', {'position': 'sticky', 'top': '0', 'padding': '5px 0 0 0'})
    u.style('a', {'text-decoration': 'none'})
    u.props['menu'] = 0

    if u.props['print'] == 1:
        u.props['print'] = 0
    else:
        u.props['print'] = 1

    os.environ['PRINT'] = str(u.props['print'])
    os.environ['INDEX'] = str(u.props['index'])

    noPage = str(u.props['index'])
    exec(ADDRESS['/']+'(q, u, noPage)')


def Translation(qdata, u, index):
    u.style('header', {'position': 'sticky', 'top': '0', 'padding': '5px 0 0 0'})
    u.style('a', {'text-decoration': 'none'})
    u.props['menu'] = 0

    if u.props['tafsir'] == 1:
        u.props['tafsir'] = 0
    else:
        u.props['tafsir'] = 1

    os.environ['TAFSIR'] = str(u.props['tafsir'])
    os.environ['INDEX'] = str(u.props['index'])

    noPage = str(u.props['index'])
    exec(ADDRESS['/']+'(qdata, u, noPage)')


def Word(qdata, u, index):
    u.style('header', {'position': 'sticky', 'top': '0', 'padding': '5px 0 0 0'})
    u.style('a', {'text-decoration': 'none'})
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
    u.style('header', {'position': 'sticky', 'top': '0', 'padding': '5px 0 0 0'})
    u.style('a', {'text-decoration': 'none'})
    u.props['menu'] = 0

    if u.props['mushaf'] == 1:
        u.props['mushaf'] = 0
    else:
        u.props['mushaf'] = 1

    os.environ['MUSHAF'] = str(u.props['mushaf'])
    os.environ['INDEX'] = str(u.props['index'])

    noPage = str(u.props['index'])
    exec(ADDRESS['/']+'(qdata, u, noPage)')
