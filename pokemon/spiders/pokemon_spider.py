# -*- coding: utf-8 -*-
ww
import scrapy
import re

class PokemonSpider(scrapy.Spider):
	name = "pokemon"

	start_urls = ["https://pokemondb.net/pokedex/national"]

	def parse(self, response):
		page = response.css('article.main-content div.infocard-tall-list span.infocard-tall a.ent-name::attr(href)').extract()
		for pokemon in page:
			if pokemon is not None:
				yield response.follow(pokemon, callback=self.parse_pokemon)

	def parse_pokemon(self, response):
		def css_extract(query):
			return response.css(query).extract_first().strip()
		yield {
			'number': response.xpath('//tbody/tr[contains(th, "National")]/td/strong/text()').extract_first(),
			'name': css_extract('article h1::text'),
			'type': response.css('div.colset div.col p a.itype::text').extract(),
			'weight': re.search(r"\((\d+\.\d+)", response.xpath('//tbody/tr[contains(th, "Weight")]/td/text()').extract_first()).group(1),
			'height': re.search(r"\((\d+\.\d+)", response.xpath('//tbody/tr[contains(th, "Height")]/td/text()').extract_first()).group(1),
			'hp': response.xpath('//tbody/tr[contains(th, "HP")]/td/text()').extract_first(),
			'attack': response.xpath('//tbody/tr[contains(th, "Attack")]/td/text()').extract_first(),
			'defense': response.xpath('//tbody/tr[contains(th, "Defense")]/td/text()').extract_first(),
			'spattack': response.xpath('//tbody/tr[contains(th, "Sp. Atk")]/td/text()').extract_first(),
			'spdefense': response.xpath('//tbody/tr[contains(th, "Sp. Def")]/td/text()').extract_first(),
			'speed': response.xpath('//tbody/tr[contains(th, "Speed")]/td/text()').extract_first(),
		}
