from wsgiref.simple_server import make_server
from multiprocessing import *
from core import *
from init import *
from ui import *

import sys
import urllib.request

def main(environ, start_response):
    status = '200 OK'
    headers = [('Content-type', 'text/html; charset=utf-8')]
    start_response(status, headers)

    u = C()
    u.props = {
        'view'              : 0,
        'arabic'            : True,
        'tafsir'            : False,
        'translation'       : False,
        'word'              : False,
        'tajweed'           : False,
        'random'            : False,
        'print'             : False,
        'mushaf'            : False,
        'firstword'         : True,
        'firstwordcolor'    : '#000000',
        'align'             : 'right',
        'arabicfont'        : 'Scheherazade',
        'arabicfontcolor'   : '#000000',
        'arabicfontsize'    : '30px',
        'tafsirfontsize'    : '20px',
    }

    u.render('<!DOCTYPE html>')
    u.render('<html>')
    u.render('<head>')
    u.render('<meta name="viewport" content="width=device-width, initial-scale=1.0">')
    u.render('<link rel="preconnect" href="https://fonts.gstatic.com">')
    u.render('<link href="https://fonts.googleapis.com/css2?family=Scheherazade&display=swap" rel="stylesheet">')
    u.render('</head>')
    u.render('<body style="padding: 0px; font-size: 200%; font-family: Scheherazade">')
    u.render('</body>')

    error = True
    path = environ['PATH_INFO']

    print(u.props)
    if path in ADDRESS:
        error = False
        exec(ADDRESS[path[0]]+'(u, "1")')

    if len(path) == 2:
        if path[1] in NUMBER:
            error = False
            noPage = path[1:2]
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


    if error:
        u.render('Invalid')

    u.render('</html>')
    body = ''.join(u.component)
    return [body.encode('utf-8')]

if __name__ == "__main__":
    q = Q()
    http1 = make_server('', 8000, main)
    print("PORT:8000 per halaman per ayat ...")
    http1.serve_forever()
