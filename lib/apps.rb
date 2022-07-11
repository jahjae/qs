require_relative 'init.rb'

def textFormat q, u, index
    u.style('header', {'position': 'sticky', 'top': '0'})
    u.style('a', {'text-decoration': 'none'})
    u.props[:menu] = 0

    u.props[:text] += 1

    if u.props[:text] == FORMAT.lenght
        u.props[:text] = 0
    end

    noPage = u.props[:index]
    exec(ADDRESS['/']+'(q, u, noPage)')
end

def number q, u, index

    u.style('a', {'text-decoration': 'none'})
    u.props['menu'] = 0
    u.header('<a href="/menu">'+'>'+'</a>')
    u.style('p.surat', {'font-size': TSIZET[u.props['fontsize']],
        'text-align': 'left','line-height': '1',})
    u.style('p.ayat', {'font-size': TSIZET[u.props['fontsize']],
        'text-align': 'right', 'line-height': '1',})


    if u.props[:mode] == 4
        for x in q.surat do
            u.render('<p class="surat"><a href="/'+str(x)+'">'+str(x)+'</a>'+q.surat[x][1]+', '+q.surat[x][0]+', '+q.surat[x][2]+', '+q.surat[x][4]+'</p>')
            u.render('<p class="ayat">')
            # quranAyat(q, u, str(x), str(0))
            u.render('</p>')
        end
    end

    if u.props[:mode] == 3
        for x in q.surat do
            u.render('<p class="surat"><a href="/'+str(x)+'">'+str(x)+'. </a>'+q.surat[x][1]+', '+q.surat[x][0]+', '+q.surat[x][2]+', '+q.surat[x][4]+'</p>')
            u.render('<p class="ayat">')
            #quranAyat q, u, str(x), str(0))
            u.render('</p>')
        end
    end

    if u.props[:mode] == 2
      u.style('p.surat', {'font-size': TSIZET[u.props['fontsize']],'text-align': 'left', 'line-height': '1',})
      u.style('p.ayat', {'font-size': TSIZET[u.props['fontsize']],'text-align': 'right', 'line-height': '1',})

        for x in q.juz do
          u.render("<p><a href='/#{x.to_s}'>#{x}</a>#{q.surat[int(q.juz[x][:surat])][1]} / #{q.juz[x][:ayat]} </p>")
            u.render('<p class="ayat">')
            #quranAyat(q, u, q.juz[x]['surat'], q.juz[x]['ayat'])
            u.render('</p>')
        end
    end

    if u.props[:mode] == 0
        for x in q.halaman do
          u.render "<p><a href='/#{x}'>#{x}</a> #{q.surat[q.halaman[x][:surat]][1]} / #{q.halaman[x][:ayat]} </p>"
        end
    end
end

def quranAyat q, u, s, a
    reset = TRUE
    puts 'Quran Ayat'

    q.kata do |x|
      if x[3].to_i == s.to_i
        if x[4].to_i == a.to_i
    
                    
          u.props[:page]     = x[0].to_i
          u.props[:row]      = x[1].to_i
          u.props[:juz]      = x[2].to_i
          u.props[:surat]    = x[3].to_i
          u.props[:ayat]     = x[4].to_i
          
          if reset
            reset = FALSE
                    
            halamanSebelum = x[0].to_i
            barisSebelum = x[1].to_i
            juzSebelum = x[2].to_i
            suratSebelum = x[3].to_i
            ayatSebelum = x[4].to_i
            kataSebelum = x[5].to_i
          end
          
          kataBerikut = q.compare x[5].to_i, kataSebelum
          
          if kataBerikut
            kataSebelum = x[5].to_i      
                q.spasi u
                
              end

              if u.props[:mushaf]
                u.props[:arabicfontsize] = 0
              end
          
              if u.props[:print]           
                q.mushafKata u, x[0].to_i, x[4].to_i, x[6].to_i
                
              else       
                quranKata q, u, a, x
                
              end
            end
        end
    end
end

def quranKata q, u, a, x
  total = x[7].to_i
  total.times do |y|
    pos = y + 8
    q.mushafHuruf u, x[pos]
  end
end

