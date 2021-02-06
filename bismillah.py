from wsgiref.simple_server import make_server
from multiprocessing import *
from core import *
from init import *

import sys

def main(environ, start_response):
    status = '200 OK'
    headers = [('Content-type', 'text/html; charset=utf-8')]
    start_response(status, headers)

    Kata = []
    Kata.append('<!DOCTYPE html>')
    Kata.append('<html>')
    Kata.append('<head>')
    Kata.append('<meta name="viewport" content="width=device-width, initial-scale=1.0">')
    Kata.append('<link rel="preconnect" href="https://fonts.gstatic.com">')
    Kata.append('<link href="https://fonts.googleapis.com/css2?family=Scheherazade&display=swap" rel="stylesheet">')
    Kata.append('</head>')
    Kata.append('<body style="padding: 0px; font-size: 200%; font-family: Scheherazade">')
    Kata.append('</body>')

    error = True
    path = environ['PATH_INFO']

    if path in ADDRESS:
        error = False
        exec(ADDRESS[path[0]]+'(Kata, VIEW, "1")')

    if len(path) == 2:
        if path[1] in NUMBER:
            error = False
            noPage = path[1:2]
            exec(ADDRESS[path[0]]+'(Kata, VIEW, noPage)')

    if len(path) == 3:
        if path[2] in NUMBER:
            error = False
            noPage = path[1:3]
            exec(ADDRESS[path[0]]+'(Kata, VIEW, noPage)')

    if len(path) == 4:
        if path[3] in NUMBER:
            error = False
            noPage = path[1:4]
            exec(ADDRESS[path[0]]+'(Kata, VIEW, noPage)')

    if error == 1:
        Kata.append('Invalid address')

    Kata.append('</html>')
    body = ''.join(Kata)
    return [body.encode('utf-8')]


if __name__ == "__main__":
    http1 = make_server('', 8000, main)
    print("PORT:8000 is serving ...")
    http1.serve_forever()
