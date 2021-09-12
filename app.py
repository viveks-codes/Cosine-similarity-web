from pywebio.input import input, FLOAT
from pywebio.output import put_text
from pywebio.platform.flask import webio_view
from pywebio import STATIC_PATH
from flask import Flask, send_from_directory
from pywebio.input import *
from pywebio.output import *
import argparse
from pywebio import start_server
from pywebio.session import *
import numpy as np
import csv 
import re
from pywebio.input import *
from pywebio.output import put_html, put_loading
import re
import math



def cosineSimilarity():
	mode = radio("select mode ", options=['Manual', 'File upload'])
	if(mode=='Manual'):
		# create list for unique words
		universalSetOfUniqueWords = []
		matchPercentage = 0
		# converting user quesry into lowercase

		inputQuery = input("Enter your query: ",type=TEXT)
		lowercaseQuery = inputQuery.lower()
		queryWordList = re.sub("[^\w]", " ",lowercaseQuery).split()
		# finding unique words from query
		for word in queryWordList:
			if word not in universalSetOfUniqueWords:
				universalSetOfUniqueWords.append(word)
		inputQuery2 = input("Enter your query: ",type=TEXT)
		lowercaseQuery2 = inputQuery2.lower()
		queryWordList2 = re.sub("[^\w]", " ",lowercaseQuery2).split()
		# finding unique words from query
		for word in queryWordList2:
			if word not in universalSetOfUniqueWords:
				universalSetOfUniqueWords.append(word)
		
		#fd = open("database1.txt", "r")
		#database1 = fd.read().lower()
		# finding unique words from list 2
		#databaseWordList = re.sub("[^\w]", " ",database1).split()	
		#for word in databaseWordList:
		#	if word not in universalSetOfUniqueWords:
		#		universalSetOfUniqueWords.append(word)
				
		queryTF = []
		databaseTF = []

		for word in universalSetOfUniqueWords:
			queryTfCounter = 0
			databaseTfCounter = 0

			for word2 in queryWordList:
				if word == word2:
					queryTfCounter += 1
			queryTF.append(queryTfCounter)

			for word2 in queryWordList2:
				if word == word2:
					databaseTfCounter += 1
			databaseTF.append(databaseTfCounter)

		dotProduct = 0
		for i in range (len(queryTF)):
			dotProduct += queryTF[i]*databaseTF[i]

		queryVectorMagnitude = 0
		for i in range (len(queryTF)):
			queryVectorMagnitude += queryTF[i]**2
		queryVectorMagnitude = math.sqrt(queryVectorMagnitude)

		databaseVectorMagnitude = 0
		for i in range (len(databaseTF)):
			databaseVectorMagnitude += databaseTF[i]**2
		databaseVectorMagnitude = math.sqrt(databaseVectorMagnitude)
		cosine = float(dotProduct / (queryVectorMagnitude * databaseVectorMagnitude))
		matchPercentage = cosine*100


		output = "Input query text matches {}% with database.".format(matchPercentage)
		outputcosine = " Cosine similarity between 2 document is {}".format(cosine)
		put_text("total number of words in string A : {}".format(len(inputQuery)))
		put_text("total number of words in string B : {}".format(len(inputQuery2)))
		put_text("total number of unique words in both Strings : {}".format(len(universalSetOfUniqueWords)))
		put_text("magnitude of string A is {}".format(queryVectorMagnitude))
		put_text("magnitude of string B is {}".format(databaseVectorMagnitude))
		put_text(output)
		put_text(outputcosine)
	else :

		# create list for unique words
		universalSetOfUniqueWords = []
		matchPercentage = 0
		# converting user quesry into lowercase
		inputQuery = file_upload(label='Upload txt file', accept='.txt')
		inputQuery = inputQuery['content']
		#print(inputQuery)
		lowercaseQuery = str(inputQuery).lower()
		queryWordList = re.sub("[^\w]", " ",lowercaseQuery).split()
		# finding unique words from query
		for word in queryWordList:
			if word not in universalSetOfUniqueWords:
				universalSetOfUniqueWords.append(word)
		inputQuery2 = file_upload(label='Upload txt file', accept='.txt')
		inputQuery2 = inputQuery2['content']
		#print(inputQuery2)
		lowercaseQuery2 = str(inputQuery2).lower()
		queryWordList2 = re.sub("[^\w]", " ",lowercaseQuery2).split()
		# finding unique words from query
		for word in queryWordList2:
			if word not in universalSetOfUniqueWords:
				universalSetOfUniqueWords.append(word)
		
		#fd = open("database1.txt", "r")
		#database1 = fd.read().lower()
		# finding unique words from list 2
		#databaseWordList = re.sub("[^\w]", " ",database1).split()	
		#for word in databaseWordList:
		#	if word not in universalSetOfUniqueWords:
		#		universalSetOfUniqueWords.append(word)
				
		queryTF = []
		databaseTF = []

		for word in universalSetOfUniqueWords:
			queryTfCounter = 0
			databaseTfCounter = 0

			for word2 in queryWordList:
				if word == word2:
					queryTfCounter += 1
			queryTF.append(queryTfCounter)

			for word2 in queryWordList2:
				if word == word2:
					databaseTfCounter += 1
			databaseTF.append(databaseTfCounter)

		dotProduct = 0
		for i in range (len(queryTF)):
			dotProduct += queryTF[i]*databaseTF[i]
		#outdot = " dot product between 2 document is {}".format(dotProduct)
		
		queryVectorMagnitude = 0
		for i in range (len(queryTF)):
			queryVectorMagnitude += queryTF[i]**2
		queryVectorMagnitude = math.sqrt(queryVectorMagnitude)
		#outmag = " Magnitude of document is {}".format(dotProduct)
		databaseVectorMagnitude = 0
		for i in range (len(databaseTF)):
			databaseVectorMagnitude += databaseTF[i]**2
		databaseVectorMagnitude = math.sqrt(databaseVectorMagnitude)

		cosine = float(dotProduct / (queryVectorMagnitude * databaseVectorMagnitude))
		matchPercentage = cosine*100



		output = "Input query text matches {}% with database.".format(matchPercentage)
		outputcosine = " Cosine similarity between 2 document is {}".format(cosine)
		put_text("total number of char in doc1 : {}".format(len(inputQuery)))
		put_text("total number of char in doc2 : {}".format(len(inputQuery2)))
		put_text("total number of unique words in both docs : {}".format(len(universalSetOfUniqueWords)))
		put_text("magnitude of Doc 1 is {}".format(queryVectorMagnitude))
		put_text("magnitude of doc 2 is {}".format(databaseVectorMagnitude))
		put_text(output)
		put_text(outputcosine)

	
app = Flask(__name__)

app.add_url_rule('/tool', 'webio_view', webio_view(cosineSimilarity),methods=['GET', 'POST', 'OPTIONS'])
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--port", type=int, default=8080)
    args = parser.parse_args()
    start_server(cosineSimilarity,port=args.port)

app.run()