# /
def quranHuruf q, u, index
    puts 'Quran Huruf'

    u.style 'header', {'position': 'sticky', 'top': '0', 'padding': '5px 0 0 0'}
    u.style 'p.page', {'position': 'sticky', 'top': '0', 'padding': '10px 0 0 0'}

    u.style('a', {'text-decoration': 'none'})
    u.render('<meta charset="UTF-8" name="viewport" content="width=device-width, initial-scale=1.0">')

    u.props[:align] = 'right'
    u.style('body',{'background-color': u.props[:backgroundcolor]})

    if u.props[:mode] == 3
      u.render('<header><a href="/menu">'+'>'+'</a>'+' '+MODET[u.props[:mode]]+' '+u.props[:index].to_s+' / 114 - '+ q.surat[u.props[:index]][1] +'</header>')
    else
        if u.props[:mode] == 4
          u.header('<a href="/menu">'+'>'+'</a>'+' '+q.surat[u.props[:surat]][1]+' '+str(u.props[:surat])+':'+str(u.props[:ayat]))
        else
          u.header "#{MODET[u.props[:mode]]} #{index}"
        end
    end

    if u.props[:mushaf]
        u.props[:align] = 'center'
        u.props[:arabicfontsize] = 0
        u.props[:tafsir] = FALSE
    end

    if u.props[:view] == 1
        u.props[:firstword] = 0
    end
    reset = TRUE
  
    u.render('<div class="m" style="width: 100%;">')
    q.barisBaru u 

    for x in q.kata do
        modeon = FALSE

        # 
        if x[u.props[:mode]].to_i == index.to_i
          modeon = TRUE
        else
          modeon = FALSE
        end

        if modeon
          u.props[:page] = x[0].to_i
          u.props[:row] = x[1].to_i
          u.props[:juz] = x[2].to_i
          u.props[:surat] = x[3].to_i
          u.props[:ayat] = x[4].to_i
          
          if reset
            reset = FALSE
                
            halamanSebelum = x[0].to_i
            barisSebelum = x[1].to_i
            juzSebelum = x[2].to_i
            suratSebelum = x[3].to_i
            ayatSebelum = x[4].to_i
            kataSebelum = x[5].to_i
          end

            
          halamanBerikut = q.compare x[0].to_i, halamanSebelum
          barisBerikut = q.compare x[1].to_i, barisSebelum
          juzBerikut = q.compare x[2].to_i, juzSebelum
          suratBerikut = q.compare x[3].to_i, suratSebelum
          ayatBerikut = q.compare x[4].to_i, ayatSebelum
          kataBerikut = q.compare x[5].to_i, kataSebelum
          
          if barisBerikut
            if u.props[:mushaf]
              q.barisBaru u
            else
              if x[4].to_i == 0
                q.barisBaru u
              end
            end
            
            barisSebelum = x[1].to_i
          end
          
          if ayatBerikut
                if not u.props[:mushaf]
                    if u.props[:tafsir] and ayatSebelum  != 0
                        q.artiBaru u
                        q.artiAyat u, suratSebelum, ayatSebelum
                    end
                    if not halamanBerikut
                        q.barisBaru u
                    end
                end

                if halamanBerikut
                  halamanSebelum = x[0].to_i
                  q.barisBaru u
                  
                  
                  u.style("m", {'align': "center"})
                  u.render('<p class="page"></p>')
                  u.render('<div style="border-bottom: 10px solid #dddddd"></div>')
                  u.render "<p class='page'>PAGE: #{halamanSebelum.to_s}</p>"
                end

                ayatSebelum = x[4].to_i
                kataSebelum = 0

          end

            if suratBerikut
              suratSebelum = x[3].to_i
                ayatSebelum = 0
                kataSebelum = 0
            end

