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
    u.props['index'] = int(os.environ.get('INDEX'))

    if path in ADDRESS:
        error = False
        noPage = str(u.props['index'])
        exec(ADDRESS[path[0]]+'(q, u, noPage)')

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
        u.render('Invalid')

    print(u.props)
    u.render('</html>')
    body = ''.join(u.component)
    return [body.encode('utf-8')]

if __name__ == "__main__":
    u = C() # User Interface
    print('Loading ...')

    #   0: Pages, 1:Row 2: Juz, 3: Sura, 4: Ayat
    u.props['mode'] = '3'
    u.props['view'] = '0'
    u.props['index'] = '1'

    os.environ['MODE'] = u.props['mode']
    os.environ['VIEW'] = u.props['view']
    os.environ['INDEX'] = u.props['index']

    q = Q()

    http1 = make_server('', 8000, main)
    print("Serving ..."  )
    http1.serve_forever()
