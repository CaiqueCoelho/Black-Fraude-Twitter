#x dados que eu tenho e y lado que queremos prever
import csv
import re

def separando():

	arquivo = open('BlackFraude_2019-12-04 02:18:46.030956_.csv', 'r')
	leitor = csv.reader(arquivo)

	next(leitor)

	i = 1

	#for Tarefa, Estimativa in leitor:
	for created_at, id_tweet, created_at, tweet in leitor:

		nome_arquivo = "tweet_black_fraude_" + str(i) + ".txt"

		dado = str(tweet)

		dado = dado.lower()

		dado = re.sub('http://\S+|https://\S+', '', dado)
		#OR 
		dado = re.sub('http[s]?://\S+', '', dado)

		stop_numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'blackfriday', 'blackfridaybrasil', 'etc']
		for number in stop_numbers:
			dado = dado.replace(number, " ")

		dado = dado.replace("r$", " ")
		dado = dado.replace(",", " ")
		dado = dado.replace(".", " ")
		dado = dado.replace("-", " ")
		dado = dado.replace("'", " ")
		dado = dado.replace("@", " ")
		dado = dado.replace("#", " ")
		dado = dado.replace("$", " ")
		dado = dado.replace("%", " ")
		dado = dado.replace("&", " ")
		dado = dado.replace("*", " ")
		dado = dado.replace("(", " ")
		dado = dado.replace(")", " ")
		dado = dado.replace("_", " ")
		dado = dado.replace("<", " ")
		dado = dado.replace(">", " ")
		dado = dado.replace("{", " ")
		dado = dado.replace("}", " ")
		dado = dado.replace("[", " ")
		dado = dado.replace("]", " ")
		dado = dado.replace("\\", " ")
		dado = dado.replace("/", " ")
		dado = dado.replace("\n", " ")
		dado = dado.replace("\t", " ")
		dado = dado.replace("...", " ")
		dado = dado.replace(":", " ")
		dado = dado.replace(";", " ")
		dado = dado.replace("!", " ")
		dado = dado.replace("?", " ")
		dado = dado.replace(".", " ")
		dado = dado.replace("+", " ")
		dado = dado.replace("#blackfraude", " ")
		dado = dado.replace("#blackfridaybrasil", " ")
		dado = dado.replace("#blackfriday", " ")
		dado = dado.replace("friday", " ")
		dado = dado.replace("black", " ")
		dado = dado.replace("blackfriday", " ")

		print(dado)

		#contando palavras na tarefa
		dadosQuebrados = dado.split(' ')

		numeroPalavras = 0
		for palavra in dadosQuebrados:
			numeroPalavras += 1

		#if(numeroPalavras >= 10):

		file = open(nome_arquivo, "w") 
		 
		file.write(dado) 
		file.close() 

		i = i + 1

separando()