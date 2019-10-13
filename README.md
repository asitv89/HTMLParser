# Многопоточный парсер Web-Сайтов
Парсит сайты в многопотчном режиме.

## Начало работы
Перед использованием нужно создать класс унаследованный от `ParserHTML`.
```python3
from ParserHTML import ParserHTML
from bs4 import BeautifulSoup

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
```
После создаем экземпляр класса, в конструктор передаем массив URL-адресов.
```python3
urls = []
	for i in range(1, 11):
		urls.append(f'https://habr.com/ru/all/page{i}/')

parser = ParserHabr(urls)
```
Теперь вызываем метод `run`
```python3
result = parser.run()
```
