#
#   Designed by Ismail Umar
#   Quran Core
#

from init import *
from qs import *

def quranHuruf(Kata, view, Key):
    qh = Ui()
    reset = True

    Kata.append('<table style="width: 100%;"><tr><td>')

    qh.barisBaru(Kata, '200%', 'right', '1.2')

    for x in qh.Huruf:
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

            barisBerikut = qh.compare(x[1], barisSebelum)
            juzBerikut = qh.compare(x[2], juzSebelum)
            suratBerikut = qh.compare(x[3], suratSebelum)
            ayatBerikut = qh.compare(x[4], ayatSebelum)
            kataBerikut = qh.compare(x[5], kataSebelum)

            if MUSHAF:
                if barisBerikut:
                    qh.barisBaru(Kata, '25px', 'left', '1')
                    qh.barisBaru(Kata, '200%', 'right' , '1.2')
                    barisSebelum = x[1]

            if not MUSHAF:
                if ayatBerikut:

                    if TAFSIR:
                        qh.barisBaru(Kata, '100%', 'left', '1.2')
                        qh.artiAyat(Kata, qh.Terjemahan, suratSebelum, ayatSebelum)
                        qh.barisBaru(Kata, '200%', 'right' , '1.2')

                    qh.barisBaru(Kata, '200%', 'right' , '1.2')
                    ayatSebelum = x[4]

            if kataBerikut:
                Kata.append(chr(32))
                kataSebelum = x[5]

#           print Unicode4
            qh.mushafHuruf(Kata, x[7])

    Kata.append('</td></tr></table>')
    return Kata
