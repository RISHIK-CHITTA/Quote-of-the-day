from datetime  import datetime as dt
from flask import Flask, jsonify, request
from flask_cors import CORS
import random
import json

with open('data.json') as f:
    quotes = json.load(f)["quotes"]

app = Flask(__name__)
CORS(app)  
@app.route('/quote', methods=['GET'])
def get_quote():
    quote = random.choice(quotes)
    return jsonify(quote)
@app.route('/quoteoftheday', methods=['GET'])
def get_quote_of_the_day():
    today = dt.now().date()
    random.seed(today.toordinal())
    quote_of_the_day = random.choice(quotes)
    return quote_of_the_day
@app.route('/searchquote', methods=['POST'])
def search_quote():
    data = request.get_json()  
    author = str(data) 
    q=[]
    for i in quotes:
        if str(i["author"]).lower()==author.lower():
            q.append(i)
    
    if len(author)==0:
        return jsonify({"code":10,"error":"Enter a valid Author Name"})
    if len(q)==0:
        return jsonify({"code":11,"error":"Author Unavailable"})
    else:
        quote = random.choice(q)
        return jsonify(quote)

if __name__ == '__main__':
    app.run(debug=True)