#           adding space before next word
            if kataBerikut
                q.spasi u
                if not u.props[:mushaf]
                    if u.props[:word] and ayatSebelum != 0 and kataSebelum != 0
                        if u.props[:tafsir]
                            q.kataBaru u
                            q.artiKata u, suratSebelum, ayatSebelum, kataSebelum
                            q.kataBaru u
                        end
                        q.barisBaru u
                    end
                end
                kataSebelum = x[5].to_i
            end
            # use font QCF
            if u.props[:print]
                # component, halaman, ayat, unicode kata
                if u.props[:mushaf]
                    u.props[:arabicfontsize] = 0
                end
                q.mushafKata u, x[0].to_i, x[4].to_i, x[6].to_i

            else
                q.spasi u

                if u.props[:mushaf]
                    u.props[:arabicfontsize] = 0
                end
                quranKata q, u, u.props[:ayat], x
            end
        end
    end

    if not u.props[:mushaf]
        if u.props[:tafsir] and ayatSebelum  != 0
            q.artiBaru(u)
            q.artiAyat(u, suratSebelum, ayatSebelum)
        end
    end
    u.render('</div>')
    u.style("m", {'align': "center"})

    return u
end

def daily q, u, index
    u.highlight '.d'
    u.style 'a', {'text-decoration': 'none'}
    u.props[:menu] = 1

    u.style 'a', {'font-size': TSIZET[1],'text-align': 'center','line-height': '1'}
    u.style 'p', {'font-size': TSIZET[1],'text-align': 'center','line-height': '1'}

    u.style 'body', {'background-color': u.props[:backgroundcolor]}

    s = rand 114
    if s == 0 
      s = 1
    end
  

    x = q.surat[s.to_i][0]
    a = rand x.to_i
    if a == 0
      a = 1 
    end
    

    u.header "<a href='/menu'>Daily</a>"
    u.p('')

    u.style 'ayat', {'font-family': "#{FONTS[1]}", 'text-align': 'center', 'font-size': "#{ASIZET[2]}"}
    u.render '<a class="ayat">' 
    
    quranAyat q, u, s, a
    u.render '</a>'
    
    u.style 'm', {'align': 'center', 'width': '100%',}

    u.props[:index] = s
    u.props[:mode] = 3


    u.style 'p', {'margin': '10px', 'font-size': "#{TSIZET[1]}",'text-align': 'center', 'line-height': '1'}
    u.render '<p>'
    u.render q.artiayat[s][a] 
    u.render '</p>'
    
    u.style 'p', {'font-size': "#{TSIZET[1]}",'text-align': 'center','line-height': '1.6'}
    u.render "<p>QS #{s}:#{a}</p>"
end

def index q, u, index
    logging.info('Indexing ...')
    u.style('a', {'text-decoration': 'none'})
    u.style('p', {'line-height': '0.5'})
    u.props['menu'] = 0

    u.render('<header><a href="/menu">'+'>'+'</a></header>')

    for x in q.indexkata
        u.p('<a href="/'+str(x)+'">'+str(x).upper()+'. </a>')
        u.p('')
        for y in q.indexkata[x] do
            u.p('QS '+y[1]+':'+y[2])
        end
        u.p('')
    end
end

def goto q, u, index
    u.style('a', {'text-decoration': 'none'})
    u.props['menu'] = 0

    if u.props['mode'] == 0
        u.props['page'] = u.props['page'] + 1
        if u.props['page'] == 605
            u.props['page'] = 1
        end
        u.props['index'] = u.props['page']
    end
    if u.props['mode'] == 1
        u.props['row'] = u.props['row'] + 1
        if u.props['row'] == q.surat[u.props['surat']][0]
            u.props['row'] = 1
        end
        u.props['index'] = u.props['row']
    end
    if u.props['mode'] == 2
        u.props['juz'] += 1
        if u.props['juz'] == 31
            u.props['juz'] = 1
        end
        u.props['index'] = u.props['juz']
    end
    if u.props['mode'] == 3
        u.props['surat'] += 1
        if u.props['surat'] == 115
            u.props['surat'] = 1
        end
        u.props['index'] = u.props['surat']
    end
    if u.props['mode'] == 4
        u.props['ayat'] += 1

        if u.props['ayat'] == int(q.surat[u.props['surat']][0]) + 1
            u.props['ayat'] = 1

            u.props['surat'] = u.props['surat'] + 1
            if u.props['surat'] == 115
                u.props['surat'] = 1
            end
        end

        u.props['index'] = u.props['ayat']
    end
    os.environ['INDEX'] = str(u.props['index'])

    noPage = str(u.props['index'])
    exec(ADDRESS['/']+'(q, u, noPage)')
