# onlineTTS
A python/flask program that takes texts from an HTML method and plays it back to you using text to speech. It can even work over the internet.

Note: before using this code you will hav eto do some setup first. At the bottom of the code where it says app.run(debug = True, port = 5000, host = "y") you have to replace y with your machines' IP adress. For example app.run(debug = True, port = 5000, host = "192.168.1.375"). This it's where Flask will host the web server. You will also have to change the x in the part where the HTML5 for the page is written to the domain and port (Default port is 5000) you want to publish it to. For example: 

@app.route('/main',methods = ['POST', 'GET'])
def hello():   
   html = """
   <html>
    <body style="font-family:'Segoe UI', Tahoma, Geneva, Verdana, sans-serif">
       
       <form action = "http://www.putyourwebsiteher.com:5000/SayTest" method = "GET">
          <p>Enter Name:</p>
          <p><input type = "text" name = "words" autocomplete="off" maxlength="250" style="height:120px; width:750px;" /></p>
          <p><input type = "submit" value = "submit" /></p>
       </form>
 
    </body>
   </html> """
you will also have to change the redirect on line 15 to the same address except add a /main instead of /SayTest.

Dependencies: The dependencies are as follows: Flask, jsonify, request and pyttsx3.

If any troubles may arise try opeening your firewall to port 5000, (I am not to be held liable for any damage may ensue)

This is a python 3.7.6 project and I cannot guarantee that it will work in earlier or later versions of python. 

If you would like to use my code please contact me first.
