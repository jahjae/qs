from wsgiref.simple_server import make_server
from multiprocessing import *

from core import *
from init import *

from ui import *
from qs import *

import sys
import os
import urllib.request
import random

def main(environ, start_response):
    status = '200 OK'
    headers = [('Content-type', 'text/html; charset=utf-8')]
    start_response(status, headers)

    u.component = []
    u.render('<!DOCTYPE html>')
    u.render('<html lang="EN">')
    u.render('<head>')
    u.render('<meta charset="UTF-8" name="viewport" content="width=device-width, initial-scale=1.0">')
    u.render('<title>'+u.props['title']+'</title>')
    u.render('<style>@import url("https://fonts.googleapis.com/css2?family=Amiri&family=Harmattan&family=Lateef&family=Montserrat&family=Open+Sans&family=Scheherazade&display=swap");</style>')
    u.render('</head>')
    u.render('<body style="font-family: '+ u.props['font']+ ';">')

    error = True
    path = environ['PATH_INFO']

    if path in ADDRESS:
        error = False
        noPage = str(u.props['index'])
        exec(ADDRESS[path]+'(q, u, noPage)')

    if len(path) == 2:
        if path[1] in NUMBER:
            error = False
            noPage = path[1]
            exec(ADDRESS[path[0]]+'(q, u, noPage)')

    if len(path) == 3:
        if path[2] in NUMBER:
            error = False
            noPage = path[1:3]
            exec(ADDRESS[path[0]]+'(q, u, noPage)')

    if len(path) == 4:
        if path[3] in NUMBER:
            error = False
            noPage = path[1:4]
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
    print('Generating Data Lake ...')
    q = Q() # Quran


    #   0: Pages, 1:Row 2: Juz, 3: Sura, 4: Ayat
    u.props['mode'] = 0
    u.props['view'] = 0
    u.props['index'] = 1
    u.props['print'] = 0 # 1 = True, 0 = False
    u.props['selected'] = MODET[u.props['mode']]

    u.props['mushaf'] = 0 # 1 = True, 0 = False
    u.props['tafsir'] = 0 # 1 = True,
    u.props['word'] = 0 # 1 = True, 0 = False

    u.props['theme'] = 0
    u.props['menu'] = 0
    u.props['backgroundcolor'] = COLOR[0][0]
    u.props['firstwordcolor'] = COLOR[0][1]
    u.props['arabicfontcolor'] = COLOR[0][2]
    u.props['fontcolor'] = COLOR[0][3]

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


    http1 = make_server('', 8000, main)
    print("Serving ..."  )
    http1.serve_forever()
