def print_data_prompt(data):
	for game in data: 
		# print(data[game])
		print('\n         %s' % game.upper() )
		print('+----Players Online----+')

		temp = data[game]; 

		for player in temp['players']: 
			print('|'+player+ ''.ljust( abs( len(player) - 22))+ '|')

		print('+--------Kills---------+')


		for killer in temp['kills']:
			pre = '|'+killer+''.ljust( abs( len(killer) - 20))

			print(pre +'%02d' %temp['kills'][killer]+'|')
		print('+----------------------+')
		print('|Total Kills:       %03d|' % temp['total_kills'])
		print('+----------------------+')
		print('\n+----Motivo e Mortes---+')

		for kill_mean in temp['kills_by_means']:
			# print(kill_mean)
			pre = '|'+kill_mean+''.ljust( abs( len(kill_mean) - 20))

			print(pre +'%02d' %temp['kills_by_means'][kill_mean]+'|')
		print('+----------------------+')