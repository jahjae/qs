from wsgiref.simple_server import make_server
from multiprocessing import *
import sys
import os
import urllib.request
import random

from core import *
from init import *
from ui import *
from qs import *


def main(environ, start_response):
    status = '200 OK'
    headers = [('Content-type', 'text/html; charset=utf-8')]
    start_response(status, headers)

    u.component = []
    u.render('<!DOCTYPE html>')
    u.render('<html lang="EN">')
    u.render('<head>')
    u.render('<title>'+u.props['title']+'</title>')
    u.render('<meta charset="UTF-8" name="viewport" content="width=device-width, initial-scale=1.0">')
    u.render('<style>@import url("https://fonts.googleapis.com/css2?family=Harmattan:wght@400;700&family=Lateef&family=Amiri&family=Montserrat&family=Open+Sans&family=Scheherazade:wght@400;700&display=swap");</style>')
    u.render('<link rel="stylesheet" href="https://fonts.googleapis.com/icon?family=Material+Icons">')
    u.render('</head>')
    u.render('<body style="font-family: '+ u.props['font']+ ';">')

    error = True
    path = environ['PATH_INFO']

    if path in ADDRESS:
        error = False
        u.props['index'] = int(os.environ['INDEX'])
        noPage = str(u.props['index'])
        exec(ADDRESS[path]+'(q, u, noPage)')

    if len(path) == 2:
        if path[1] in NUMBER:
            error = False
            noPage = path[1]
            u.props['index'] = int(noPage)
            os.environ['INDEX'] = str(u.props['index'])
            exec(ADDRESS[path[0]]+'(q, u, noPage)')

    if len(path) == 3:
        if path[2] in NUMBER:
            error = False
            noPage = path[1:3]
            u.props['index'] = int(noPage)
            os.environ['INDEX'] = str(u.props['index'])

            exec(ADDRESS[path[0]]+'(q, u, noPage)')

    if len(path) == 4:
        if path[3] in NUMBER:
            error = False
            noPage = path[1:4]
            u.props['index'] = int(noPage)
            os.environ['INDEX'] = str(u.props['index'])

            exec(ADDRESS[path[0]]+'(q, u, noPage)')

    if error:
        noPage = str(u.props['index'])
        exec(ADDRESS['/']+'(q, u, noPage)')

    u.render('</body></html>')
    body = ''.join(u.component)
    return [body.encode('utf-8')]


if __name__ == "__main__":
    u = C() # User Interface
    print('Loading Data Source ...')


    #   0: Pages, 1:Row 2: Juz, 3: Sura, 4: Ayat
    u.props['mode'] = 0
    u.props['view'] = 0
    u.props['index'] = 1
    u.props['print'] = 0 # 1 = True, 0 = False

    u.props['mushaf'] = 0 # 1 = True, 0 = False
    u.props['tafsir'] = 0 # 1 = True,
    u.props['word'] = 0 # 1 = True, 0 = False
    u.props['font'] = 'Harmattan'
    u.props['fontsize'] = 1
    u.props['arabicfont'] = 'Scheherazade'
    u.props['arabicfontsize'] = 2

    u.props['theme'] = 0
    u.props['menu'] = 0
    u.props['backgroundcolor'] = COLOR[0][0]
    u.props['firstwordcolor'] = COLOR[0][1]
    u.props['arabicfontcolor'] = COLOR[0][2]
    u.props['fontcolor'] = COLOR[0][3]

    os.environ['ARABICFONT'] = str(u.props['arabicfont'])
    os.environ['ARABICFONTSIZE'] = str(u.props['arabicfontsize'])
    os.environ['FONT'] = str(u.props['font'])
    os.environ['FONTSIZE'] = str(u.props['fontsize'])

    os.environ['MODE'] = str(u.props['mode'])
    os.environ['VIEW'] = str(u.props['view'])
    os.environ['INDEX'] = str(u.props['index'])
    os.environ['MUSHAF'] = str(u.props['mushaf'])
    os.environ['WORD'] = str(u.props['word'])
    os.environ['TAFSIR'] = str(u.props['tafsir'])
    os.environ['PRINT'] = str(u.props['print'])
    os.environ['FIRSTWORD'] = str(u.props['firstword'])
    os.environ['BACKGROUNDCOLOR'] = u.props['backgroundcolor']
    os.environ['FIRSTWORDCOLOR'] = u.props['firstwordcolor']
    os.environ['ARABICFONTCOLOR'] = u.props['arabicfontcolor']
    os.environ['FONTCOLOR'] = u.props['fontcolor']

    u.props['selected'] = MODET[u.props['mode']]

    print('Generating Data Lake ...')
    q = Q() # Quran

    u.style('a', {'text-decoration': 'none'})

    http1 = make_server('', 8000, main)
    print("Serving ..."  )
    http1.serve_forever()
