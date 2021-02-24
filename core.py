
from init import *
from qs import *

def quranHuruf(qdata, u, index):
    q = Q()
    u.props['align'] = 'right'

    if u.props['medina']:
        u.props['align'] = 'center'
        u.props['tafsir'] = False

    quran = q.huruf
    if u.props['print']:
        quran = q.kata

    if u.props['view'] == 1:
        u.props['firstword'] = False

    u.render('<table style="width: 100%;"><tr><td>')
    q.barisBaru(u)
    reset = True

    for x in quran:

        u.props['arabicfontcolor'] = '#000000'

        if x[u.props['mode']] == index:

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
                if u.props['medina']:
                    q.barisBaru(u)

                if not u.props['medina']:
                    if x[4] == '0':
                        q.barisBaru(u)

                barisSebelum = x[1]

            if halamanBerikut:
                halamanSebelum = x[0]

            if ayatBerikut:
                if not u.props['medina']:
                    if u.props['tafsir'] and ayatSebelum  != '0':
                        q.artiBaru(u)
                        q.artiAyat(u, suratSebelum, ayatSebelum)
                        q.barisBaru(u)

                    q.barisBaru(u)

                ayatSebelum = x[4]

            if suratBerikut:
                suratSebelum = x[3]

#           adding space before next word
            if kataBerikut:
                q.spasiBaru(u)
                if not u.props['medina']:
                    if u.props['word'] and ayatSebelum != '0':
                            q.kataBaru(u)
                            # q.artiKata(u, x[3], x[4], x[5])

                kataSebelum = x[5]

            # show or hide
            if u.props['view']  != 0:
                u.props['arabicfontcolor'] = '#DDDDDD'

            # non ayat
            if x[4] == '0':
                u.props['arabicfontcolor'] = '#000000'

            # first word
            if x[5] == '1' and u.props['firstword'] and x[4] != '0':
                u.props['arabicfontcolor'] = u.props['firstwordcolor']

            # Black
            if x[7] == '1758' or  x[7] == '1769' or x[7] in PAGES:
                u.props['arabicfontcolor'] = '#000000'

#           use font QCF
            if u.props['print']:
                # component, halaman, ayat, unicode kata
                q.mushafKata(u, x[0], x[4], x[6])

#           use font Scheherazade
            if not u.props['print']:
                # component, unicode huruf
                q.mushafHuruf(u, x[7])

    if not u.props['medina']:
        if u.props['tafsir'] and ayatSebelum  != '0':
            q.artiBaru(u)
            q.artiAyat(u, suratSebelum, ayatSebelum)

    u.render('</td></tr></table>')
    return u
