require "sinatra"

if $0 == __FILE__

    get '/' do
        "Mushaf"
    end

    get '/daily' do
        "Daily Ayat"
    end

    get '/page/:no' do |x|
        "Page #{params[:no]}"
    end

    get '/sura/:no' do
        "Sura #{params[:no]}"
    end

    get '/juz/:no' do
        "Juz #{params[:no]}"
    end

end