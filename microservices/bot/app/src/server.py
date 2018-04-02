from src import app
from flask_ask import Ask, statement, question, session
import json
import requests
import time
import unidecode
import random
import datetime
from collections import namedtuple

now = datetime.datetime.now()

ask = Ask(app, "/yoda_quotes")
def getEntertainment():
	rand= random.randint(1, 9);
	url = "https://newsapi.org/v2/top-headlines?country=in&category=entertainment&pagesize=1&page="+str(rand)+"&apiKey=5111f0da1fe0402ba1f08867dc513e8b"
	headers = {
		"Content-Type": "application/json",
		"X-api-key": "5111f0da1fe0402ba1f08867dc513e8b"
	}
	response= requests.get(url)
	respObj = response.json()
	for element in respObj['articles']:
		x= "did you know "+element['description']
	return x;

def getSports():
	rand= random.randint(1, 9);
	url = "https://newsapi.org/v2/top-headlines?country=in&category=sports&pagesize=1&page="+str(rand)+"&apiKey=5111f0da1fe0402ba1f08867dc513e8b"
	headers = {
		"Content-Type": "application/json",
		"X-api-key": "5111f0da1fe0402ba1f08867dc513e8b"
	}
	response= requests.get(url)
	respObj = response.json()
	for element in respObj['articles']:
		x= "did you know "+element['description']
	return x;

def getHistory():
	url = "http://numbersapi.com/"+str(now.month)+"/"+str(now.day)+"/date?json"
	response= requests.get(url)
	respObj = response.json()
	return "did you know "+respObj['text']

def getTrivia():
	url = "http://numbersapi.com/random/trivia?json"
	response= requests.get(url)
	respObj = response.json()
	return "did you know "+respObj['text']

def getYodaQuote():
	rand= random.randint(1, 4);
	if rand== 1 :
		return getEntertainment()

	elif rand== 2 :
		return getSports()

	elif rand== 3 :
		return getHistory()

	else:
		return getTrivia()

@app.route('/')
def homepage():
    return "Alexa skill is running."

@ask.launch
def startSkill():
    quote = getYodaQuote()
    response = quote + '.. hmmm Do you want more?'
    return question(response)

@ask.intent("YesIntent")
def shareQuote():
    quote = getYodaQuote()
    response = quote + '.. hmmm  Do you want more?'
    return question(response)

@ask.intent("NoIntent")
def noIntent():
    byeText = 'Fine... OK... Bye'
    return statement(byeText)


@ask.intent("Help")
def noIntent():
    helpText = 'Just say... Alexa, launch nice icebreaker'
    return question(helpText)
