import asyncio
import discord
import shlex
import logging
import datetime
from discord.ext.commands import Bot
from discord.ext import commands

client = discord.Client()
###################################
#CHANGE YOUR TRIGGER WORD FROM HERE
triggerWord = "kral"
#CHANGE YOUR TRIGGER WORD FROM HERE
###################################

#####################################
#CHANGE YOUR WHITELIST WORD FROM HERE
protectedIDS = ["410530044012789763", "273433751281991681", "449604066759409675", "439544588156534804", "308697726424711179", "471330282474307595", "304501446324387842", "451055396233150474", "439899161127551007", "374540703306350603", "344497557092958210", "196213498844282881", "332464881829937155", "300569216115933194", "447093766956777472", "284470702864728065", "253832857255018496", "284472409090949141", "442238356718485504", "451128375575183390", "208279650860793856", "239103782409994242", "454684427851792384", "308553382853869568", "370187405476757525", "341620641256177664"]
#CHANGE YOUR WHITELIST WORD FROM HERE
#####################################


#Logging and starting
@client.event
async def on_ready():
    print("Cylops' Core Is Online :)\n\nName: %s || ID: %s"%(client.user.name, client.user.id))
    logging.basicConfig(filename='sqBot_Log.log',level=logging.INFO)
    logging.info("----------=[ Logging Started At: %s ]=----------"%(datetime.datetime.now()))
    logging.info(" [ Cylops' Core Is Online -|- Name: %s || ID: %s ] "%(client.user.name, client.user.id))

#Scanning All Messages For Your Trigger Word.
@client.event
async def on_message(message):
    global triggerWord
    global protectedIDS
    try:
        #Whitelist Scan
        for id in protectedIDS:
            if(id == message.author.id):
                return
    except:
        pass
    try:
        #Message Argument Scan
        ss = shlex.split(message.content)
        messageCntnt = message.content.lower()
    except:
        pass
    try:
        #Messages
        if ss[0].lower() == "kral" or ss[0].lower() == "krall" or ss[0].lower() == "kralll" or ss[0].lower() == "krallll" or ss[0].lower() == "kral1" or ss[0].lower() == "kralllll" or ss[0].lower() == "krallllll" or ss[0].lower() == "kralllllll" or ss[0].lower() == "krallllllll" or ss[0].lower() == "kralllllllll" or ss[0].lower() == "krallllllllll" or ss[0].lower() == "kralllllllllll":
            embed = discord.Embed(color=0xff0000)
            embed.add_field(name="Cylops' Sq Bot", value="Sayın, <@%s> \nSQ      SQ\nSQ      SQ\nSQ      SQ\nSQ      SQ\nSQ      SQ\nSQ      SQ"%(message.author.id), inline=False)
            embed.set_thumbnail(url="http://www.sqgc.com/images/logo.png")
            await client.send_message(message.author, embed=embed)
            #print("Word => ['%s'] Has Been Triggered. \nTriggered By %s || Triggered From=> %s || Channel => %s"%(triggerWord, message.author, message.server, message.channel))
            logging.info("Word => ['%s'] Has Been Triggered. || Triggered By %s || Triggered From=> %s || Channel => %s || Time=> %s"%(triggerWord, message.author, message.server, message.channel, datetime.datetime.now()))
        else:
            if messageCntnt.find(triggerWord) > 0 :
                embed = discord.Embed(color=0xff0000)
                embed.add_field(name="Cylops' Sq Bot", value="Sayın, <@%s> \nSQ      SQ\nSQ      SQ\nSQ      SQ\nSQ      SQ\nSQ      SQ\nSQ      SQ"%(message.author.id), inline=False)
                embed.set_thumbnail(url="http://www.sqgc.com/images/logo.png")
                await client.send_message(message.author, embed=embed)
                #print("Word => ['%s'] Has Been Triggered. \nTriggered By %s || Triggered From=> %s || Channel => %s"%(triggerWord, message.author, message.server, message.channel))
                logging.info("Word => ['%s'] Has Been Triggered. || Triggered By %s || Triggered From=> %s || Channel => %s || Time=> %s"%(triggerWord, message.author, message.server, message.channel, datetime.datetime.now()))
            else:
                pass
    except:
        pass


#######################################################
#THIS IS FOR WHO WANTS TO USE HIS OWN ACCOUNT AS A BOT.
client.run('E-MAIL', 'PASS', bot=False)
#THIS IS FOR WHO WANTS TO USE HIS OWN ACCOUNT AS A BOT.
#######################################################




#####################################
#THIS IS WHO WANTS TO USE HIS OWN BOT
#
#client.run('TOKEN')
#
#THIS IS WHO WANTS TO USE HIS OWN BOT
#####################################
