from wsgiref.simple_server import make_server
from multiprocessing import *
from core import *
from init import *
from ui import *
from qs import *

import sys
import urllib.request
import random

def main(environ, start_response):
    status = '200 OK'
    headers = [('Content-type', 'text/html; charset=utf-8')]
    start_response(status, headers)

    u.component = []
    u.render('<!DOCTYPE html>')
    u.render('<html>')
    u.render('<head>')
    u.render('<meta name="viewport" content="width=device-width, initial-scale=1.0">')
    u.render('<link rel="preconnect" href="https://fonts.gstatic.com">')
    u.render('<link href="https://fonts.googleapis.com/css2?family=Scheherazade&display=swap" rel="stylesheet">')
    u.render('</head>')
    u.render('<body style="padding: 0px; font-family: '+ u.props['arabicfont']+ ';">')
    u.render('</body>')

    error = True
    path = environ['PATH_INFO']


    if path in ADDRESS:
        error = False
        noPage = u.props['index']
        exec(ADDRESS[path[0]]+'(u, noPage)')

    if len(path) == 2:
        if path[1] in NUMBER:
            error = False
            noPage = path[1]
            exec(ADDRESS[path[0]]+'(u, noPage)')

    if len(path) == 3:
        if path[2] in NUMBER:
            error = False
            noPage = path[1:3]
            exec(ADDRESS[path[0]]+'(u, noPage)')

    if len(path) == 4:
        if path[3] in NUMBER:
            error = False
            noPage = path[1:4]
            exec(ADDRESS[path[0]]+'(u, noPage)')

    print(u.artikata)

    if error:
        u.render('Invalid')

    u.render('</html>')
    body = ''.join(u.component)
    return [body.encode('utf-8')]

if __name__ == "__main__":
    u = C() # User Interface
    u.props = {
        'mode'              : 0,        #0: Pages, 1:Row 2: Juz, 3: Sura, 4: Ayat
        'view'              : 0,        #0: Show All, 1: Hide All, 2, firstword
        'arabic'            : True,
        'tafsir'            : True,
        'translation'       : True,
        'word'              : True,
        'tajweed'           : False,
        'random'            : False,
        'print'             : False,
        'medina'            : False,   #True: Usmani, False: Medina
        'firstword'         : True,
        'firstwordcolor'    : '#BDB76B',
        'align'             : 'right',
        'arabicfont'        : 'Scheherazade',
        'arabicfontcolor'   : '#000000',
        'arabicfontsize'    : '50px',
        'tafsirfontsize'    : '20px',
        'index'              : '1',
    }

    http1 = make_server('', 8000, main)
    print("PORT:8000 per halaman mode " + str(u.props['view']) )
    http1.serve_forever()