end

def Search q,  u, index
    u.style('header', {'position': 'sticky', 'top': '0', 'padding': '5px 0 0 0'})
    u.style('a', {'text-decoration': 'none'})

    u.render('<header><a href="/menu">'+'>'+'</a></header>')
    u.render('<div style="width: 100%;">')

    u.props['arabicfont'] = int(os.environ.get('ARABICFONT'))

    q.huruf do |x|
        q.barisBaru(u)
        u.render('<a class ="d" style="text-align: center; font-size: 50vw; color: '+q.huruf[x]['color']+';font-family: '+ FONTS[u.props['arabicfont']]+';" href="/select/">' +chr(int(x))+ '</a>')
    end
    u.render('</div>')
end

def info q, u, index
    u.style('header', {'position': 'sticky', 'top': '0', 'padding': '5px 0 0 0'})
    u.style('p', {'font-size': TSIZET[1]})
    u.style('a', {'text-decoration': 'none'})

    u.render('<header><a href="/menu">'+'>'+'</a></header>')

    u.p('<a href="/daily">DAILY</a> > AYAT')

    if u.props['mode'] == 4
        u.render('<p> <a href="/mode">MODE</a> > ')
        u.render('<a href="/goto">'+MODET[u.props['mode']]+'</a> > '+str(u.props['surat'])+':'+str(u.props['ayat'])+'</p>')
    end
    if u.props['mode'] == 3
        u.render('<p> <a href="/mode">MODE</a> > ')
        u.render('<a href="/goto">'+MODET[u.props['mode']]+'</a> > <a href="/number">'+str(u.props['index'])+'</a> / 114 - '+q.surat[u.props['index']][1]+'</p>')
    end
    if u.props['mode'] == 2
        u.render('<p> <a href="/mode">MODE</a> > ')
        u.render('<a href="/goto">'+MODET[u.props['mode']] +'</a> > <a href="/number">'+str(u.props['index'])+'</a> / 30</p>')
    end
    if u.props['mode'] == 1
        u.render('<p> <a href="/mode">MODE</a> > ')
        u.render('<a href="/goto">'+MODET[u.props['mode']] +'</a> > '+str(u.props['index'])+' / '+u.quran[u.props['surat']][0]+'</p>')
    end
    if u.props['mode'] == 0
        u.render('<p> <a href="/mode">MODE</a> > ')
        u.render('<a href="/goto">'+MODET[u.props['mode']] +'</a> > <a href="/number">'+str(u.props['index'])+'</a> / 604</p>')
    end
    u.render('<p> <a href="/mushaf">MUSHAF</a>: '               +MUSHAFT[u.props['mushaf']]+'</p>')
    u.render('<p> <a href="/quran">READING</a>: '               +LOGICALT[u.props['print']] +'</p>')
    u.render('<p> <a href="/text">TEXT</a>: '                   +FORMAT[u.props['text']]+'</p>')
    u.render('<p> <a href="/view">VIEW</a>: '                   +VIEWT[u.props['view']] +'</p>')
    u.render('<p> <a href="/pertama">HIGHLIGH</a>: '            +HIGHLIGH[u.props['firstword']] +'</p>')
    u.p('<a href="/word">BY WORD</a>: '                         +LOGICALT[u.props['word']])
    u.render('<p> <a href="/translation">TRANSLATION</a>: '     +LOGICALT[u.props['tafsir']] +' / ')
    u.render('<a href="/fontsize">SIZE</a>: '                   +TSIZET[u.props['fontsize']]+'</p>')
    u.render('<p> <a href="/fontname">FONTS</a>: '              +FONTS[u.props['arabicfont']]+' / ')
    u.render('<a href="/arabicsize">SIZE</a>: '                 +ASIZET[u.props['arabicfontsize']]+'</p>')
    u.p('<a href="/index">INDEX</a>')
    u.p('<a href="/search">DICTIONARY</a>')
    u.p('<a href="/theme">THEME</a>: '                          +THEMET[u.props['theme']])
    u.p('<a href="/match">MATCH</a>: '                          +MATCHT[u.props['match']])
    u.p('<a href="/note">NOTE</a>')
end

