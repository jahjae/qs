require 'socket'

require_relative './lib/data.rb'
require_relative './lib/apps.rb'
require_relative './lib/nets.rb'
require_relative './lib/init.rb'

q = Quran.new
u = Ui.new

server = TCPServer.new 8000

def main q, u, path
    u.component = []
    u.render('<!DOCTYPE html>')
    u.render('<html lang="EN">')
    u.render('<head>')
    u.render "<title>#{u.props[:title]}</title>"
    u.render('<meta charset="UTF-8" name="viewport" content="width=device-width, initial-scale=1.0">')
    u.render('<link rel="preconnect" href="https://fonts.gstatic.com">')
    u.render('<link href="https://fonts.googleapis.com/css2?family=Scheherazade New&display=swap" rel="stylesheet">')
    u.render('</head>')
    u.render "<body style='margin: 20px; font-family: #{FONTS[1]};'>"
    
    index = u.props[:index] 
    quranHuruf q, u, index

    u.render('</body></html>')
    body = u.component.join ' '

    return body
end

u.props[:mode] = 2 #   0: Pages, 1:Row 2: Juz, 3: Sura, 4: Ayat
u.props[:view] = 0 # 0: Show All, 1: Hide All 2: First Only
u.props[:index] = 2
u.props[:print] = FALSE # 1 = True, 0 = False
u.props[:mushaf] = FALSE # 1 = True, 0 = False
u.props[:tafsir] = FALSE # 1 = True,
u.props[:word] = FALSE # 1 = True, 0 = False
u.props[:font] = FONTS[1]
u.props[:fontsize] = 1
u.props[:arabicfont] = 1
u.props[:arabicfontsize] = 2
u.props[:theme] = 0
u.props[:color] = 1
u.props[:title] = 'Alquran'

u.props[:nimu] = 0
u.props[:menu] = 0
u.props[:highlight] = [1618, 1648]
u.props[:match] = 0 # 0 = None, 1 = Ayah, 2 = Kata
u.props[:backgroundcolor] = COLOR[0][0]
u.props[:firstwordcolor] = COLOR[0][1]
u.props[:arabicfontcolor] = COLOR[0][2]
u.props[:fontcolor] = COLOR[0][3]
u.props[:selected] = MODET[0]

u.style 'a', {'text-decoration': 'none'}

loop {
  Thread.start server.accept do | client |
    request = client.gets
    method, path = request.split ' '

    client.print "HTTP/1.1 200\r\n"
    client.print "Content-Type: text/html\r\n"
    client.set_encoding 'UTF-8'
    client.print "\r\n"
    
    body = main q, u, '/'

    client.print body
    client.close
  end
}
