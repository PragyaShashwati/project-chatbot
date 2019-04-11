#!C:\Program Files (x86)\Python37-32\python.exe
print("Content-type: text/html\r\n\r\n") 

import cgi
import os
import wikipedia

message=[]
message[1]="hello!what do u want to know abt today?"

template-top = '''<!doctype html>
<html>
	<head>
		<title>botman</title>
		<link rel = "stylesheet" type = "text/css" href = "css/bot.css">
	</head>
	
	<body>
	
	
		<div class ="chatbox">
			<div class ="chatlogs">
			
				<div class="chat bot">
					<div class = "user-photo"></div>
					<p class = "chat-message">Hello how are you?</p>
				</div>
				
				<div class="chat self">
					<div class = "user-photo"></div>
					<p class = "chat-message">I am fine.</p>
				</div>'''
print(template_top)
				
template_middle_bot ='''				<div class="chat bot">
					<div class = "user-photo"></div>
					<p class = "chat-message">Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.</p>
				</div>'''
				
template_middle_self='''				<div class="chat self">
					<div class = "user-photo"></div>
					<p class = "chat-message">It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using 'Content here, content here', making it look like readable English. Many desktop publishing packages and web page editors now use Lorem Ipsum as their default model text, and a search for 'lorem ipsum' will uncover many web sites still in their infancy. Various versions have evolved over the years, sometimes by accident, sometimes on purpose (injected humour and the like).</p>
				</div>
				
				<div class="chat bot">
					<div class = "user-photo"></div>
					<p class = "chat-message">Hello how are you?</p>
				</div>
				
				<div class="chat self">
					<div class = "user-photo"></div>
					<p class = "chat-message">I am fine.</p>
				</div>
				
			</div>'''
			
templte_bottom='''			<div class ="chat-form">
				<textarea name ="term" id="></textarea>
				<button>send</button>
			</div>
		</div>
		
	</body>
</html>'''
print(template)