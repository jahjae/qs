
from init import *
from qs import *

def quranHuruf(Kata, view, Key):
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

    Kata.append('<table style="width: 100%;"><tr><td>')
    q.barisBaru(Kata)

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
                    q.barisBaru(Kata)
                    barisSebelum = x[1]

            if not MUSHAF:
                if ayatBerikut:

                    if TAFSIR:
                        q.size = '50%'
                        q.barisBaru(Kata)
                        q.artiAyat(Kata, suratSebelum, ayatSebelum)
                        q.size = '100%'
                        q.barisBaru(Kata)

                    q.barisBaru(Kata)
                    ayatSebelum = x[4]

            if kataBerikut:
                q.spasiBaru(Kata)
                kataSebelum = x[5]

#           print Unicode4
            if PRINT:
                # halaman, ayat, kata
                q.mushafKata(Kata, x[0], x[4], x[6])

            if not PRINT:
                q.mushafHuruf(Kata, x[7])

    Kata.append('</td></tr></table>')
    return Kata
