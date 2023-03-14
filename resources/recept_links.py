def recept_links():
	all_links = input('Copie e cole o link completo aqui: ')

	if len(all_links) < 43:
		while len(all_links) < 43:
			print('O link está incorreto, por favor tente novamente. ')
			all_links = input('Copie e cole o link completo aqui: ')
	else:
		pass

	return all_links