
from init import *
from qs import *

def quranHuruf(c, view, Key):
    q = Q()
    reset = True

    if MUSHAF:
        q.align = 'center'
    else:
        q.align = 'right'

    if PRINT:
        quran = q.kata
    else:
        quran = q.huruf

    u.render('<table style="width: 100%;"><tr><td>')
    q.barisBaru(u)

    for x in quran:
        warnaKata = COLOR['BLACK']
        if x[view] == Key:

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

            if MUSHAF:
                if barisBerikut:
                    q.barisBaru(u)
                    barisSebelum = x[1]

            if not MUSHAF:
                if ayatBerikut:

                    if TAFSIR:
                        q.size = '50%'
                        q.barisBaru(u)
                        q.artiAyat(u, suratSebelum, ayatSebelum)
                        q.size = '100%'
                        q.barisBaru(u)

                    q.barisBaru(u)
                    ayatSebelum = x[4]

            if kataBerikut:
                q.spasiBaru(u)
                kataSebelum = x[5]

#           print Unicode4
            if PRINT:
                # component, halaman, ayat, kata
                q.mushafKata(u, x[0], x[4], x[6])

            if not PRINT:
                q.mushafHuruf(u, x[7])

    u.render('</td></tr></table>')
    return u
