import os

class LogParser:
	def parse(self, fullpath=''):
		self.__log_file_path = fullpath
		
		#Chegando que o path informado é um arquivo.
		#Casocontrário, o método __check_file_exists lança uma exceção
		self.__check_file_exists()

		for chunk in self.__chunk_lines(): 
			print(chunk)

	def __chunk_lines(self): 
		log = open(self.__log_file_path, 'r')

		for line in log.readlines():
			yield line

	def __check_file_exists(self):
		if not os.path.isfile(self.__log_file_path):
			raise Exception('Path informado não é um arquivo', self.__log_file_path); 