def menu q, u, index
    u.style('header', {'position': 'sticky', 'top': '0', 'padding': '5px 0 0 0'})
    u.style('a', {'text-decoration': 'none'})

    os.environ['INDEX'] = str(u.props['index'])

    if u.props['menu'] == 1
        u.props['menu'] = 0

        noPage = str(u.props['index'])
        exec(ADDRESS['/']+'(q, u, noPage)')
    else
        u.props['menu'] = 1
        Info(q, u, index)
    end
end

def match q, u, index
    u.style 'header', {'position': 'sticky', 'top': '0', 'padding': '5px 0 0 0'}
    u.style 'a', {'text-decoration': 'none'}

    u.props['menu'] = 0

    if u.props['match'] == len(MATCHT)-1
        u.props['match'] = 0
    else
        u.props['match'] = u.props['match'] + 1
    end
    noPage = str(u.props['index'])
    exec(ADDRESS['/']+'(q, u, noPage)')
end

def mode q, u, index
    u.style('header', {'position': 'sticky', 'top': '0', 'padding': '5px 0 0 0'})
    u.style('a', {'text-decoration': 'none'})
    u.props['menu'] = 0

    if u.props['mode'] == len(MODET)-1
        u.props['mode'] = 0
    else
        u.props['mode'] = u.props['mode'] + 1
    end

    if u.props['mode'] == 1
        u.props['mode'] = 2
    end
    u.props['selected'] = MODET[u.props['mode']]

    if u.props['mode'] == 0
            u.props['index'] = u.props['page']
    end
    if u.props['mode'] == 1
            u.props['index'] = u.props['row']
    end
    if u.props['mode'] == 2
            u.props['index'] = u.props['juz']
    end
    if u.props['mode'] == 3
            u.props['index'] = u.props['surat']
    end
    if u.props['mode'] == 4
            u.props['ayat'] = 1
            u.props['index'] = u.props['ayat']
    end
    os.environ['MODE'] = str(u.props['mode'])
    os.environ['INDEX'] = str(u.props['index'])

    noPage = str(u.props['index'])
    exec(ADDRESS['/']+'(q, u, noPage)')
end

def Arabicsize q, u, index
    u.style('header', {'position': 'sticky', 'top': '0', 'padding': '5px 0 0 0'})
    u.style('a', {'text-decoration': 'none'})
    u.props['menu'] = 0

    u.props['arabicfontsize'] = u.props['arabicfontsize'] + 1

    if u.props['arabicfontsize'] == len(ASIZET)
        u.props['arabicfontsize'] = 1
    end
    os.environ['ARABICFONTSIZE'] = str(u.props['arabicfontsize'])
    os.environ['INDEX'] = str(u.props['index'])

    noPage = str(u.props['index'])
    exec(ADDRESS['/']+'(q, u, noPage)')
end

def Fontname q, u, index
    u.style('header', {'position': 'sticky', 'top': '0', 'padding': '5px 0 0 0'})
    u.style('a', {'text-decoration': 'none'})
    u.props['menu'] = 0

    u.props['arabicfont'] = u.props['arabicfont'] + 1

    if u.props['arabicfont'] == len(FONTS)
        u.props['arabicfont'] = 1
    end
   
    os.environ['ARABICFONT'] = str(u.props['arabicfont'])
    os.environ['INDEX'] = str(u.props['index'])

    noPage = str(u.props['index'])
    exec(ADDRESS['/']+'(q, u, noPage)')
end

def Fontsize q, u, index
    u.style('header', {'position': 'sticky', 'top': '0', 'padding': '5px 0 0 0'})
    u.style('a', {'text-decoration': 'none'})
    u.props['menu'] = 0

    u.props['fontsize'] += 1

    if u.props['fontsize'] == len(TSIZET)+1
        u.props['fontsize'] = 1
    end
    os.environ['FONTSIZE'] = str(u.props['fontsize'])
    os.environ['INDEX'] = str(u.props['index'])

    noPage = str(u.props['index'])
    exec(ADDRESS['/']+'(q, u, noPage)')
end

