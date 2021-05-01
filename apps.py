from init import *

def Dan(q, u, index):
    u.style('header', {'position': 'sticky', 'top': '0', 'padding': '5px 0 0 0'})
    u.style('a', {'text-decoration': 'none'})

    u.render('<header><a href="/nimu">'+'>'+'</a></header>')

def Nimu(q, u, index):
    u.style('header', {'position': 'sticky', 'top': '0', 'padding': '5px 0 0 0'})
    u.style('a', {'text-decoration': 'none'})

    if u.props['nimu'] == 1:
        u.props['nimu'] = 0

        noPage = str(u.props['index'])
        exec(ADDRESS['/dan']+'(q, u, noPage)')
    else:
        u.props['nimu'] = 1
        module(q, u, index)

def module(q, u, index):
    u.style('header', {'position': 'sticky', 'top': '0', 'padding': '5px 0 0 0'})
    u.style('a', {'text-decoration': 'none'})

    u.render('<header><a href="/nimu">'+'>'+'</a></header>')

    u.render('<p><a href="/role">ROLE</a></p>')
    u.render('<p><a href="/item">OBJECT</a></p>')
    u.render('<p><a href="/action">ACTION</a></p>')
    u.render('<p><a href="/menu">QURAN</a></p>')


def Role(q, u, index):
    u.style('header', {'position': 'sticky', 'top': '0', 'padding': '5px 0 0 0'})
    u.style('a', {'text-decoration': 'none'})

    u.render('<header><a href="/nimu">'+'>'+'</a></header>')

def Item(q, u, index):
    u.style('header', {'position': 'sticky', 'top': '0', 'padding': '5px 0 0 0'})
    u.style('a', {'text-decoration': 'none'})

    u.render('<header><a href="/nimu">'+'>'+'</a></header>')

def Action(q, u, index):
    u.style('header', {'position': 'sticky', 'top': '0', 'padding': '5px 0 0 0'})
    u.style('a', {'text-decoration': 'none'})

    u.render('<header><a href="/nimu">'+'>'+'</a></header>')
