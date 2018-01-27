#Key: 5111f0da1fe0402ba1f08867dc513e8b
# sports
# /alexa-yoda-skill/microservices/bot/app/src

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
	url = "https://newsapi.org/v2/top-headlines?country=in&category=entertainment&pagesize=1&page=2&apiKey=5111f0da1fe0402ba1f08867dc513e8b"
	headers = {
		"Content-Type": "application/json",
		"X-api-key": "5111f0da1fe0402ba1f08867dc513e8b"
	}
	response= requests.get(url)
	respObj = response.json()
	for element in respObj['articles']:
		x= element['description']
	return x;

def getSports():
	url = "https://newsapi.org/v2/top-headlines?country=in&category=sports&pagesize=1&page=2&apiKey=5111f0da1fe0402ba1f08867dc513e8b"
	headers = {
		"Content-Type": "application/json",
		"X-api-key": "5111f0da1fe0402ba1f08867dc513e8b"
	}
	response= requests.get(url)
	respObj = response.json()
	for element in respObj['articles']:
		x= element['description']
	return x;

def getHistory():
	url = "http://numbersapi.com/"+str(now.month)+"/"+str(now.day)+"/date?json"
	response= requests.get(url)
	respObj = response.json()
	return respObj['text']

def getTrivia():
	url = "http://numbersapi.com/random/trivia?json"
	response= requests.get(url)
	respObj = response.json()
	return respObj['text']

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
    response = quote + '...... mmmmmmm ......... Do you want more?'
    return question(response)

@ask.intent("YesIntent")
def shareQuote():
    quote = getYodaQuote()
    response = quote + '...... mmmmmmm ......... Do you want more?'
    return question(response)

@ask.intent("NoIntent")
def noIntent():
    byeText = 'Lol... OK... Bye'
    return statement(byeText)

