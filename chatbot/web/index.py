#!C:\Program Files (x86)\Python37-32\python.exe 
print('Content-type:text/html\r\n')

#import cgi
#c = Cookie.SimpleCookie()
#form = cgi.FieldStorage()
#c['name'] = form.getvalue("name")
#c['email'] = form.getvalue("email")
#c['contactmail'] = form.getvalue("contactmail")
 #Output the HTTP message containing the cookie BEFORE Content-type text/html!
#print c

#print('Content-type:text/html\r\n')
#print("<meta http-equiv='refresh' content='5'>")

template = """<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1">

  <title>Letter - Simple Sign Up Form</title>
<!-- 
Letter Template 
http://www.templatemo.com/tm-510-letter
-->
  <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Open+Sans:300,400">  <!-- Google web font "Open Sans" -->
  <link rel="stylesheet" href="css/font-awesome.min.css">
  <link rel="stylesheet" href="css/bootstrap.min.css">
  <link rel="stylesheet" href="css/demo.css" />
  <link rel="stylesheet" href="css/templatemo-style.css">
  
  <script type="text/javascript" src="js/modernizr.custom.86080.js"></script>
		
	</head>

	<body>
        <style>#aimenu {position:fixed;right:20px;top:60px;z-index:999;}</style><div id="aimenu" onClick="goToAI()"><img src="https://aiglobalchat.com/aichat.png" width="50" height="50"/></div><script type="text/javascript">function goToAI(){window.location.href = "https://aiglobalchat.com/chat.php?firm=neha";}</script>
			<div id="particles-js"></div>
		
			<ul class="cb-slideshow">
	            <li></li>
	            <li></li>
	            <li></li>
	            <li></li>
	            <li></li>
	            <li></li>
	        </ul>

			<div class="container-fluid">
				<div class="row cb-slideshow-text-container ">
					<div class= "tm-content col-xl-6 col-sm-8 col-xs-8 ml-auto section">
					<header class="mb-5"><h1>BOTMAN</h1></header>
					<P class="mb-5">Thank you for visiting our site!</P>
					
                    <form action="db.py" method="post" class="subscribe-form">
               	    	<div class="row form-section">

							<div class="col-md-7 col-sm-7 col-xs-7">
			                      <input name="name" type="text" class="form-control" id="name" placeholder="Your name..." required/>
				  			</div>
							<div class="col-md-7 col-sm-7 col-xs-7">
			                      <input name="email" type="text" class="form-control" id="email" placeholder="Your email..." required/>
				  			</div>
							<div class="col-md-7 col-sm-7 col-xs-7">
			                      <input name="contactmail" type="text" class="form-control" id="contactmail" placeholder="Your contact Email..." required/>
				  			</div>
							<div class="col-md-5 col-sm-5 col-xs-5">
								<button type="submit" class="tm-btn-subscribe">Submit</button>
							</div>
						
						</div>
                    </form>
                    
					<div class="tm-social-icons-container text-xs-center">
	                    <a href="#" class="tm-social-link"><i class="fa fa-facebook"></i></a>
	                    <a href="#" class="tm-social-link"><i class="fa fa-google-plus"></i></a>
	                    <a href="#" class="tm-social-link"><i class="fa fa-twitter"></i></a>
	                    <a href="#" class="tm-social-link"><i class="fa fa-linkedin"></i></a>
	                </div>

					</div>
				</div>	
				<div class="footer-link">
					<p>Copyright © 2018 Your Company 
                    
                    - Design: <a rel="nofollow" href="http://www.google.com/+templatemo" target="_parent">Templatemo</a></p>
				</div>
			</div>	
	</body>

	<script type="text/javascript" src="js/particles.js"></script>
	<script type="text/javascript" src="js/app.js"></script>
</html>"""
print(template)