#
# Quran Parameter

ROLES = ['Administrator','Director','Manager','Supervisor','Coordinator','Operator']

HIGHLIGH = ['OFF','FIRST WORD','MAD']

FONTS = {
    1:  'Scheherazade New',
    0:  'Harmattan',

}

ASIZET = {
    0: '4vw',
    1: '100%',
    2: '200%',
    3: '300%',
}

TSIZET = {
    1: '100%',
    2: '150%',
    3: '200%',
}

MATCHT = {
    0: 'NONE',
    1: 'AYAH',
    2: 'WORD',
}

MODET = {
    0:  'PAGE',
    1:  'ROW',
    2:  'JUZ',
    3:  'SURA',
    4:  'AYAT',
}

LOGICALT = {
    0:  'FALSE',
    1:  'TRUE',
}

VIEWT = {
    0:  'Show All',
    1:  'Hide All',
    2:  'Show only first',

}

MUSHAFT = {
    0:  'BY AYAH',
    1:  'BY ROW'
}

COLOR = [
    ['#ffffff','#ff0000','#000000','#000000','#bdb76b'],
    ['#f0ffff','#ff0000','#000000','#000000','#bdb76b'],
    ['#fff8dc','#ff0000','#000000','#000000','#bdb76b'],
    ['#d3d3d3','#ff0000','#000000','#000000','#bdb76b'],
]

THEMET = {
    0: 'White',
    1: 'Azure',
    2: 'Cornsilk',
    3: 'LightGray',
}

NUMBER = [
    '0',
    '1',
    '2',
    '3',
    '4',
    '5',
    '6',
    '7',
    '8',
    '9'
]
DATA = {
    'huruf'     : './data/db/alfaazha.db',
    'kata'      : './data/db/mushaf.db',
    'juz'       : './data/db/juz.db',
    'surat'     : './data/db/surat.db',
    'halaman'	: './data/db/halaman.db',
    'hizb'      : './data/db/hizb.db',
    'rukuq'     : './data/db/rukuq.db',
    'sajadah'   : './data/db/sajadah.db',
    'artiayat'  : './data/db/depag.db',
    'tafsir'    : './data/db/jalalayn.db',
    'artikata'  : './data/db/kata.db',
}

SYMBOL = [
    '1619',
    '1769',
    '1758',
]

PAGES = {
    '1757' : '1757',
    '1632' : '1632',
    '1633' : '1633',
    '1634' : '1634',
    '1635' : '1635',
    '1636' : '1636',
    '1637' : '1637',
    '1638' : '1638',
    '1639' : '1639',
    '1640' : '1640',
    '1641' : '1641',
}

PAGENUMBER = {
    '0' : 1632,
    '1' : 1633,
    '2' : 1634,
    '3' : 1635,
    '4' : 1636,
    '5' : 1637,
    '6' : 1638,
    '7' : 1639,
    '8' : 1640,
    '9' : 1641,
}

ADDRESS = {
    '/'             : 'quranHuruf',
    '/mushaf'       : 'Mushaf',
    '/word'         : 'Word',
    '/translation'  : 'Translation',
    '/quran'        : 'Quran',
    '/view'         : 'View',
    '/info'         : 'Info',
    '/pertama'      : 'Pertama',
    '/theme'        : 'Theme',
    '/menu'         : 'Menu',
    '/mode'         : 'Mode',
    '/goto'         : 'Goto',
    '/search'       : 'Search',
    '/arabicsize'   : 'Arabicsize',
    '/fontsize'     : 'Fontsize',
    '/daily'        : 'Daily',
    '/number'       : 'Number',
    '/page'         : 'Page',
    '/juz'          : 'Juz',
    '/fontname'     : 'Fontname',
    '/text'         : 'TextFormat',
    '/index'        : 'Index',
    '/nimu'         : 'Nimu',
    '/role'         : 'Role',
    '/item'         : 'Item',
    '/action'       : 'Action',
    '/note'         : 'Note',
}


FORMAT = {
    0:  'UTHMANI',
    1:  'CLEAN',
}


PLAIN = {
    '1600': True,
    '1706': True,
    '32' : True,
    '1772': True,
    '1612': True,
    '1613': True,
    '1614' : True,
    '1615' : True,
    '1616' : True,
    '1617' : True,
    '1648' : True,
    '1755': True,
    '1771': True,
    '1765': True,
    '1753': True,
    '1766': True,
    '1761' : False,
    '1754': True,
    '1756': True,
    '1770': True,
    '1763': True,
    '1752': True,
    '1620': True,
    '1767': True,
    '1619': True,
    '1768': True,
    '1773': True,
    '1762': True,
    '1611': True,
    '1618' : True,
    '1757' : True,
    '1769' : True,
    '1758' : True,
    '1632' : True,
    '1760' : True,
    '1759' : True,
    '1633' : True,
    '1634' : True,
    '1635' : True,
    '1636' : True,
    '1637' : True,
    '1638' : True,
    '1639' : True,
    '1640' : True,
    '1641' : True,
    '1569' : True,
    '1649' : True,
    '1575' : True,
    '1573' : True,
    '1571' : True,
    '1570' : True,
    '1576' : True,
    '1577' : True,
    '1578' : True,
    '1579' : True,
    '1580' : True,
    '1581' : True,
    '1582' : True,
    '1583' : True,
    '1584' : True,
    '1585' : True,
    '1586' : True,
    '1587' : True,
    '1588' : True,
    '1589' : True,
    '1750' : True,
    '1590' : True,
    '1591' : True,
    '1592' : True,
    '1593' : True,
    '1594' : True,
    '1601' : True,
    '1602' : True,
    '1751' : True,
    '1603' : True,
    '1604' : True,
    '1605' : True,
    '1606' : True,
    '1607' : True,
    '1608' : True,
    '1572' : True,
    '1609' : True,
    '1610' : True,
    '1574' : True,
}

