import requests
from multiprocessing import Queue, Process, Lock, Manager
from multiprocessing.queues import Empty as QueueEmpty
from abc import ABC, abstractmethod

class ParserHTML(ABC):
	def __init__(self, urls=[], max_process=5):
		self.queue_urls = Queue()
		for i in urls:
			self.queue_urls.put(i)

		self.max_process = max_process
		self.lock_add_result = Lock()

	@abstractmethod
	def parse_data(self, text_html):
		pass

	def get_html(self, url):
		return requests.get(url).text

	def _worker(self, result):
		while True:
			try:
				url = self.queue_urls.get_nowait()
			except QueueEmpty as e:
				break

			html = self.get_html(url)
			parsed_data = self.parse_data(html)
			result.append(parsed_data)

		return result

	def run(self):
		manager = Manager()
		result = manager.list()

		processes = []
		for i in range(self.max_process):
			proc = Process(target=self._worker, args=(result, ))
			proc.deamon = True
			processes.append(proc)

		for proc in processes:
			proc.start()

		for proc in processes:
			proc.join()

		return result
