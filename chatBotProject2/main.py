from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

import time
time.clock = time.time

#*******************************************************************************************
# CONTINUE FROM HERE !!
# import logging
# logger = logging.getLogger() logger.setLevel(logging.CRITICAL)
#*******************************************************************************************
bot = ChatBot("My Bot")

convo = [
    'hello',
    'hi',
    'what is your name ?',
    'My name is Bot!'
]

trainer = ListTrainer(bot)

trainer.train(convo)

# answer = bot.get_response("What is your name ?")
# print(answer)

print("Talk to bot.")
while True:
    query = input("You : ")
    if query.strip() == 'exit':
        break
    answer = bot.get_response(query.strip())
    print(f"Bot : {answer}")