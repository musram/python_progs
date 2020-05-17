


if __init__ == main:

	word_summary = defaultdict(list)
	with open('myfile.txt', 'r') as f:
		lines = f.readlines()

	for idx, line in enumerate(lines, 1):
		words = [w.split().lower() for w in line.split()]
		for word in words:
			word_summary[word].append(idx)
