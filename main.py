import keep_alive
import os
import random
import discord
from discord.ext import commands
import requests
import json
import asyncio

my_secret = os.environ['TOKEN']
my_secret2 = os.environ['WeatherAPIKey']


intents = discord.Intents.all()

bot = commands.Bot(command_prefix='!joe', intents = intents)

@bot.event

async def on_connect():
	print("bot is online")


@bot.command()
async def Name(ctx, name):
	await ctx.reply("Hello " + name + " how you doing")




####################
#@bot.command(aliases=["HELP","Help"])
#async def help(ctx):

  
####################


  
@bot.command()
async def Add(ctx, numberOne, numberTwo):
	numberTotal = int(numberOne) + int(numberTwo)
	numberTotal = str(numberTotal)
	await ctx.reply(numberOne + " + " + numberTwo + " = " + numberTotal)

@bot.command()
async def Time(ctx, time, AmPm):
	time = int(time)
	if (AmPm.lower() == "am" and time >= 5):
		await ctx.reply("Good Morning!")
	elif (AmPm.lower() == "pm" and time >= 0 and time <= 6):
		await ctx.reply("Good Afternoon!")
	else:
		await ctx.reply("Good Night!")

@bot.command()
async def picture(ctx):
	await ctx.reply("https://www.loveyourdog.com/wp-content/uploads/2019/07/Chigi-Corgi-Chihuahua-Mix-900x500.jpg")

@bot.command()
async def randomPic(ctx):
	pictures=["https://i.kym-cdn.com/entries/icons/mobile/000/029/043/Shaq_Tries_to_Not_Make_a_Face_While_Eating_Spicy_Wings___Hot_Ones_11-21_screenshot.jpg", "https://ftw.usatoday.com/wp-content/uploads/sites/90/2019/03/screen-shot-2019-03-14-at-1.04.08-pm.jpg?w=1000&h=600&crop=1", "https://preview.redd.it/sa6pn0gki9g71.jpg?width=640&crop=smart&auto=webp&s=b7a30d386cea5ed88cfefb6609c0ec6011fba251", "https://preview.redd.it/ut3ec1gki9g71.jpg?width=640&crop=smart&auto=webp&s=c073de1877a7e9471415bcc009a1f0a71f21fed2", "https://preview.redd.it/epw430gki9g71.jpg?width=640&crop=smart&auto=webp&s=d94e97aa97c51c89285bff18a86bb2cae5f0fc2a"]
	rand = random.choice(pictures)
	await ctx.reply(rand)

@bot.command()
async def eightBall(ctx, *, phrase: str):
	myList=["It is certain", "It is decidedly so", "Without a doubt", "Yes definitely", "Outlook not so good", "Very doubtful", "Better not tell you now", "My sources say no", "My reply is no"]
	rand = random.choice(myList)
	await ctx.reply(phrase + ": " + rand)
	
@bot.command()
async def rps(ctx, choice):
	rpsList=["rock", "paper", "scissors"]
	botchoice = random.choice(rpsList)

	choice = choice.lower()

	if botchoice == choice:
		await ctx.reply("Tie. 🥴 You chose " + choice + " The bot chose " + botchoice)
	elif botchoice == "rock" and botchoice == "scissors":
		await ctx.reply("You LOSE. 🤓 You chose " + choice + " The bot chose " + botchoice)
	elif botchoice == "paper" and botchoice == "rock":
		await ctx.reply("You LOSE. 🤓 You chose " + choice + " The bot chose " + botchoice)
	elif botchoice == "scissors" and botchoice == "paper":
		await ctx.reply("You LOSE. 🤓 You chose " + choice + " The bot chose " + botchoice)
	else:
		await ctx.reply("You WIN. 🙏🙏🙏 You chose " + choice + " The bot chose " + botchoice)

#use a joke api to get a joke setup, wait a few seconds
#and deliver the punch line
@bot.command()
async def Joke(ctx):
	#variable to hold url
	url = "https://official-joke-api.appspot.com/random_joke"

	req = requests.get(url)

	#data variable that holds the json data that the api holds
	data = req.json()

	#pull joke setup from json data
	setup = data["setup"]
	punchline = data["punchline"]
	
	await ctx.reply(setup)
	await asyncio.sleep(3)
	await ctx.send(punchline)


