import os

class LogParser:

	def parse(self, fullpath=''):
		self.__log_file_path = fullpath
		
		#Chegando que o path informado é um arquivo.
		#Casocontrário, o método __check_file_exists lança uma exceção
		self.__check_file_exists()

		#Armazena a referência de qual partida o parser está processando
		temp_game_round = 0
		key_game        = ''
		log_parsed      = {}

		for chunk in self.__chunk_lines(): 
		
			if chunk['type'] == 'Kill:': 
				processed = self.__kill_chunk_slice(chunk['content'])
				self.__kill_chunk_rules(log_parsed[key_game], processed)
				continue

			if chunk['type'] == 'InitGame:': 
				key_game             = 'game-'+ str(temp_game_round)
				log_parsed[key_game] = self.__new_game_dictionary()
				continue

			if chunk['type'] == 'ShutdownGame:': 
				temp_game_round += 1

				
		return log_parsed


	def __kill_chunk_rules(self, game, pre):
		#Sempre adicionar um novo kill ao game
		#Verificar se assassino e assassinado estão na lista de players do game.
		#Quantificar assassinato; 
		#    |
		#    Se o 'killer' for <world> será necessário retirar um flag do 'killed'
		#Motivo da mote

		#Incrementa o montante total de mortes na partida. 
		game['total_kills'] += 1

		#Agraga os motivos de mortes numa partida. 
		if not pre['weapon'] in game['kills_by_means']: 
			game['kills_by_means'][pre['weapon']] = 1
		else: 
			game['kills_by_means'][pre['weapon']] += 1
		

		#As duas condicionais abaixo adicionam players desconhecidos na lista de jogadores.
		if not pre['killer'] in game['players'] and pre['killer'] != '<world>':
			game['players'].append(pre['killer']) 

		if not pre['killed'] in game['players'] and pre['killed'] != '<world>':
			game['players'].append(pre['killed']) 

		#No caso do usuário matar a si mesmo
		if pre['killed'] == pre['killer']: 
			return

		#No caso do assassino não existir na lista de matadores
		if not pre['killer'] in game['kills'] and pre['killer'] != '<world>':
			game['kills'][pre['killer']]  = 1 
		elif pre['killer'] != '<world>':
			game['kills'][pre['killer']] += 1 

		#No caso do assassinado não existir na lista de matadores. 
		if not pre['killed'] in game['kills']:
			game['kills'][pre['killed']]  = 0 

		#No caso do usuário se matar com alguma armadilha do cenário. 
		if '<world>' in pre['killer']:
			game['kills'][pre['killed']] -= 1



	def __kill_chunk_slice(self, chunk): 
		# exemplo do padaço kill: 
		#21:42 Kill: 1022 2 22: <world> killed Isgalamido by MOD_TRIGGER_HURT
		index = chunk.rindex(':') + 1
		temp  = chunk[index:]
		temp  = temp.replace('killed', '|').replace('by', '|').split('|')

		result = {
			'killer' : temp[0].rstrip(), 
			'killed' : temp[1].rstrip(), 
			'weapon' : temp[2].rstrip()
		}

		return result


	def __chunk_lines(self): 
		log = open(self.__log_file_path, 'r')

		for line in log.readlines():
			chunk = self.__chunk_is_important(line); 
			if not chunk['status']: 
				continue
			yield chunk

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
