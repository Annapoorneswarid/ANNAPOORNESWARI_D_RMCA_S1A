Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
>>> 
>>> def word_count(str):
	counts=dict()
	words=str.split()
	for word in words:
		if word in counts:
			counts[word]+=1
		else:
			counts[word]=1
	return counts

>>> print(word_count('One day a rabbit was boasting about how fast he could run.'))
{'One': 1, 'day': 1, 'a': 1, 'rabbit': 1, 'was': 1, 'boasting': 1, 'about': 1, 'how': 1, 'fast': 1, 'he': 1, 'could': 1, 'run.': 1}
>>> 
>>> 