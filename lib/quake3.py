import os

class LogParser:
	

	def parse(self, fullpath=''):
		self.__log_file_path = fullpath
		
		#Chegando que o path informado é um arquivo.
		#Casocontrário, o método __check_file_exists lança uma exceção
		self.__check_file_exists()

		#Armazena a referência de qual partida o parser está processando
		temp_game_round = 0
		
		log_parsed = {}

		for chunk in self.__chunk_lines(): 
			# print(chunk)

			if chunk['type'] == 'Kill:': 
				#dosomething here
				continue

			if chunk['type'] == 'InitGame:': 
				#dosomething here
				self.log_parsed['game-'+ temp_game_round] = self.__new_game_dictionary()
				continue

			if chunk['type'] == 'ShutdownGame:': 
				#dosomething here
				continue


	def __chunk_lines(self): 
		log = open(self.__log_file_path, 'r')

		for line in log.readlines():
			chunk = self.__chunk_is_important(line); 
			if not chunk['status']: 
				continue
			yield chunk['status']

	#Verifica se a fatia do logo é importante para o contexto do parser
	def __chunk_is_important(self, chunk):
		#pedaços que são importantes contêm
		#Kill: 			(representa um assassinato no jogo)
		#InitGame:      (representa o início do jogo/partida)
		#ShutdownGame:	(representa que o jogo foi finalizado)

		important_labels = ['Kill:', 'InitGame:', 'ShutdownGame:']

		for label in important_labels:
			if label in chunk:
				return {'status': True, 'type': label, 'content': chunk }

		return {'status': False }; 

	#Analisa o caminho do arquivo e lança uma Exception caso seja necessário
	def __check_file_exists(self):
		if not os.path.isfile(self.__log_file_path):
			raise Exception('Path informado não é um arquivo', self.__log_file_path); 

	def __new_game_dictionary(self):
		d = {
			'total_kills'    : 0,
			'players'	     : [], 
			'kills'          : {}, 
			'kills_by_means' : {}
		}
		return d
