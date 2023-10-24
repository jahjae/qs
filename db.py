from wsgiref.simple_server import make_server
from multiprocessing import *

import logging
import os

from lib.data import *
from lib.apps import *
from lib.nets import *

from lib.init import *

format = "%(asctime)s: %(message)s"
logging.basicConfig(format=format, level=logging.INFO,datefmt="%H:%M:%S")


def maindb(environ, start_response):
    status = '200 OK'
    headers = [('Content-type', 'text/html; charset=utf-8')]
    start_response(status, headers)
    u.component = []

    u.render('<!DOCTYPE html>')
    u.render('<html lang="EN">')
    u.render('<head>')
    u.render('<title>'+u.props['title']+'</title>')
    u.render('<meta charset="UTF-8" name="viewport" content="width=device-width, initial-scale=1.0">')
    u.render('<link rel="preconnect" href="https://fonts.gstatic.com"><link href="https://fonts.googleapis.com/css2?family=Lateef&family=Scheherazade New&display=swap" rel="stylesheet">')
    u.render('</head>')
    u.render('<body style="margin: 20px; font-family: '+ u.props['font']+ ';">')
    u.render('</body></html>')
    body = ''.join(u.component)
    return [body.encode('utf-8')]

if __name__ == "__main__":
    u = C()
    q = Q() # Quran

    q.loadData()
    print(q.tafsir[1])
    print(q.juz[1])
    print(q.surat[1])
    print(q.halaman[1])
    print(q.codehuruf[1763])
    print(q.artiayat[1])
    print(q.artikata[1])
    print(q.codekata[92])
    print(q.huruf[1763])

    httpd = make_server('', 8001,maindb)
    httpd.serve_forever()
