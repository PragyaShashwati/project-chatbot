import wikipedia
#term = input("what would you like to learn about?")
#print(wikipedia.summary(term,sentences=10))

name = input("Hi! i am botman. What can i call you? /n :")

while True:
     term = input (name + ":")
     response = wikipedia.summary(term, sentences=5)
	 
     if term == ( "Bye" or  "See you" or "so long" or "bye"):
          break

     else:
          print('botMan : ', response, '\n Is there anything else you would like to know?')
		  
		  
		 