require 'open-uri'
require 'nokogiri'
require 'json'
require 'net/http'

uri = URI('https://www.betfair.com/sport/inplay')

https = Net::HTTP.new(uri.host, uri.port)
https.open_timeout = 5
https.use_ssl = true
https.ssl_version = 'SSLv3'
request = Net::HTTP::Get.new(uri.request_uri)
html = https.request(request)

doc = Nokogiri::HTML(html)

bets = []
doc.css('.ui-runner-price').each do |bet|
	bet_value = bet.text.strip
	bets.push(
		bet_value: bet_value
		)
	end

puts JSON.pretty_generate(bets)

