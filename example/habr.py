from ParserHTML import ParserHTML
from bs4 import BeautifulSoup
from time import time

class ParserHabr(ParserHTML):
	def parse_data(self, text_html):
		soap = BeautifulSoup(text_html, 'html.parser')
		soaps_title = soap.find_all(class_='post__title_link')

		title = None
		if soaps_title is not None:
			title = []
			for i in soaps_title:
				title.append(i.get_text())

		return title

if __name__ == '__main__':
	urls = [
		'https://habr.com/ru/all/page1/',
		'https://habr.com/ru/all/page2/',
		'https://habr.com/ru/all/page3/',
		'https://habr.com/ru/all/page4/',
		'https://habr.com/ru/all/page5/',
		'https://habr.com/ru/all/page6/',
		'https://habr.com/ru/all/page7/',
		'https://habr.com/ru/all/page8/',
		'https://habr.com/ru/all/page9/',
		'https://habr.com/ru/all/page10/'
	]

	parser = ParserHabr(urls)
	result = parser.run()

	for num, page in enumerate(result):
		print(f'Страница: {num + 1}')
		for title in page:
			print(f'   {title}')
		print('---------------------')