def Theme qdata, u, index
    u.style('header', {'position': 'sticky', 'top': '0', 'padding': '5px 0 0 0'})
    u.props['menu'] = 0
    u.style('a', {'text-decoration': 'none'})

    if u.props['theme'] == len(COLOR)-1
        u.props['theme'] = 0
    else
        u.props['theme'] = u.props['theme'] + 1
    end
    x = u.props['theme']

    os.environ['BACKGROUNDCOLOR'] = COLOR[x][0]
    os.environ['FIRSTWORDCOLOR'] = COLOR[x][1]
    os.environ['ARABICFONTCOLOR'] = COLOR[x][2]
    os.environ['FONTCOLOR'] = COLOR[x][3]

    os.environ['THEME'] = str(u.props['theme'])
    os.environ['INDEX'] = str(u.props['index'])

    u.props['backgroundcolor'] = os.environ['BACKGROUNDCOLOR']

    noPage = str(u.props['index'])
    exec(ADDRESS['/']+'(qdata, u, noPage)')
end

def View qdata, u, index
    u.style('header', {'position': 'sticky', 'top': '0', 'padding': '5px 0 0 0'})
    u.style('a', {'text-decoration': 'none'})
    u.props['menu'] = 0

    if u.props['view'] == len(VIEWT)-1
        u.props['view'] = 0
    else
        u.props['view'] = u.props['view'] + 1
    end
    os.environ['VIEW'] = str(u.props['view'])
    os.environ['INDEX'] = str(u.props['index'])

    noPage = str(u.props['index'])
    exec(ADDRESS['/']+'(qdata, u, noPage)')
end

def Pertama qdata, u, index
    u.style('header', {'position': 'sticky', 'top': '0', 'padding': '5px 0 0 0'})
    u.style('a', {'text-decoration': 'none'})
    u.props['menu'] = 0

    if u.props['firstword'] == len(HIGHLIGH) - 1
        u.props['firstword'] = 0
    else
        u.props['firstword'] += 1
    end
    os.environ['FIRSTWORD'] = str(u.props['firstword'])
    os.environ['INDEX'] = str(u.props['index'])

    noPage = str(u.props['index'])
    exec(ADDRESS['/']+'(qdata, u, noPage)')
end

def Quran q, u, index
    u.style('header', {'position': 'sticky', 'top': '0', 'padding': '5px 0 0 0'})
    u.style('a', {'text-decoration': 'none'})
    u.props['menu'] = 0

    u.props['print'] = !u.props['print']

    os.environ['PRINT'] = str(u.props['print'])
    os.environ['INDEX'] = str(u.props['index'])

    noPage = str(u.props['index'])
    exec(ADDRESS['/']+'(q, u, noPage)')
end

def Translation qdata, u, index
    u.style('header', {'position': 'sticky', 'top': '0', 'padding': '5px 0 0 0'})
    u.style('a', {'text-decoration': 'none'})
    u.props['menu'] = 0

    u.props['tafsir'] = !u.props['tafsir']

    os.environ['TAFSIR'] = str(u.props['tafsir'])
    os.environ['INDEX'] = str(u.props['index'])

    noPage = str(u.props['index'])
    exec(ADDRESS['/']+'(qdata, u, noPage)')

end
def Word qdata, u, index
    u.style('header', {'position': 'sticky', 'top': '0', 'padding': '5px 0 0 0'})
    u.style('a', {'text-decoration': 'none'})
    u.props['menu'] = 0

    if u.props['word'] == 1
        u.props['word'] = 0
    else
        u.props['word'] = 1
    end
    os.environ['WORD'] = str(u.props['word'])
    os.environ['INDEX'] = str(u.props['index'])

    noPage = str(u.props['index'])
    exec(ADDRESS['/']+'(qdata, u, noPage)')
end

def Mushaf qdata, u, index
    u.style 'header', {'position': 'sticky', 'top': '0', 'padding': '5px 0 0 0',}
    u.style 'a', {'text-decoration': 'none'}
    u.props[:menu] = 0

    u.props[:mushaf] = !u.props[:mushaf]
    
    os.environ['MUSHAF'] = str(u.props['mushaf'])
    os.environ['INDEX'] = str(u.props['index'])

    noPage = str(u.props['index'])
    exec(ADDRESS['/']+'(qdata, u, noPage)')
end
