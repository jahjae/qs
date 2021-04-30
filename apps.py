from init import *

def Nimu(q, u, index):
    u.style('header', {'position': 'sticky', 'top': '0', 'padding': '5px 0 0 0'})
    u.style('a', {'text-decoration': 'none'})
    u.props['menu'] = 0

    u.render('<header><a href="/nimu">'+'>'+'</a>'+' '+HUBO[u.props['hubo']].upper()+'</header>')

    if u.props['hubo'] == len(HUBO)-1:
        u.props['hubo'] = 0
    else:
        u.props['hubo'] = u.props['hubo'] + 1
