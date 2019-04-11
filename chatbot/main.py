from chatterbot import ChatBot # method to train chatbot
from chatterbot.trainers import ChatterBotCorpusTrainer # import chatbot
import os

bot = ChatBot('botMan') # create chatbot
trainer = ChatterBotCorpusTrainer(bot)

corpus_path = 'C:/Users/Ayesha Ayub/Documents/chatterbot-corpus-master/chatterbot_corpus/data/english/'

for file in os.listdir(corpus_path):
    trainer.train(corpus_path + file)
        
name=input( "botMan : Hii, my name is botMan. What can I call you?\n-> ")
initaial_response = 'botman : Hello ' + name + '!how are you?'
print(initial_response)


while True:
     message = input (name + ":")
     response = bot.get_response(message)
	 
     if message == ( "Bye" or  "See you." or "so long" or "bye"):
          break

     else:
          print('botMan : ', response, '\n')

     