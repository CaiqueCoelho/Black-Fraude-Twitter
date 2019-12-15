from textblob import TextBlob

traducao = TextBlob("I am very sad")
b = TextBlob("I am very happy")

if traducao.detect_language() == 'en':

	if traducao.sentiment.polarity > 0:
		print('positive')

	elif traducao.sentiment.polarity == 0:
		print('neutral')

	else:
		print('negative')