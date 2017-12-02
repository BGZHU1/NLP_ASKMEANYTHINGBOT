from flask import Flask, render_template, request, jsonify
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

app = Flask(__name__)


english_bot = ChatBot("English Bot", storage_adapter="chatterbot.storage.SQLStorageAdapter")
english_bot.set_trainer(ChatterBotCorpusTrainer)
english_bot.train("chatterbot.corpus.english")

response = {
   "Hello" :"Hi, Welcome to BlockVac, please type blockChain or blockVac to learn more about us! ",
}

response2 = {
   "Creator" : "My creator is Bijie Zhu, you can email her @ bijizhu@yahoo.com",
   "BlockVac" : "BlockVac is a startUp that using ethereum smart contract that automating the insurance settlement process, To learn more, please email us @ bijizhu@yahoo.com or keep typing the things you need to know ",
   "BlockChain" : "a digital ledger in which transactions made in bitcoin or another cryptocurrency are recorded chronologically and publicly.To learn more, please email us @bijizhu@yahoo.com or keep typing the things you need to know",
   "BitCoin" : "Bitcoin is a cryptocurrency and worldwide payment system. It is the first decentralized digital currency – the system works without a central repository or single administrator.",
   "Ethereum" : "Ethereum is an open-source, public, blockchain-based distributed computing platform featuring smart contract functionality"
}



@app.route('/')
def index():
	return render_template('form.html')

@app.route('/process', methods=['POST'])
def process():

	name = request.form['name']
	name = name.lower()
	print(name)
	name = name.replace('?', ' ')
	name = name.replace('.', ' ')
	wordList = name.split()
	#print(type(name))
	newName = "Welcome"
	if "hi" in wordList or "hello" in wordList or "hey" in wordList :
		print(name.split())
		newName = response['Hello']


	elif "creator" in wordList or "creats" in wordList or "created" in wordList :
		newName = response2["Creator"]

	elif "blockvac" in wordList :
		newName = response2["BlockVac"]

	elif "blockchain" in wordList :
		newName = response2["BlockChain"]

	elif "bitcoin" in wordList :
		newName = response2["BitCoin"]

	elif "ethereum" in wordList :
		newName = response2["Ethereum"]

	else :
		newName = "Hi"
		newName = str(english_bot.get_response(name))

	print(newName)
	return jsonify({'name' : newName})

	#return jsonify({'error' : 'Missing data!'})

if __name__ == '__main__':
	app.run(debug=True)
