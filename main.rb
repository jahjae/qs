require 'socket'

require_relative './lib/data.rb'
require_relative './lib/apps.rb'
require_relative './lib/nets.rb'

def main
    status = '200 OK'
    headers = [('Content-type': 'text/html; charset=utf-8')]
    start_response(status, headers)

    u.component = []
    u.render('<!DOCTYPE html>')
    u.render('<html lang="EN">')
    u.render('<head>')
    u.render('<title>'+u.props[:title]+'</title>')
    u.render('<meta charset="UTF-8" name="viewport" content="width=device-width, initial-scale=1.0">')
    u.render('<link rel="preconnect" href="https://fonts.gstatic.com"><link href="https://fonts.googleapis.com/css2?family=Scheherazade New&display=swap" rel="stylesheet">')
    u.render('</head>')
    u.render('<body style="margin: 20px; font-family: '+ u.props[:font]+ ';">')
    
    noPage = '1'
    exec(ADDRESS[path]+'(q, u, noPage)')

    u.render('</body></html>')
    body = ''.join(u.component)
    return [body.encode('utf-8')]

end

u = Ui.new # User Interface

    # set property
u.props[:mode] = 0 #   0: Pages, 1:Row 2: Juz, 3: Sura, 4: Ayat
u.props[:view] = 0 # 0: Show All, 1: Hide All 2: First Only
u.props[:index] = 1
u.props[:print] = 0 # 1 = True, 0 = False
u.props[:mushaf] = 0 # 1 = True, 0 = False
u.props[:tafsir] = 0 # 1 = True,
u.props[:word] = 0 # 1 = True, 0 = False
u.props[:font] = FONTS[0]
u.props[:fontsize] = 1
u.props[:arabicfont] = 1
u.props[:arabicfontsize] = 2
u.props[:theme] = 0
u.props[:color] = 1
u.props[:nimu] = 0
u.props[:menu] = 0
u.props[:highlight] = [1618, 1648]
u.props[:match] = 0 # 0 = None, 1 = Ayah, 2 = Kata
u.props[:backgroundcolor] = COLOR[0][0]
u.props[:firstwordcolor] = COLOR[0][1]
u.props[:arabicfontcolor] = COLOR[0][2]
u.props[:fontcolor] = COLOR[0][3]
u.props[:selected] = MODET[u.props['mode']]

u.style('a', {'text-decoration': 'none'})

q = Quran.new 

while client = server.accept
  request = client.gets
  client.close
end