@bot.command()
async def Weather(ctx,zip):
	#variable to hold url
	url = "https://api.openweathermap.org/data/2.5/weather?zip=" + zip + ",us&appid="+my_secret2


	req = requests.get(url)

	data = req.json()

	desc = data["weather"][0]["description"]
	degree = data["main"]["temp"]

	temp = (degree - 273.15) * 9/5 + 32
	await ctx.send(desc + " " + str(temp) + " degrees F")

@bot.command()
async def IP(ctx, ip):

	url = "https://ipinfo.io/" + ip + "/geo"
	req = requests.get(url)

	data = req.json()

	descCity = data["city"]
	descRegion = data["region"]
	descLoc = data["loc"]
	await ctx.send("analyzing " + ip)
	await asyncio.sleep(2)
	await ctx.send("Do you live in " + descRegion)
	await ctx.send("How about " + descCity)
	await ctx.send("I found you 👀 " + descLoc)

@bot.command()
async def LOL(ctx, region, *, username: str):
	url = "https://lol_stats.p.rapidapi.com/" + region + "/" + username
	
	headers = {
		"X-RapidAPI-Key": "1c35b18f16msh826f266abe6d481p1c5ff1jsnc3e466a132c8",
		"X-RapidAPI-Host": "lol_stats.p.rapidapi.com"
	}
	
	response = requests.request("GET", url, headers=headers)

	data = response.json()
	name = data['name']
	soloQ = data['soloQ']
	champName = data['mostPlayedChamps'][0]['champName']
	lpGained = data['mostPlayedChamps'][0]['lpGained']
	kda = data['mostPlayedChamps'][0]['kda']
	wr = data['mostPlayedChamps'][0]['winrate']
	totalgames = data['mostPlayedChamps'][0]['totalGames']

	
	await ctx.send(name + ' ' +  soloQ)
	await ctx.send('your most played champ is ' + champName + ' you gained ' + lpGained + ' lp and your kda is ' + kda + ' with a winrate of ' + wr + ' and played ' + totalgames)
	
@bot.command()
async def urlShortner(ctx, url):
	url = "https://url-shortener-service.p.rapidapi.com/shorten"

	payload = "url=" + url
	headers = {
		"content-type": "application/x-www-form-urlencoded",
		"X-RapidAPI-Key": "1c35b18f16msh826f266abe6d481p1c5ff1jsnc3e466a132c8",
		"X-RapidAPI-Host": "url-shortener-service.p.rapidapi.com"
	}
	
	response = requests.request("POST", url, data=payload, headers=headers)

	data = response.json()
	urlshort = data['result_url']
	await ctx.send(urlshort)

@bot.command()
async def chatBot(ctx, *, message: str):
	url = "https://waifu.p.rapidapi.com/v1/waifu"

	payload = {
		"user_id": "sample_user_id",
		"message": message,
		"from_name": "Boy",
		"to_name": "Girl",
		"situation": "Girl loves Boy.",
		"translate_from": "auto",
		"translate_to": "en"
	}
	headers = {
		"content-type": "application/json",
		"X-RapidAPI-Key": "1c35b18f16msh826f266abe6d481p1c5ff1jsnc3e466a132c8",
		"X-RapidAPI-Host": "waifu.p.rapidapi.com"
	}
	
	response = requests.request("POST", url, json=payload, headers=headers)
	
	data = response.json()
	responser = data['response']
	await ctx.send(responser)
	
@bot.command()
async def getAnime(ctx, rank):
	url = "https://anime-db.p.rapidapi.com/anime/by-ranking/" + rank

	headers = {
		"X-RapidAPI-Key": "1c35b18f16msh826f266abe6d481p1c5ff1jsnc3e466a132c8",
		"X-RapidAPI-Host": "anime-db.p.rapidapi.com"
	}
	
	response = requests.request("GET", url, headers=headers)

	data = response.json()
	title = data['title']
	altTitles = data['alternativeTitles']
	altTitle = ' '.join(map(str,altTitles))
	episodeCount = data['episodes']
	image = data['image']
	synopsis = data['synopsis']
	ranking = data['ranking']

	
	await ctx.send(title + ' aka ' + str(altTitle) + ' ' + str(episodeCount) + ' episodes ' + ' ranked at ' + str(ranking))
	await ctx.send(image)
	await ctx.send(synopsis)
	print(response.text)








keep_alive.keep_alive()
bot.run(my_secret)