MINIMAL = {
    '1600' : False,
    '32' : False,
    '1772' : False,
    '1612' : False,
    '1613' : False,
    '1614' : True,
    '1615' : True,
    '1616' : True,
    '1617' : True,
    '1648' : True,
    '1755' : False,
    '1771' : False,
    '1765' : False,
    '1753' : False,
    '1766' : False,
    '1761' : False,
    '1754' : False,
    '1756' : False,
    '1770' : False,
    '1763' : False,
    '1752' : False,
    '1620' : False,
    '1767' : False,
    '1619' : False,
    '1768' : False,
    '1773' : False,
    '1762' : False,
    '1611' : False,
    '1618' : True,
    '1757' : True,
    '1769' : True,
    '1758' : True,
    '1632' : True,
    '1760' : True,
    '1759' : True,
    '1633' : True,
    '1634' : True,
    '1635' : True,
    '1636' : True,
    '1637' : True,
    '1638' : True,
    '1639' : True,
    '1640' : True,
    '1641' : True,
    '1569' : True,
    '1649' : True,
    '1575' : True,
    '1573' : True,
    '1571' : True,
    '1570' : True,
    '1576' : True,
    '1577' : True,
    '1578' : True,
    '1579' : True,
    '1580' : True,
    '1581' : True,
    '1582' : True,
    '1583' : True,
    '1584' : True,
    '1585' : True,
    '1586' : True,
    '1587' : True,
    '1588' : True,
    '1589' : True,
    '1750' : True,
    '1590' : True,
    '1591' : True,
    '1592' : True,
    '1593' : True,
    '1594' : True,
    '1601' : True,
    '1602' : True,
    '1751' : True,
    '1603' : True,
    '1604' : True,
    '1605' : True,
    '1606' : True,
    '1607' : True,
    '1608' : True,
    '1572' : True,
    '1609' : True,
    '1610' : True,
    '1574' : True,
}


CLEAN = {
    '1600' : False,
    '32' : True,
    '1772' : False,
    '1612' : False,
    '1613' : False,
    '1614' : False,
    '1615' : False,
    '1616' : False,
    '1617' : False,
    '1648' : False,
    '1755' : False,
    '1771' : False,
    '1765' : False,
    '1753' : False,
    '1766' : False,
    '1761' : False,
    '1754' : False,
    '1756' : False,
    '1770' : False,
    '1763' : False,
    '1752' : False,
    '1620' : False,
    '1767' : False,
    '1619' : False,
    '1768' : False,
    '1773' : False,
    '1762' : False,
    '1611' : False,
    '1618' : True,
    '1757' : True,
    '1769' : True,
    '1758' : True,
    '1632' : True,
    '1760' : True,
    '1759' : True,
    '1633' : True,
    '1634' : True,
    '1635' : True,
    '1636' : True,
    '1637' : True,
    '1638' : True,
    '1639' : True,
    '1640' : True,
    '1641' : True,
    '1569' : True,
    '1649' : True,
    '1575' : True,
    '1573' : True,
    '1571' : True,
    '1570' : True,
    '1576' : True,
    '1577' : True,
    '1578' : True,
    '1579' : True,
    '1580' : True,
    '1581' : True,
    '1582' : True,
    '1583' : True,
    '1584' : True,
    '1585' : True,
    '1586' : True,
    '1587' : True,
    '1588' : True,
    '1589' : True,
    '1750' : True,
    '1590' : True,
    '1591' : True,
    '1592' : True,
    '1593' : True,
    '1594' : True,
    '1601' : True,
    '1602' : True,
    '1751' : True,
    '1603' : True,
    '1604' : True,
    '1605' : True,
    '1606' : True,
    '1607' : True,
    '1608' : True,
    '1572' : True,
    '1609' : True,
    '1610' : True,
    '1574' : True,
}

CHAR = [
    32,
    1569,
    1570,
    1571,
    1572,
    1573,
    1574,
    1575,
    1576,
    1577,
    1578,
    1579,
    1580,
    1581,
    1582,
    1583,
    1584,
    1585,
    1586,
    1587,
    1588,
    1589,
    1590,
    1591,
    1592,
    1593,
    1594,
    1600,
    1601,
    1602,
    1603,
    1604,
    1605,
    1606,
    1607,
    1608,
    1609,
    1610,
    1611,
    1612,
    1613,
    1614,
    1615,
    1616,
    1617,
    1618,
    1619,
    1620,
    1632,
    1633,
    1634,
    1635,
    1636,
    1637,
    1638,
    1639,
    1640,
    1641,
    1648,
    1649,
    1750,
    1751,
    1752,
    1753,
    1754,
    1755,
    1756,
    1757,
    1758,
    1759,
    1760,
    1761,
    1762,
    1763,
    1765,
    1766,
    1767,
    1768,
    1769,
    1770,
    1771,
    1772,
    1773,
]
