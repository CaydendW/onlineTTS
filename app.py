from flask import Flask, redirect, url_for, request
import win32com.client as wincl
import time as time

app = Flask(__name__)

@app.route('/SayTest',methods = ['POST', 'GET'])
def login():
   if request.method == 'GET':
      wordstosay = request.args.get('words')

   speak = wincl.Dispatch("SAPI.SpVoice")
   speak.Speak(wordstosay)

   return redirect("x")

@app.route('/main',methods = ['POST', 'GET'])
def hello():   
   html = """
   <html>
    <body style="font-family:'Segoe UI', Tahoma, Geneva, Verdana, sans-serif">
       
       <form action = "x" method = "GET">
          <p>Enter Name:</p>
          <p><input type = "text" name = "words" autocomplete="off" maxlength="250" style="height:120px; width:750px;" /></p>
          <p><input type = "submit" value = "submit" /></p>
       </form>
 
    </body>
   </html> """

   return html

if __name__ == '__main__':
   app.run(debug = True, port = 5000, host = "y")