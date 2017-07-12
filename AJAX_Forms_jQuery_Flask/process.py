
from flask import Flask, render_template, request, jsonify
import requests
from bson.json_util import dumps

from pymongo import MongoClient
cli = MongoClient()
db = cli['locations']
app = Flask(__name__)

@app.route('/')
def index():
	return render_template('form.html')




def games():
	data = db['locations.main'].find()
	x = dumps(data)
	return x


@app.route('/process', methods=['POST'])
def process():
	email = request.form['email']
	name = request.form['name']

	if name and email:

		db['locations.main'].insert_one({'game_name': email, 'game_money_count': name})
		return jsonify({'name' : games()})

	return jsonify({'error' : 'Missing data!'})



@app.route('/cart_append', methods=['POST'])
def cart():
	email = request.form['email']
	name = request.form['name']
	print(games)
	if name and email:
		newName = name[::-1]
		db['locations.main'].insert_one({'game_name': email, 'game_money_count': name})
		return jsonify({'name' : games()})

	return jsonify({'error' : 'Missing data!'})

if __name__ == '__main__':
	app.run(debug=True)