import json
import os
import flask
from flask import jsonify
from flask import Flask
from flask import Flask, request, render_template


app = Flask(__name__)



@app.route('/', methods=(['GET','POST']))
def searching():   
 results = [
        {
          "Book Name": "Clean Architecture",
          "Author": "Robert Martin",
          "ISBN": "978-0134494166",
          "Avaliability": "In-Stock",
          "Course": "Advance Software Engineering (CS604-A)",
            
        },
        {
          "Book Name": "Cryptography And Network Security",
          "Author": "William Stallings",
          "ISBN": "978-93-325-8522-5",
          "Avaliability": "In-Stock",
          "Course": "Cryptography (CS625-A)",
         },
        {
          "Book Name": "Fundamentals of Information Systems Security",
          "Author": "David Kim",
          "ISBN": "978-1-284-11645-8",
          "Avaliability": "In-Stock",
          "Course": "Intro to Cyber Security (CS626-A)",

        }    
 
    ]
 
 return jsonify(results)

if __name__ == '__main__':
    app.run()
