links = []
def capture_link(all_links):
	for i in range(0, len(all_links), 43):
		links.append(all_links[i:i+43])

	return links