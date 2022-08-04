require 'socket'

require_relative './lib/data.rb'
require_relative './lib/apps.rb'
require_relative './lib/nets.rb'
require_relative './lib/init.rb'

server = TCPServer.new 8000

def start q, u, m
  
  u.component = []
  u.render '<!DOCTYPE html>'
  u.render '<html lang="EN">'
  u.render '<head>'
  u.render "<title>#{u.props[:title]}</title>"
  u.render '<meta charset="UTF-8" name="viewport" content="width=device-width, initial-scale=1.0">'
  u.render '</head>'
  u.render '<body style="margin: 20px">'

  done = FALSE
  begin
    m.surah q, u
    done = TRUE
  rescue
    if not done
      puts "#{Time.now} invalid address"
    end
  end
  u.render '</body></html>'
  body = u.component.join ' '

  return body
end

m = Mushaf.new
u = Ui.new
q = Quran.new

u.props[:title] = 'Alquran'

loop {
  Thread.start server.accept do | client |
    req = client.gets
    puts "#{Time.now} #{client}"
  
    client.print "HTTP/1.1 200\r\n"
    client.print "Content-Type: text/html\r\n"
    client.print "\r\n"
    
    body = start q, u, m
    client.print body
    client.close
  end
}
